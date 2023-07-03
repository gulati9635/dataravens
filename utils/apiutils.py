from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

def oauth2_authentication(client_id, client_secret, token_url, api_url):
    # Obtain access token
    client = BackendApplicationClient(client_id=client_id)
    oauth2_session = OAuth2Session(client=client)
    token = oauth2_session.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)

    # Access the API using the access token
    headers = {'Authorization': f'Bearer {token["access_token"]}'}
    response = oauth2_session.get(api_url, headers=headers)

    if response.status_code == 200:
        # Process the API response
        data = response.json()
        # Do something with the data
        return data
    else:
        print('Error accessing the API:', response.status_code)
        return None
