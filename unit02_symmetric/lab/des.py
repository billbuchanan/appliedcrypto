# https://asecuritysite.com/encryption/padding_des

from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

val='foxtrot'
password=''

plaintext=val


def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))


print("\nDES")
key = hashlib.sha256(password.encode()).digest()[:8]

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')

print("After padding (CMS): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,DES.MODE_ECB)
print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)

plaintext = Padding.removePadding(plaintext.decode(),mode='CMS')
print("  decrypt: ",plaintext)