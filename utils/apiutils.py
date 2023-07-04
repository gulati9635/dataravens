from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

import requests

# Define the authorization endpoint and parameters
authorization_endpoint = 'https://api.sandbox.dentally.co/oauth/authorize'
client_id = 'EB7eqfRv1r95QVi3W718ix0pB6RUmS07G7lXqORmM1M'
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
scope = 'appointment patient:read patient:update user:read'
response_type = 'code'

# Construct the authorization URL
authorization_url = f"{authorization_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type={response_type}"

# Redirect the user to the authorization URL
print("Please visit the following URL to authorize the application:")
print(authorization_url)

# After the user grants authorization and is redirected back to the redirect URI:
# Extract the temporary authorization code from the redirected URL
redirected_url = "urn:ietf:wg:oauth:2.0:oob"
#temp_code = redirected_url.split('?code=')[1] # Extract the code from the URL

# Exchange the temporary code for an access token
token_endpoint = 'https://authorization-server.com/token'
client_secret = 'zqWu1B5sMfnZzLKVSWx-xjGJcQzBmEnV-ejDrt9NREc'

token_data = {
    'grant_type': 'authorization_code',
    #'code': temp_code,
    'redirect_uri': redirect_uri,
    'client_id': client_id,
    'client_secret': client_secret
}

response = requests.post(token_endpoint, data=token_data)
print(response.content)

# Parse the response to obtain the access token
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info['access_token']
    print("Access Token:", access_token)
else:
    print("Token request failed:", response.text)
