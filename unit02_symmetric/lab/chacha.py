import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
import sys
import binascii
from cryptography.hazmat.backends import default_backend

msg = "edinburgh"
key = "qwerty"

if (len(sys.argv)>1):
  msg=str(sys.argv[1])

if (len(sys.argv)>2):
  key=str(sys.argv[2])

print ("Data:\t",msg)
print ("Key:\t",key)

digest = hashes.Hash(hashes.SHA256(),default_backend())
digest.update(key.encode())
k=digest.finalize()

nonce = b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'
add=''

algorithm = algorithms.ChaCha20(k, nonce)
cipher = Cipher(algorithm, mode=None, backend=default_backend())
encryptor = cipher.encryptor()
ct = encryptor.update(msg.encode())

ct = binascii.unhexlify("e47a2bfe646a")
ct = binascii.unhexlify("ea783afc66")
ct = binascii.unhexlify("e96924f16d6e")
print(f'ct: {ct}')
# ct_b64 = base64.b64decode(ct)

# print(f'ct_b64: {ct_b64}')
pt = cipher.decryptor()
pt=pt.update(ct)

print ("\nKey:\t",binascii.b2a_hex(key.encode()).decode())
print ("Nonce:\t",binascii.b2a_hex(nonce).decode())
print ("\nCipher:\t",binascii.b2a_hex(ct).decode())
print ("Decrypted:\t",pt.decode())
