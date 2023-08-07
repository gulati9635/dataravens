import pandas as pd
from datetime import datetime
import sqlalchemy

def extract_tablename(data):
    table_name = list(data.keys())[0]
    return table_name

def create_dataframe(data, key):
    df = pd.json_normalize(data[key])
    return df

def add_timestamp_column(df):
    df['timestamp'] = pd.to_datetime(datetime.now())
    return df

def create_sql_server_engine(server, database, username, password, driver):
    connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"
    engine = sqlalchemy.create_engine(connection_string)
    return engine

def load_dataframe_to_sql(df, table_name, engine, if_exists='replace', index=False):
    df.to_sql(table_name, engine, if_exists=if_exists , index=index)
