from ecdsa import SigningKey,NIST192p,NIST224p,NIST256p,NIST384p,NIST521p,SECP256k1
import base64
import sys

msg="Hello"
type = 1
cur=NIST192p


sk = SigningKey.generate(curve=cur) 

vk = sk.get_verifying_key()

signature = sk.sign(msg)

print "Message:\t",msg
print "Type:\t\t",cur.name
print "========================="

print "Signature:\t",base64.b64encode(signature)

print "========================="

print "Signatures match:\t",vk.verify(signature, msg)
