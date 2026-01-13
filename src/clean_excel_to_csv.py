import pandas as pd
from src.config import RAW_XLSX, RAW_CSV, PROCESSED_DIR, CLEAN_CSV

def load_raw() -> pd.DataFrame:
    if RAW_XLSX.exists():
        return pd.read_excel(RAW_XLSX, sheet_name=0)
    if RAW_CSV.exists():
        return pd.read_csv(RAW_CSV)
    raise FileNotFoundError("Put sales_marketing_raw.xlsx or sales_marketing_raw.csv in data/raw/")

def clean_discount(x):
    if pd.isna(x):
        return 0.0
    s = str(x).strip()
    if s.endswith("%"):
        return float(s.replace("%", "")) / 100.0
    return float(s)

def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df = load_raw()

    # Basic column normalization (optional)
    df.columns = [c.strip().lower() for c in df.columns]

    # Clean types
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce", dayfirst=True).dt.date
    df["units"] = pd.to_numeric(df["units"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["shipping_cost"] = pd.to_numeric(df["shipping_cost"], errors="coerce")
    df["ad_spend"] = pd.to_numeric(df["ad_spend"], errors="coerce")
    df["returns"] = pd.to_numeric(df["returns"], errors="coerce").fillna(0).astype(int)

    # Discount percent cleanup
    df["discount_pct"] = df["discount_pct"].apply(clean_discount)

    # Fill missing categories
    for col in ["region", "channel", "product"]:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    # Filters for bad rows
    df = df.dropna(subset=["order_date", "units", "unit_price"])
    df = df[(df["units"] > 0) & (df["unit_price"] > 0)]
    df = df[(df["shipping_cost"].fillna(0) >= 0)]
    df = df[(df["discount_pct"] >= 0) & (df["discount_pct"] <= 0.9)]

    # Create metrics
    df["gross_revenue"] = df["units"] * df["unit_price"]
    df["discount_amount"] = df["gross_revenue"] * df["discount_pct"]
    df["net_revenue"] = df["gross_revenue"] - df["discount_amount"] - df["shipping_cost"].fillna(0)

    df.to_csv(CLEAN_CSV, index=False)
    print(f"Saved: {CLEAN_CSV}")

if __name__ == "__main__":
    main()
