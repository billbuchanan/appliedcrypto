import passlib.hash;
import sys;

salt="ZDzPE45C"
string="password"

if (len(sys.argv)>1):
        string=sys.argv[1]

if (len(sys.argv)>2):
        salt=sys.argv[2]

def pbkdf(salt, pt):
    print (f"{pt}: PBKDF2 (SHA1):",passlib.hash.pbkdf2_sha1.hash(pt, salt=salt.encode()))
    print (f"{pt}: PBKDF2 (SHA256):",passlib.hash.pbkdf2_sha256.hash(pt,salt=salt.encode()))

pbkdf(salt, "changeme")
pbkdf(salt, "123456")
pbkdf(salt, "password")
