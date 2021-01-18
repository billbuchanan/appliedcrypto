from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

import sys
import binascii
import base64

password="hello"
val="hello world"


def get_key(password):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password)
    return base64.urlsafe_b64encode(digest.finalize())

if (len(sys.argv)>1):
	val=sys.argv[1]

if (len(sys.argv)>2):
	password=str(sys.argv[2])

if (len(password)>1):
	key = get_key(password)
else:
	key = Fernet.generate_key()


print "Key: "+binascii.hexlify(bytearray(key))


cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(val)
cipher=binascii.hexlify(bytearray(cipher_text))
print "Cipher: "+cipher

print "\nVersion:\t"+cipher[0:2]
print "Time stamp:\t"+cipher[2:18]
print "IV:\t\t"+cipher[18:50]
print "HMAC:\t\t"+cipher[-64:]

plain_text = cipher_suite.decrypt(cipher_text)
print "\nPlain text: "+plain_text

