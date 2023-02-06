import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import sys
import hashlib
import binascii

val='hello'
password='hello'
# password='ankle'
# password='changeme'
# password='123456'

plaintext=val

def encrypt(plaintext,key, mode):
    method=algorithms.TripleDES(key)
    cipher = Cipher(method,mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return(ct)

def decrypt(ciphertext,key, mode):
    method=algorithms.TripleDES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)

def pad(data,size=64):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return(padded_data)

def unpad(data,size=64):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)



if (len(sys.argv)>1):
    plaintext=str(sys.argv[1])
if (len(sys.argv)>2):
    password=str(sys.argv[2])
  


# print("Before padding: ",plaintext)
# print("Passphrase: ",password)
  
key = hashlib.sha256(password.encode()).digest()[:16]



# plaintext=pad(plaintext.encode())

ciphertext=binascii.unhexlify("0b8bd1e345e7bbf0")
ciphertext=binascii.unhexlify("6ee95415aca2b33c")
ciphertext=binascii.unhexlify("c08c3078bc88a6c3")
ciphertext=binascii.unhexlify("9d69919c37c375645451d92ae15ea399")
# print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

ciphertext = "/vA6BD+ZXu8j6KrTHi1Y+w=="
print(f'Cipher : {ciphertext}')
ct_b64 = base64.b64decode(ciphertext)
print(f'Cipher ct_b64: {ct_b64}')
# ct_ba = bytearray(ciphertext)
# ct_hx = base64.b64decode(ciphertext).encode('hex')

# # print(f'Cipher : {ct_ba}')
# print(f'Cipher : {ct_hx}')

plaintext = decrypt(ct_b64,key,modes.ECB())

plaintext = unpad(plaintext)
print("  decrypt: ",plaintext.decode())