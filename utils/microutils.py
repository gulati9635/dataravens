import pypyodbc as odbc
import requests

def connect_azure_sql(driver,server,port,database,username,password):

    conn_str = f'Driver={{{driver}}};Server=tcp:{server},{port};Database={database};Uid={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    #conn_str = f'Driver={{odbc Driver 18 for SQL Server}};Server=tcp:dentallyprojectserver.database.windows.net,1433;Database=SQLDB;Uid=dentallyproject;Pwd={"Susanoo0609"};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    try:
        conn = odbc.connect(conn_str)
        print("connection established.")
    except odbc.Error as e:
        print(f"Database connection error: {e}")


def get_api_data(api_url, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        # API request successful
        data = response.json()
        return data
    else:
        # API request failed
        print(f"Error {response.status_code}: {response.text}")
        return None


# Example usage
api_url = "https://developer.dentally.co/#patients"
token = "TdSO06XdxjmTMTGmlyL44a062iO-4Hui6noFxXU24I8"
api_data = get_api_data(api_url, token)

