import passlib.hash;

salt="PkWj6gM4"
string="hello"
print ("APR1:"+passlib.hash.apr_md5_crypt.encrypt(string, salt=salt))


