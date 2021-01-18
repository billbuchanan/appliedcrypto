from cryptography.fernet import Fernet
import sys
import binascii

operator = "a & b"
x=0
y=0

operator=operator.replace('or','|')
operator=operator.replace('and','&')
operator=operator.replace('xor','^')
operator=operator.replace('not','~')

print "---Input parameters---"
print "Operation:",operator
print "Input:",x,y

keyX_0 = Fernet.generate_key()
keyX_1 = Fernet.generate_key()
keyY_0 = Fernet.generate_key()
keyY_1 = Fernet.generate_key()

data =[]
for a in range(0,2):
	for b in range(0,2):
		data.append(str(eval(operator) & 0x01))
print "Outputs of function:",data

print "\n---Keys generated---"

print "KeyX_0 (first 20 characters):"+binascii.hexlify(bytearray(keyX_0))[:20]
print "KeyX_1 (first 20 characters):"+binascii.hexlify(bytearray(keyX_1))[:20]
print "KeyY_0 (first 20 characters):"+binascii.hexlify(bytearray(keyY_0))[:20]
print "KeyY_1 (first 20 characters):"+binascii.hexlify(bytearray(keyY_1))[:20]

print "\n---Cipers send from Bob to Alice---"


cipher_text00 = Fernet(keyY_0).encrypt(Fernet(keyX_0).encrypt(data[0]))
cipher_text01 = Fernet(keyY_0).encrypt(Fernet(keyX_1).encrypt(data[1]))
cipher_text10 = Fernet(keyY_1).encrypt(Fernet(keyX_0).encrypt(data[2]))
cipher_text11 = Fernet(keyY_1).encrypt(Fernet(keyX_1).encrypt(data[3]))

print "Cipher (first 20 chars): "+binascii.hexlify(bytearray(cipher_text00))[:40]
print "Cipher (first 20 chars): "+binascii.hexlify(bytearray(cipher_text01))[:40]
print "Cipher (first 20 chars): "+binascii.hexlify(bytearray(cipher_text10))[:40]
print "Cipher (first 20 chars): "+binascii.hexlify(bytearray(cipher_text11))[:40]


if (x==0): keyB = keyX_0
if (x==1): keyB = keyX_1

if (y==0): keyA = keyY_0
if (y==1): keyA = keyY_1

print "\n---Bob and Alice's key---"
print "Bob's key: "+binascii.hexlify(bytearray(keyB))[:20]
print "Alice's key: "+binascii.hexlify(bytearray(keyA))[:20]

print "\n---Decrypt with keys (where '.' is an exception):"

try:
	print Fernet(keyB).decrypt(Fernet(keyA).decrypt(cipher_text00)),	
except:
	print ".",
try:
	print Fernet(keyB).decrypt(Fernet(keyA).decrypt(cipher_text01)),	
except:
	print ".",
try:
	print Fernet(keyB).decrypt(Fernet(keyA).decrypt(cipher_text10)),
except:
	print ".",
try:
	print Fernet(keyB).decrypt(Fernet(keyA).decrypt(cipher_text11)),
except:
	print ".",
