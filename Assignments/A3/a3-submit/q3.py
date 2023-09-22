import requests
import json
import nacl.encoding
from nacl.signing import SigningKey

# q3.1

url = 'https://hash-browns.cs.uwaterloo.ca/api/signed/set-key'
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
api_token = '7ee15d8bf822f9f4537d62d46ca61ea809e29469c226da5a6ad8e6b5b92465d7'
recipient = 'Muffin'
msg = 'Hello, world!'

signing_key = SigningKey.generate()
verify_key = signing_key.verify_key
verify_key_bytes = verify_key.encode()

# convert to base64
base64_encoded_verify_key = nacl.encoding.Base64Encoder.encode(verify_key_bytes)
# convert to string
str_verify_key = base64_encoded_verify_key.decode('utf-8')
print("str_verify_key:", str_verify_key)

# data
data = {'api_token': api_token,
        'pubkey': str_verify_key}
json_data = json.dumps(data)
print("Q3.1")
print("request:", data)

# request
response = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)

# q3.2
url = 'https://hash-browns.cs.uwaterloo.ca/api/signed/send'
signed = signing_key.sign(b"Attack at Dawn")
# convert to base64
base64_encoded_signed_msg = nacl.encoding.Base64Encoder.encode(signed)
# convert to string
str_signed_msg = base64_encoded_signed_msg.decode('utf-8')

# data
data = {'api_token': api_token,
        'recipient': recipient,
        'msg': str_signed_msg}
json_data = json.dumps(data)
print("Q3.2")
print("request:", data)

# request
response = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)
