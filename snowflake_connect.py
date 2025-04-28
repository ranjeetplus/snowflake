import snowflake.connector
import pandas as pd

# Create a connection
def create_connection():
    conn = snowflake.connector.connect(
        account = 'PSBVJDC-EE09239',
        user = 'RANJEETPLUS',
        password = 'Learnpython@816107',
        role = 'ACCOUNTADMIN',
        warehouse = 'COMPUTE_WH',
        database = 'PYDB',
        schema = 'PUBLIC',
    )
    return conn


# Fetch data from a table
def fetch_customer_data():
    conn = create_connection()
    query = "SELECT * FROM CUSTOMER_DATA_TABLE"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
