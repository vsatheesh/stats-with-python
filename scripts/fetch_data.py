"""Download raw datasets into data/raw/. Re-run any time; files are overwritten.

Usage:  uv run python scripts/fetch_data.py
"""
from pathlib import Path
from urllib.request import urlretrieve

RAW = Path(__file__).resolve().parents[1] / "data" / "raw"

DATASETS = {
    # name: url   (license + citation live in data/SOURCES.md)
    "penguins.csv": "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv",
}


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    for name, url in DATASETS.items():
        dest = RAW / name
        print(f"Downloading {name} ...")
        urlretrieve(url, dest)
        print(f"  -> {dest.relative_to(RAW.parents[1])} ({dest.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
