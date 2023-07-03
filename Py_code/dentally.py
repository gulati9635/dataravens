import utils.dbutils as db
import db_config.connection_config as conn
import db_config.credentials as cred
import utils.apiutils as ap
import api_config.apiconfig

server = conn.server
database = conn.database
port = conn.port
driver = conn.driver
username = cred.username
password = cred.password

db.connect_azure_sql(driver
                     ,server
                     ,port
                     ,database
                     ,username
                     ,password)

ap.oauth2_authentication(client_id,
                         client_secret,
                         token_url,
                         api_url)