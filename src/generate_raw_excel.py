import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker

from src.config import RAW_DIR, RAW_XLSX, RAW_CSV

fake = Faker()

REGIONS = ["Ontario", "Quebec", "BC", "Alberta", "Manitoba", "Nova Scotia", None, ""]
CHANNELS = ["Meta", "Google", "TikTok", "Organic", "Email", "Affiliate", None, ""]
PRODUCTS = ["Shower Head", "Filter Refill", "Phone Case", "Hoodie", "Water Bottle", "Keyboard", "Mousepad"]

def random_date(start_days_ago: int = 365) -> str:
    d = datetime.today() - timedelta(days=random.randint(0, start_days_ago))
    # Intentionally messy date formats
    fmt = random.choice(["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"])
    return d.strftime(fmt)

def messy_discount() -> object:
    r = random.random()
    if r < 0.10:
        return None
    if r < 0.40:
        return f"{random.choice([5,10,15,20,25,30])}%"
    if r < 0.90:
        return round(random.choice([0.05, 0.1, 0.15, 0.2, 0.25]), 2)
    return "0"  # as string

def maybe_bad_number(x: float) -> object:
    # Occasionally inject bad values (negative or text)
    r = random.random()
    if r < 0.03:
        return -abs(x)
    if r < 0.06:
        return "N/A"
    return x

def generate_rows(n: int = 800) -> pd.DataFrame:
    rows = []
    for i in range(n):
        units = random.randint(1, 6)
        unit_price = round(random.uniform(14.99, 89.99), 2)
        shipping_cost = round(random.uniform(0, 9.99), 2)
        ad_spend = round(max(0, np.random.normal(2.5, 3.0)), 2)

        row = {
            "order_id": f"ORD-{100000+i}",
            "order_date": random_date(365),
            "customer_id": f"CUST-{random.randint(1000, 9999)}",
            "region": random.choice(REGIONS),
            "product": random.choice(PRODUCTS),
            "units": maybe_bad_number(units),
            "unit_price": maybe_bad_number(unit_price),
            "discount_pct": messy_discount(),
            "shipping_cost": maybe_bad_number(shipping_cost),
            "ad_spend": maybe_bad_number(ad_spend),
            "channel": random.choice(CHANNELS),
            "returns": random.choice([0, 0, 0, 0, 1]),  # mostly no returns
        }
        rows.append(row)

    return pd.DataFrame(rows)

def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    df = generate_rows(900)

    # Save CSV too (nice for Databricks upload)
    df.to_csv(RAW_CSV, index=False)

    # Save Excel
    with pd.ExcelWriter(RAW_XLSX, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="raw", index=False)

    print(f"Created: {RAW_XLSX}")
    print(f"Created: {RAW_CSV}")

if __name__ == "__main__":
    main()
