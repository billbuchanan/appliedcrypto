# https://asecuritysite.com/encryption/padding
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='foxtrotanteatercastle'
val='aaaaaa'
password=''

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password.encode()).digest()


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')

print("After padding (CMS): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)

plaintext = Padding.removePadding(plaintext.decode(),mode='CMS')
print("  decrypt: ",plaintext)

plaintext=val


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')

print("After padding (ZeroLen): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
print("Cipher (ZeroLen): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)

plaintext = Padding.removePadding(plaintext.decode(),mode='ZeroLen')
print("  decrypt: ",plaintext)


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')

print("After padding (Space): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
print("Cipher (Space): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)

plaintext = Padding.removePadding(plaintext.decode(),mode='Space')
print("  decrypt: ",plaintext)


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Random')

print("After padding (Random): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
print("Cipher (Random): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)

plaintext = Padding.removePadding(plaintext.decode(),mode='Random')
print("  decrypt: ",plaintext)