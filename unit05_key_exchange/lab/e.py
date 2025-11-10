import hashlib
import binascii
import random

from Crypto.Cipher import AES
from Crypto import Random

msg="test"

def encrypt(word,key, mode):
	plaintext=pad(word)
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	rtn = encobj.decrypt(ciphertext)
	return(rtn)

def pad(s):
    extra = len(s) % 16
    if extra > 0:
        s = s + (' ' * (16 - extra))
    return s

key_size = 256

rnd = random.randint(1,2**key_size)

keyA= hashlib.md5(str(rnd).encode()).digest()

rnd = random.randint(1,2**key_size)

keyB= hashlib.md5(str(rnd).encode()).digest()
 
print('Long-term Key Alice=',binascii.hexlify(keyA))
print('Long-term Key Bob=',binascii.hexlify(keyB))

rnd = random.randint(1,2**key_size)
keySession= hashlib.md5(str(rnd).encode()).hexdigest()

ya = encrypt(keySession.encode(),keyA,AES.MODE_ECB)
yb = encrypt(keySession.encode(),keyB,AES.MODE_ECB)

print("Encrypted key sent to Alice:",binascii.hexlify(ya))
print("Encrypted key sent to Bob:",binascii.hexlify(yb))

decipherA = decrypt(ya,keyA,AES.MODE_ECB)
decipherB = decrypt(yb,keyB,AES.MODE_ECB)

print("Session key:", decipherA)
print("Session key:", decipherB)

