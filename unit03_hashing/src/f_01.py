import passlib.hash;
salt="8sFt66rZ"
string="hello"
print ("SHA1:"+passlib.hash.sha1_crypt.encrypt(string, salt=salt))
print ("SHA256:"+passlib.hash.sha256_crypt.encrypt(string, salt=salt))
print ("SHA512:"+passlib.hash.sha512_crypt.encrypt(string, salt=salt))

