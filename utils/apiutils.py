import requests
def authorization_url_fn(authorization_endpoint, client_id, redirect_uri, scope, response_type):
    authorization_url = f"{authorization_endpoint}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type={response_type}"

    return authorization_url

def token_data(token_endpoint,token_data):

    response = requests.post(token_endpoint, data=token_data)
    if response.status_code == 200:
        token_info = response.json()
        access_token = token_info['access_token']
        print("Access Token:", access_token)
    else:
        print("Token request failed:", response.text)
    return access_token