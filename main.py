from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.load import load_data


DATA_FILE = "data/sales_data_sample.csv"


def run_pipeline():
    print("Starting pipeline...")

    raw_df = extract_data(DATA_FILE)
    print(f"Extracted {len(raw_df)} rows.")

    clean_df = transform_data(raw_df)
    print(f"Transformed {len(clean_df)} rows.")

    load_data(clean_df)
    print(f"Loaded {len(clean_df)} rows into PostgreSQL.")

    print("Pipeline complete.")


if __name__ == "__main__":
    run_pipeline()