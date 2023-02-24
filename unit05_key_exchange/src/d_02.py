from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import 
X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import binascii
import sys

Bob_private_key = X25519PrivateKey.generate()

Alice_private_key = X25519PrivateKey.generate()

size=32 # 256 bit key

Bob_shared_key = Bob_private_key.exchange(Alice_private_key.public_key())

Bob_derived_key = 
HKDF(algorithm=hashes.SHA256(),length=size,salt=None,info=b'',backend=default_backend()).derive(Bob_shared_key)

Alice_shared_key = 
Alice_private_key.exchange(Bob_private_key.public_key())

Alice_derived_key = 
HKDF(algorithm=hashes.SHA256(),length=size,salt=None,info=b'',backend=default_backend()).derive(Alice_shared_key)

print ("Name of curve: Curve 25519")

vals = 
binascii.b2a_hex(Bob_private_key.private_bytes(serialization.Encoding.Raw,serialization.PrivateFormat.Raw,serialization.NoEncryption()))
print (f"\nBob private key value: {vals}")
vals=Bob_private_key.public_key()
enc_point=binascii.b2a_hex(vals.public_bytes(encoding=serialization.Encoding.DER,format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
print("Bob's public key: ",enc_point)

vals = 
binascii.b2a_hex(Alice_private_key.private_bytes(serialization.Encoding.Raw,serialization.PrivateFormat.Raw,serialization.NoEncryption()))
print (f"\nAlice private key value: {vals}")
vals=Alice_private_key.public_key()
enc_point=binascii.b2a_hex(vals.public_bytes(encoding=serialization.Encoding.DER,format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
print("Alice's public key: ",enc_point)


print ("\nBob's derived key: ",binascii.b2a_hex(Bob_derived_key).decode())
print("Alice's derived key: 
",binascii.b2a_hex(Alice_derived_key).decode())
