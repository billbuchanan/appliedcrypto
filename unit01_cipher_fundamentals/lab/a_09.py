import base64

str = "crypto"
str2 = "crypto1"
print (f'crypto: {base64.b64encode(str.encode())}')
print (f'crypto1: {base64.b64encode(str2.encode())}')
