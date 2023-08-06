import pypyodbc as odbc
import  mysql.connector
import pandas as pd
from datetime import datetime
import sqlalchemy


# def connect_azure_sql(driver,server,port,database,username,password):
#
#     conn_str = f'Driver={{{driver}}};Server=tcp:{server},{port};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
#     #conn_str = f'Driver={{odbc Driver 18 for SQL Server}};Server=tcp:dentallyprojectserver.database.windows.net,1433;Database=SQLDB;Uid=dentallyproject;Pwd={"Susanoo0609"};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
#     try:
#         conn = odbc.connect(conn_str)
#         print("connection established.")
#     except odbc.Error as e:
#         print(f"Database connection error: {e}")

# def connect_to_mysql(host, username, password, database):
#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="root123",
#             database="sql_db"
#         )
#         if connection.is_connected():
#             print("Connected to MySQL database")
#             return connection
#     except mysql.connector.Error as error:
#         print(f"Failed to connect to MySQL database: {error}")
#         return None

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
