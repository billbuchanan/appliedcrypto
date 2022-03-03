import hashlib;
import passlib.hash;

salt="0b72ad84e34c9fc218dc92bc13463fd3"
salt=salt.decode('hex')
print 'Salt is ',salt.encode('base64')
string="Hello"

print "PBKDF2 (SHA1):"+passlib.hash.pbkdf2_sha1.encrypt(string, salt=salt,rounds=1000)
print "PBKDF2 (SHA256):"+passlib.hash.pbkdf2_sha256.encrypt(string, salt=salt,rounds=1000)

