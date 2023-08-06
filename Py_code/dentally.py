import utils.dbutils as db
import db_config.connection_config as conn
import db_config.credentials as cred
import webbrowser
import utils.apiutils as apu
import api_config.apiconfig as ap
import pip_package as pp

# db.connect_azure_sql(conn.driver
#                      ,conn.server
#                      ,conn.port
#                      ,conn.database
#                      ,cred.username
#                      ,cred.password)

# db.connect_to_mysql(conn.host, cred.user, cred.password, conn.database)
pp.install_project_dependencies(requirements_file='requirements.txt')
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

table_name = db.extract_tablename(data)
print(table_name)
key = table_name

df = db.create_dataframe(data,key)

final_df= db.add_timestamp_column(df)

print(final_df)

# engine = db.create_sql_server_engine(conn.server,conn.database,cred.username,cred.password,conn.driver)
# db.load_dataframe_to_sql(final_df,table_name, engine, 'replace', False)