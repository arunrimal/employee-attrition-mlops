"""
Prepare data for Feast feature store.
- Uses cleaned `EmployeeAttrition.csv` if present (preferred), otherwise falls back to
  concatenating `data/train.csv` and `data/test.csv` (legacy).
- Ensures an `event_timestamp` column exists for Feast, normalizes entity key to
  `employee_id`, converts column names to snake_case, and writes Parquet.
Run this once: python prepare_feast_data.py
"""

import pandas as pd
from datetime import datetime
from pathlib import Path

# Paths
cleaned_csv = Path("../data/raw/EmployeeAttrition.csv")
train_csv = Path("../data/raw/train.csv")
test_csv = Path("../data/raw/test.csv")
out_path = Path("../data/processed/employee_attrition.parquet")

# Load cleaned CSV if available, else concatenate raw train/test
if cleaned_csv.exists():
    print(f"Using cleaned CSV: {cleaned_csv}")
    df = pd.read_csv(cleaned_csv)
else:
    print("Cleaned CSV not found — falling back to data/train.csv + data/test.csv")
    train_df = pd.read_csv(train_csv, index_col=0) if train_csv.exists() else pd.DataFrame()
    test_df = pd.read_csv(test_csv, index_col=0) if test_csv.exists() else pd.DataFrame()
    df = pd.concat([train_df, test_df], ignore_index=True)

# Add or ensure event_timestamp (Feast requires a timestamp column)
if "event_timestamp" not in df.columns:
    # Use a reasonable default: current UTC time. Replace with real timestamps if available.
    df["event_timestamp"] = pd.to_datetime(datetime.utcnow())

# Normalize entity key
if "Employee ID" in df.columns:
    df = df.rename(columns={"Employee ID": "employee_id"})
elif "employee id" in df.columns:
    df = df.rename(columns={"employee id": "employee_id"})

# Normalize column names to snake_case for Feast compatibility
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Ensure output folder exists
out_path.parent.mkdir(parents=True, exist_ok=True)

# Save as parquet
df.to_parquet(out_path, index=False)

print(f"✓ Saved {len(df)} rows to {out_path}")
print(f"  Columns ({len(df.columns)}): {list(df.columns)}")
print(f"  Entity key: employee_id")
print(f"  Timestamp range: {df['event_timestamp'].min()} to {df['event_timestamp'].max()}")
