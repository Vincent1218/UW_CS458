import requests
import json
import nacl.encoding

# q1.1

url = 'https://hash-browns.cs.uwaterloo.ca/api/plain/send'
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
api_token = '7ee15d8bf822f9f4537d62d46ca61ea809e29469c226da5a6ad8e6b5b92465d7'
recipient = 'Muffin'
msg = 'Hello, world!'
# convert to base64
base64_encoded_msg = nacl.encoding.Base64Encoder.encode(msg.encode('utf-8'))
# convert to string
str_msg = base64_encoded_msg.decode('utf-8')

# data
data = {'api_token': api_token,
        'recipient': recipient,
        'msg': str_msg}
json_data = json.dumps(data)

print("Q1.1")
print("request:", data)

# request
response = requests.post(url, headers=headers, data=json_data).json()

print("response:", response)

# q1.2
url = 'https://hash-browns.cs.uwaterloo.ca/api/plain/inbox'

data = {'api_token': api_token}
json_data = json.dumps(data)

print("Q1.2")
print("request:", data)

# request
response_arr = requests.post(url, headers=headers, data=json_data).json()
print("response_arr:", response_arr)

# response
response = response_arr[0]
str_msg = response.get('msg')

# decode base64
base64_dencoded_msg = nacl.encoding.Base64Encoder.decode(str_msg.encode('utf-8'))
print("response msg:", base64_dencoded_msg.decode('utf-8'))
