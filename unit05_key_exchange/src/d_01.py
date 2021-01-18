from os import urandom
from eccsnacks.curve25519 import scalarmult, scalarmult_base
import binascii

a = urandom(32)
a_pub = scalarmult_base(a)

b = urandom(32)
b_pub = scalarmult_base(b)

k_ab = scalarmult(a, b_pub)
k_ba = scalarmult(b, a_pub)

print "Bob public: ",binascii.hexlify(b_pub)
print "Alice public: ",binascii.hexlify(a_pub)
print "Bob shared: ",binascii.hexlify(k_ba)
print "Alice shared: ",binascii.hexlify(k_ab)

