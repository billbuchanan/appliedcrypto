import passlib.hash;

salt="PkWj6gM4"
string="hello"

def apr1(salt, pt):
    print (f"{pt}:APR1:{passlib.hash.apr_md5_crypt.hash(pt, salt=salt)}")

apr1(salt, "changeme")
apr1(salt, "123456")
apr1(salt, "password")