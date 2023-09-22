import requests
import json
import nacl.encoding
import nacl.utils
import nacl.hash
from nacl.public import PrivateKey, Box
from nacl.secret import SecretBox

# q5.1

url = 'https://hash-browns.cs.uwaterloo.ca/api/surveil/set-key'
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
api_token = '7ee15d8bf822f9f4537d62d46ca61ea809e29469c226da5a6ad8e6b5b92465d7'
recipient = 'Muffin'

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
print("Q5.1")
print("request:", data)

# request
response = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)

url = 'https://hash-browns.cs.uwaterloo.ca/api/surveil/get-key'


# data
data = {'api_token': api_token,
        'user': recipient}
json_data = json.dumps(data)
print("Q5.1")
print("request:", data)

# request
response = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)
pubkey = response.get('pubkey')
# Decode base 64
mufpk_bytes = nacl.encoding.Base64Encoder.decode(pubkey.encode('utf-8'))


url = 'https://hash-browns.cs.uwaterloo.ca/api/surveil/send'
govpk_base64 = 'fncAcwRlDB33NTNi/Zq0ECiHWoxunpOJ+TFF20PJPDY='
# Decode base 64
govpk_bytes = nacl.encoding.Base64Encoder.decode(govpk_base64.encode('utf-8'))

govpk = nacl.public.PublicKey(govpk_bytes)
mufpk = nacl.public.PublicKey(mufpk_bytes)

msg = "Hello World"

# encrypt message (Secret box)
key = nacl.utils.random(SecretBox.KEY_SIZE)
secretBox = SecretBox(key)
nonce = nacl.utils.random(SecretBox.NONCE_SIZE)
encrypted_msg = secretBox.encrypt(msg.encode('utf-8'), nonce)
# convert to base64
base64_encoded_encrypted_msg = nacl.encoding.Base64Encoder.encode(encrypted_msg)
# convert to string
str_msg = base64_encoded_encrypted_msg.decode('utf-8')


print("key:", key)
# hex encode
# key_hex = key.hex()
# print("key_hex:", key_hex)


# Gov encrypt message key
govBox = Box(sk, govpk)
nonce = nacl.utils.random(Box.NONCE_SIZE)
encrypted_gov_key = govBox.encrypt(key, nonce)
# convert to base64
base64_encoded_encrypted_gov_key = nacl.encoding.Base64Encoder.encode(encrypted_gov_key)
# convert to string
str_gov_key = base64_encoded_encrypted_gov_key.decode('utf-8')

# Muf encrypt message key
mufBox = Box(sk, mufpk)
nonce = nacl.utils.random(Box.NONCE_SIZE)
encrypted_muf_key = mufBox.encrypt(key, nonce)
# convert to base64
base64_encoded_encrypted_muf_key = nacl.encoding.Base64Encoder.encode(encrypted_muf_key)
# convert to string
str_muf_key = base64_encoded_encrypted_muf_key.decode('utf-8')

# data
data = {'api_token': api_token,
        'recipient': recipient,
        'msg': str_msg,
        'recipient_key': str_muf_key,
        'gov_key': str_gov_key}

json_data = json.dumps(data)
print("Q5.1")
print("request:", data)

# request
response = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)

# q5.2
url = 'https://hash-browns.cs.uwaterloo.ca/api/surveil/inbox'

# data
data = {'api_token': api_token}
json_data = json.dumps(data)
print("Q5.2")
print("request:", data)

# request
response_arr = requests.post(url, headers=headers, data=json_data).json()
print("response:", response)

# response
response = response_arr[0]
print("response:", response)
recipient_key = response.get('recipient_key')
msg = response.get('msg')

# decode base64
base64_decoded_encrypted_recipient_key = nacl.encoding.Base64Encoder.decode(recipient_key.encode('utf-8'))

# decrypt recipient key
decrypted_recipient_key = mufBox.decrypt(base64_decoded_encrypted_recipient_key)
print("decrypted_recipient_key:", decrypted_recipient_key)

# decrypt message
base64_decoded_encrypted_msg = nacl.encoding.Base64Encoder.decode(msg.encode('utf-8'))

# decrypt message
secretBox = SecretBox(decrypted_recipient_key)
decrypted_msg = secretBox.decrypt(base64_decoded_encrypted_msg)
print("decrypted_msg:", decrypted_msg.decode('utf-8'))

