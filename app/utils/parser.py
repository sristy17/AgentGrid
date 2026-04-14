import pandas as pd


def parse_csv(file) -> list:
    df = pd.read_csv(file)

    # Ensure required columns exist
    if "revenue" not in df.columns or "cost" not in df.columns:
        raise ValueError("CSV must contain 'revenue' and 'cost' columns")

    # Convert to list of dicts
    data = df[["revenue", "cost"]].to_dict(orient="records")

    return data