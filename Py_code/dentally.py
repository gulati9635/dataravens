
import utils.dbutils as db
import db_config.connection_config as conn
import db_config.credentials as cred
import webbrowser
import utils.apiutils as apu
import api_config.apiconfig as ap


db.connect_azure_sql(conn.driver
                     ,conn.server
                     ,conn.port
                     ,conn.database
                     ,cred.username
                     ,cred.password)

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
apu.token_data(ap.token_endpoint,token_data)



