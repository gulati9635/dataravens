import utils.dbutils as db
import db_config.connection_config as conn
import db_config.credentials as cred

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

