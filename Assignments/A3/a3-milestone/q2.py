import requests
import json
import nacl.encoding
import nacl.secret

# q2.1

url = 'https://hash-browns.cs.uwaterloo.ca/api/psk/send'
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
api_token = '7ee15d8bf822f9f4537d62d46ca61ea809e29469c226da5a6ad8e6b5b92465d7'
recipient = 'Muffin'
msg = 'Hello, world!'

# convert string key to hex
preshared_key = '6e67600583e185e766364cf6467f5c82250560bc28ad5dedba88fa83d1ff38d1'
hex_key = nacl.encoding.HexEncoder.decode(preshared_key.encode('utf-8'))
# encrypt message
box = nacl.secret.SecretBox(hex_key)
nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
encrypted_msg = box.encrypt(msg.encode('utf-8'), nonce)
# convert to base64
base64_encoded_encrypted_msg = nacl.encoding.Base64Encoder.encode(encrypted_msg)
# convert to string
str_msg = base64_encoded_encrypted_msg.decode('utf-8')

# data
data = {'api_token': api_token,
        'recipient': recipient,
        'msg': str_msg}
json_data = json.dumps(data)
print("Q2.1")
print("request:", data)

# request
response = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)

# q2.2
url = 'https://hash-browns.cs.uwaterloo.ca/api/psk/inbox'

# data
data = {'api_token': api_token}
json_data = json.dumps(data)
print("Q2.2")
print("request:", data)

# request
response_arr = requests.post(url, headers=headers, data=json_data).json()
print("response_arr:", response_arr)

# response
response = response_arr[0]
str_msg = response.get('msg')

# decode base64
base64_decoded_encrypted_msg = nacl.encoding.Base64Encoder.decode(str_msg.encode('utf-8'))

# decrypt message
decrypted_msg = box.decrypt(base64_decoded_encrypted_msg)
print("response msg:", decrypted_msg.decode('utf-8'))
