import passlib.hash;
salt="8sFt66rZ"
string="hello"

def shas(salt, pt):
    print (f"{pt}:SHA1:{passlib.hash.sha1_crypt.hash(pt, salt=salt)}")
    print (f"{pt}:SHA256:{passlib.hash.sha256_crypt.hash(pt, salt=salt)}")
    print (f"{pt}:SHA512:{passlib.hash.sha512_crypt.hash(pt, salt=salt)}")

shas(salt, "changeme")
shas(salt, "123456")
shas(salt, "password")
