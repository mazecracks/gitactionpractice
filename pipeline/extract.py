import pandas as pd


def extract_data(file_path):
    """Read sales data from a CSV file."""

    df = pd.read_csv(
        file_path,
        encoding="latin1",
    )

    return df