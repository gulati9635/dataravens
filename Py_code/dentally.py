import utils.microutils as mu
import db_config.connection_config as conn
import db_config.credentials as cred

server = conn.server
database = conn.database
port = conn.port
driver = conn.driver
username = cred.username
password = cred.password

mu.connect_azure_sql(driver
                     ,server
                     ,port
                     ,database
                     ,username
                     ,password)