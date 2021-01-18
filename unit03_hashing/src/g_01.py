import hashlib;
import passlib.hash;
import sys;


salt="ZDzPE45C"
string="password"

if (len(sys.argv)>1):
	string=sys.argv[1]

if (len(sys.argv)>2):
	salt=sys.argv[2]

print ("PBKDF2 (SHA1):"+passlib.hash.pbkdf2_sha1.encrypt(string, salt=salt.encode()))
print ("PBKDF2 (SHA256):"+passlib.hash.pbkdf2_sha256.encrypt(string, salt=salt.encode()))


