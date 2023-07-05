import requests
import webbrowser

# Define the authorization endpoint and parameters
authorization_endpoint = 'https://api.sandbox.dentally.co/oauth/authorize'
client_id = 'EB7eqfRv1r95QVi3W718ix0pB6RUmS07G7lXqORmM1M'
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
scope = 'appointment patient:read patient:update user:read'
response_type = 'code'

# Construct the authorization URL
authorization_url = f"{authorization_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type={response_type}"

webbrowser.open(authorization_url)

redirected_url = input("Enter the redirected URL: ")

temp_code = redirected_url.split('?code=')[1] # Extract the code from the URL

# Exchange the temporary code for an access token
token_endpoint = 'https://api.sandbox.dentally.co/oauth/token'
client_secret = 'zqWu1B5sMfnZzLKVSWx-xjGJcQzBmEnV-ejDrt9NREc'

token_data = {
    'grant_type': 'authorization_code',
    'code': temp_code,
    'redirect_uri': redirect_uri,
    'client_id': client_id,
    'client_secret': client_secret
}

response = requests.post(token_endpoint, data=token_data)

# Parse the response to obtain the access token
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info['access_token']
    print("Access Token:", access_token)
else:
    print("Token request failed:", response.text)