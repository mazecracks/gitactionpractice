import pandas as pd

from pipeline.transform import transform_data


def create_sample_data():
    """Create a small fake version of our sales data."""

    return pd.DataFrame(
        {
            "ORDERNUMBER": [1001],
            "ORDERLINENUMBER": [1],
            "QUANTITYORDERED": [2],
            "PRICEEACH": [100.00],
            "SALES": [200.00],
            "ORDERDATE": ["01/10/2026"],
            "STATUS": [" Shipped "],
            "PRODUCTLINE": ["Motorcycles"],
            "PRODUCTCODE": ["S10_001"],
            "CUSTOMERNAME": [" Example Company "],
            "CITY": ["London"],
            "COUNTRY": ["UK"],
            "DEALSIZE": ["Small"],
        }
    )


def test_calculated_sales():
    raw_df = create_sample_data()

    result = transform_data(raw_df)

    assert result["calculated_sales"].iloc[0] == 200


def test_columns_are_renamed():
    raw_df = create_sample_data()

    result = transform_data(raw_df)

    assert "order_number" in result.columns
    assert "ORDERNUMBER" not in result.columns


def test_customer_name_is_cleaned():
    raw_df = create_sample_data()

    result = transform_data(raw_df)

    assert result["customer_name"].iloc[0] == "Example Company"