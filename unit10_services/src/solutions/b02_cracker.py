from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from binascii import unhexlify

import sys
import binascii
import base64

password="napier"
val="hello world"


def get_key(password):
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password)
    return base64.urlsafe_b64encode(digest.finalize())


key = get_key(password)


print "Key: "+binascii.hexlify(bytearray(key))

cipher_text="6741414141414263706c6c645f707a5f2d6158394c3173623566354d366a6a636d575f5436307a737233764d5446484c634f622d6150794447486d55416a7839685a47496a477870367830455066657344725f376b676457584d38565747586e41773d3d"


cipher_suite = Fernet(key)


plain_text = cipher_suite.decrypt(unhexlify(cipher_text))
print "\nPlain text: "+plain_text

