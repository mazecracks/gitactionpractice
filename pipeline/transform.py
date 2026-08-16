import pandas as pd

COLUMNS_TO_KEEP = [
    "ORDERNUMBER",
    "ORDERLINENUMBER",
    "QUANTITYORDERED",
    "PRICEEACH",
    "SALES",
    "ORDERDATE",
    "STATUS",
    "PRODUCTLINE",
    "PRODUCTCODE",
    "CUSTOMERNAME",
    "CITY",
    "COUNTRY",
    "DEALSIZE",
]


COLUMN_NAMES = {
    "ORDERNUMBER": "order_number",
    "ORDERLINENUMBER": "order_line_number",
    "QUANTITYORDERED": "quantity_ordered",
    "PRICEEACH": "price_each",
    "SALES": "sales",
    "ORDERDATE": "order_date",
    "STATUS": "status",
    "PRODUCTLINE": "product_line",
    "PRODUCTCODE": "product_code",
    "CUSTOMERNAME": "customer_name",
    "CITY": "city",
    "COUNTRY": "country",
    "DEALSIZE": "deal_size",
}


def transform_data(df):
    """Clean and transform the raw sales data."""

    # Check that the columns we need exist
    missing_columns = [
        column
        for column in COLUMNS_TO_KEEP
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Keep only the columns we need
    df = df[COLUMNS_TO_KEEP].copy()

    # Rename columns
    df = df.rename(columns=COLUMN_NAMES)

    # Convert numeric columns
    df["order_number"] = pd.to_numeric(
        df["order_number"],
        errors="coerce",
    )

    df["order_line_number"] = pd.to_numeric(
        df["order_line_number"],
        errors="coerce",
    )

    df["quantity_ordered"] = pd.to_numeric(
        df["quantity_ordered"],
        errors="coerce",
    )

    df["price_each"] = pd.to_numeric(
        df["price_each"],
        errors="coerce",
    )

    df["sales"] = pd.to_numeric(
        df["sales"],
        errors="coerce",
    )

    # Convert the order date
    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce",
    ).dt.date

    # Clean text columns
    text_columns = [
        "status",
        "product_line",
        "product_code",
        "customer_name",
        "city",
        "country",
        "deal_size",
    ]

    for column in text_columns:
        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
        )

    # Calculate sales ourselves
    df["calculated_sales"] = (
        df["quantity_ordered"]
        * df["price_each"]
    ).round(2)

    # Remove rows missing important information
    df = df.dropna(
        subset=[
            "order_number",
            "order_line_number",
            "quantity_ordered",
            "price_each",
            "order_date",
        ]
    )

    # Make integer columns integers
    df["order_number"] = df["order_number"].astype(int)

    df["order_line_number"] = (
        df["order_line_number"].astype(int)
    )

    df["quantity_ordered"] = (
        df["quantity_ordered"].astype(int)
    )

    return df