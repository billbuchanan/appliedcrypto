from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
import sys
import binascii
from cryptography.hazmat.backends import default_backend



msg = "edinburgh"
key = "napier"

if (len(sys.argv)>1):
    msg=str(sys.argv[1])

if (len(sys.argv)>2):
    key=str(sys.argv[2])

print ("Data:\t",msg)
print ("Key:\t",key)

digest = hashes.Hash(hashes.SHA256(),default_backend())
digest.update(key.encode())
k=digest.finalize()

algorithm = algorithms.ARC4(k)
cipher = Cipher(algorithm, mode=None, backend=default_backend())
encryptor = cipher.encryptor()
ct = encryptor.update(msg.encode())
print(f'ct: {ct}, type: {type(ct)}')
ct = binascii.unhexlify("8d1cc8bdf6da")
ct = binascii.unhexlify("911adbb2e6dda57cdaad")
ct = binascii.unhexlify("8907deba")
print(f'ct: {ct}, type: {type(ct)}')
pt = cipher.decryptor()
pt=pt.update(ct)


print ("\nKey:\t",binascii.b2a_hex(key.encode()).decode())

print ("\nCipher:\t",binascii.b2a_hex(ct).decode())
print ("Decrypted:\t",pt.decode())

