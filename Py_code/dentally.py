import utils.dbutils as db
import db_config.connection_config as conn
import db_config.credentials as cred
import webbrowser
import utils.apiutils as apu
import api_config.apiconfig as ap
import pandas as pd
# import pymysql
from datetime import datetime
import sqlalchemy



# db.connect_azure_sql(conn.driver
#                      ,conn.server
#                      ,conn.port
#                      ,conn.database
#                      ,cred.username
#                      ,cred.password)

# db.connect_to_mysql(conn.host, cred.user, cred.password, conn.database)

authorization_url = apu.authorization_url_fn(ap.authorization_endpoint,
                                             ap.client_id,
                                             ap.redirect_uri,
                                             ap.scope,
                                             ap.response_type)

webbrowser.open(authorization_url)

redirected_url = input("Enter the redirected URL: ")

temp_code = redirected_url.split('?code=')[1]

token_data = {
    'grant_type': ap.grant_type,
    'code': temp_code,
    'redirect_uri': ap.redirect_uri,
    'client_id': ap.client_id,
    'client_secret': ap.client_secret
}
token_generated = apu.token_data(ap.token_endpoint, token_data)

data = apu.get_api(token_generated, ap.patient_read_endpoint)

table_name = key = list(data.keys())[0]
print(table_name)

df = pd.json_normalize(data[key])

df['timestamp'] = pd.to_datetime(datetime.now())

print(df)

engine = sqlalchemy.create_engine('mysql+pymysql://root:root123@localhost:3306/SQLDB')

df.to_sql(table_name, engine, if_exists='replace', index=False)