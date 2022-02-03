from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
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

chacha = ChaCha20Poly1305(k)
nonce = '\0\0\0\0\0\0\0\0\0\0\0\0'
add=''
cipher = chacha.encrypt(nonce.encode(), msg.encode(), add.encode())
rtn=chacha.decrypt(nonce.encode(), cipher, add.encode())

print ("\nKey:\t",binascii.b2a_hex(key.encode()).decode())
print ("Nonce:\t",binascii.b2a_hex(nonce.encode()).decode())
print ("\nCipher:\t",binascii.b2a_hex(cipher).decode())
print ("Decrypted:\t",rtn.decode())
