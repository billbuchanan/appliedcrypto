import passlib.hash;
salt="8sFt66rZ"
string="hello"
print ("SHA1:"+passlib.hash.sha1_crypt.hash(string, salt=salt))
print ("SHA256:"+passlib.hash.sha256_crypt.hash(string, salt=salt))
print ("SHA512:"+passlib.hash.sha512_crypt.hash(string, salt=salt))

