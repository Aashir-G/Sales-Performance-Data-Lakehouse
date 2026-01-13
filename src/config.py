from pathlib import Path

# Project root
ROOT = Path(__file__).resolve().parents[1]

# Data folders
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
SAMPLE_DIR = DATA_DIR / "sample"

# Raw files
RAW_XLSX = RAW_DIR / "sales_marketing_raw.xlsx"
RAW_CSV = RAW_DIR / "sales_marketing_raw.csv"

# Processed files
CLEAN_CSV = PROCESSED_DIR / "silver_sales.csv"
