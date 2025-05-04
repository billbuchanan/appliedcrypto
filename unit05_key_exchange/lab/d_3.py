from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import binascii
import sys

Bob_private_key = ec.generate_private_key(ec.SECP384R1(),default_backend())

Alice_private_key = ec.generate_private_key(ec.SECP384R1(),default_backend())
size=32 # 256 bit key
if (len(sys.argv)>1):
	type=int(sys.argv[1])

if (len(sys.argv)>2):
	size=int(sys.argv[2])

if (type==1): 
  Bob_private_key = ec.generate_private_key(ec.SECP192R1(),default_backend())
  Alice_private_key = ec.generate_private_key(ec.SECP192R1(),default_backend())
elif (type==2): 
  Bob_private_key = ec.generate_private_key(ec.SECP224R1(),default_backend())
  Alice_private_key = ec.generate_private_key(ec.SECP224R1(),default_backend())  
elif (type==3): 
  Bob_private_key = ec.generate_private_key(ec.SECP256K1(),default_backend())
  Alice_private_key = ec.generate_private_key(ec.SECP256K1(),default_backend())
elif (type==4): 
  Bob_private_key = ec.generate_private_key(ec.SECP256R1(),default_backend())
  Alice_private_key = ec.generate_private_key(ec.SECP256R1(),default_backend())  
elif (type==5): 
  Bob_private_key = ec.generate_private_key(ec.SECP384R1(),default_backend())
  Alice_private_key = ec.generate_private_key(ec.SECP384R1(),default_backend())  
elif (type==6): 
  Bob_private_key = ec.generate_private_key(ec.SECP521R1(),default_backend())
  Alice_private_key = ec.generate_private_key(ec.SECP521R1(),default_backend())  
elif (type==7): 
  Bob_private_key = ec.generate_private_key(ec.BrainpoolP256R1(),default_backend())
  Alice_private_key = ec.generate_private_key(ec.BrainpoolP256R1(),default_backend())  
elif (type==8): 
  Bob_private_key = ec.generate_private_key(ec.BrainpoolP384R1(),default_backend())
  Alice_private_key = ec.generate_private_key(ec.BrainpoolP384R1(),default_backend())
elif (type==9): 
  Bob_private_key = ec.generate_private_key(ec.BrainpoolP512R1(),default_backend())
  Alice_private_key = ec.generate_private_key(ec.BrainpoolP512R1(),default_backend())

Bob_shared_key = Bob_private_key.exchange(ec.ECDH(), Alice_private_key.public_key())

Bob_derived_key = HKDF(algorithm=hashes.SHA256(),length=size,salt=None,info=b'',backend=default_backend()).derive(Bob_shared_key)

Alice_shared_key = Alice_private_key.exchange(ec.ECDH(), Bob_private_key.public_key())

Alice_derived_key = HKDF(algorithm=hashes.SHA256(),length=size,salt=None,info=b'',backend=default_backend()).derive(Alice_shared_key)

print ("Name of curve: ",Bob_private_key.public_key().curve.name)
print (f"Generated key size: {size} bytes ({size*8} bits)")

vals = Bob_private_key.private_numbers()
print (f"\nBob private key value: {vals.private_value}")
vals=Bob_private_key.public_key()
enc_point=binascii.b2a_hex(vals.public_bytes(encoding=serialization.Encoding.DER,format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
print("Bob's public key: ",enc_point)

vals = Alice_private_key.private_numbers()
print (f"\nAlice private key value: {vals.private_value}")
vals=Alice_private_key.public_key()
enc_point=binascii.b2a_hex(vals.public_bytes(encoding=serialization.Encoding.DER,format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
print("Alice's public key: ",enc_point)


print ("\nBob's derived key: ",binascii.b2a_hex(Bob_derived_key).decode())
print("Alice's derived key: ",binascii.b2a_hex(Alice_derived_key).decode())




print("\n\n\n== Additional (PEM) ==")

vals = Bob_private_key.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption())
print (f"\nBob private key value (PEM):\n{vals.decode()}")
vals=Bob_private_key.public_key()
enc_point=vals.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode()
print("Bob's public key (PEM):\n",enc_point)

vals = Alice_private_key.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption())
print (f"\nAlice private key value (PEM):\n{vals.decode()}")
vals=Alice_private_key.public_key()
enc_point=vals.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo).decode()
print("Alice's public key (PEM):\n",enc_point)



vals = Bob_private_key.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption())
print (f"\nBob private key value (PEM):\n{vals.decode()}")
vals=Bob_private_key.public_key()
enc_point=vals.public_bytes(encoding=serialization.Encoding.OpenSSH,format=serialization.PublicFormat.OpenSSH).decode()
print("Bob's public key (PEM):\n",enc_point)

vals = Alice_private_key.private_bytes(serialization.Encoding.PEM,serialization.PrivateFormat.PKCS8,serialization.NoEncryption())
print (f"\nAlice private key value (PEM):\n{vals.decode()}")
vals=Alice_private_key.public_key()
enc_point=vals.public_bytes(encoding=serialization.Encoding.OpenSSH,format=serialization.PublicFormat.OpenSSH).decode()
print("Alice's public key (PEM):\n",enc_point)