from kiteconnect import KiteConnect
import json

with open('config.json', 'r') as file:
    config = json.load(file)

# Your API Key and API Secret
kite_api_key = config['KITE_API_KEY']
kite_api_secret = config['KITE_API_SECRET']

kite = KiteConnect(api_key=kite_api_key)

# Get the login URL
login_url = kite.login_url()
print(f"Login URL: {login_url}")

# After visiting the login URL and authenticating, you'll receive a request token.
# Replace 'YOUR_REQUEST_TOKEN' with the actual token you receive.

request_token = "nglf1dEZ9u0KHvn0chcvGCAWfzzAR0FM"
data = kite.generate_session(request_token, api_secret=kite_api_secret)
config['KITE_ACCESS_TOKEN'] = data['access_token']

with open('config.json', 'w') as file:
    json.dump(config, file, indent=4)

kite.set_access_token(data["access_token"])

print("Authentication successful!")
