"""Turn data/raw/* into the tidy CSVs in data/clean/ that episodes load on camera.

Cleaning is kept deliberately minimal: real data stays real (missing values are
kept, because a later episode teaches how to handle them).

Usage:  uv run python scripts/clean_data.py
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
CLEAN = ROOT / "data" / "clean"


def clean_penguins() -> None:
    df = pd.read_csv(RAW / "penguins.csv", na_values=["NA"])
    expected = {
        "species", "island", "bill_length_mm", "bill_depth_mm",
        "flipper_length_mm", "body_mass_g", "sex", "year",
    }
    missing = expected - set(df.columns)
    assert not missing, f"penguins.csv is missing columns: {missing}"
    assert len(df) == 344, f"expected 344 rows, got {len(df)}"
    df.to_csv(CLEAN / "penguins.csv", index=False)
    print(f"penguins.csv: {len(df)} rows, {df.isna().any(axis=1).sum()} rows with a missing value")


def main() -> None:
    CLEAN.mkdir(parents=True, exist_ok=True)
    clean_penguins()


if __name__ == "__main__":
    main()
