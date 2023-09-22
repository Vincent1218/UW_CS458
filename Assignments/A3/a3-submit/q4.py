import requests
import json
import nacl.encoding
import nacl.utils
import nacl.hash
from nacl.public import PrivateKey, Box

# q4.1

url = 'https://hash-browns.cs.uwaterloo.ca/api/pke/get-key'
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
api_token = '7ee15d8bf822f9f4537d62d46ca61ea809e29469c226da5a6ad8e6b5b92465d7'
recipient = 'Muffin'

# data
data = {'api_token': api_token,
        'user': recipient}
json_data = json.dumps(data)
print("Q4.1")
print("request:", data)

# request
response = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)
pubkey = response.get('pubkey')
# Decode base 64
pubkey_bytes = nacl.encoding.Base64Encoder.decode(pubkey.encode('utf-8'))
print("pubkey_bytes:", pubkey_bytes)

# blake2b hashing
hash = nacl.hash.blake2b(pubkey_bytes, encoder=nacl.encoding.HexEncoder)
str_hash = hash.decode('utf-8')
print("hash:", str_hash)

# q4.2
url = 'https://hash-browns.cs.uwaterloo.ca/api/pke/set-key'

sk = PrivateKey.generate()
# public key
pk = sk.public_key

# convert to base64
base64_encoded_pk = nacl.encoding.Base64Encoder.encode(pk.encode())
# convert to string
str_pk = base64_encoded_pk.decode('utf-8')

# data
data = {'api_token': api_token,
        'pubkey': str_pk}
json_data = json.dumps(data)
print("Q4.2")
print("request:", data)

# request
response = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)

# q4.3
url = 'https://hash-browns.cs.uwaterloo.ca/api/pke/send'

# box
print("pk1:", pk)
print("pk2:", pubkey_bytes)
box = Box(sk, nacl.public.PublicKey(pubkey_bytes))

# message
msg = "Hello World"
nonce = nacl.utils.random(Box.NONCE_SIZE)
encrypted = box.encrypt(msg.encode('utf-8'), nonce)
# convert to base64
base64_encoded_encrypted = nacl.encoding.Base64Encoder.encode(encrypted)
# convert to string
str_encrypted = base64_encoded_encrypted.decode('utf-8')

# data
data = {'api_token': api_token,
        'recipient': recipient,
        'msg': str_encrypted}

json_data = json.dumps(data)
print("Q4.3")
print("request:", data)

# request
response = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)

# q4.4
url = 'https://hash-browns.cs.uwaterloo.ca/api/pke/inbox'

# data
data = {'api_token': api_token}
json_data = json.dumps(data)
print("Q4.4")
print("request:", data)

# request
response_arr = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)

# response
response = response_arr[0]
str_msg = response.get('msg')

# decode base64
base64_decoded_encrypted_msg = nacl.encoding.Base64Encoder.decode(str_msg.encode('utf-8'))

# decrypt
decrypted = box.decrypt(base64_decoded_encrypted_msg)
print("decrypted:", decrypted.decode('utf-8'))

