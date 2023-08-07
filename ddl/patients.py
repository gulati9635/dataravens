import pandas as pd
from datetime import datetime

def extract_tablename(data):
    table_name = list(data.keys())[0]
    return table_name

def create_dataframe(data, key):
    df = pd.json_normalize(data[key])
    return df

def add_timestamp_column(df):
    df['timestamp'] = pd.to_datetime(datetime.now())
    return df
