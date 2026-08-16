import os

from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text


load_dotenv()


def get_engine():
    """Create a PostgreSQL database connection."""

    database_url = URL.create(
        drivername="postgresql+psycopg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME"),
    )

    return create_engine(database_url)


def create_sales_table(engine):
    """Create the sales table if it does not already exist."""

    create_table_query = """
    CREATE TABLE IF NOT EXISTS sales (
        id BIGSERIAL PRIMARY KEY,

        order_number INTEGER,
        order_line_number INTEGER,
        quantity_ordered INTEGER,

        price_each NUMERIC(12, 2),
        sales NUMERIC(14, 2),

        order_date DATE,

        status VARCHAR(50),
        product_line VARCHAR(100),
        product_code VARCHAR(50),

        customer_name VARCHAR(255),

        city VARCHAR(100),
        country VARCHAR(100),

        deal_size VARCHAR(50),

        calculated_sales NUMERIC(14, 2)
    );
    """

    with engine.begin() as connection:
        connection.execute(
            text(create_table_query)
        )


def load_data(df):
    """Load transformed sales data into PostgreSQL."""

    engine = get_engine()

    try:
        create_sales_table(engine)

        df.to_sql(
            name="sales",
            con=engine,
            if_exists="append",
            index=False,
        )

    finally:
        engine.dispose()