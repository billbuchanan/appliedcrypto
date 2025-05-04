# https://asecuritysite.com/encryption/hash

import sys
from hashlib import md5
import passlib.hash;

import bcrypt
import hashlib;

num = 30
repeat_n=1

salt="ZDzPE45C"
string="the boy stood on the burning deck"
salt2="1111111111111111111111"


print ("Word: ",string)
print ("Salt: ",salt)


print("\nHashes")
print("SHA-1\t",hashlib.sha1(string.encode()).hexdigest())
print("SHA-256\t",hashlib.sha256(string.encode()).hexdigest())
print("SHA-512\t",hashlib.sha512(string.encode()).hexdigest())

print("MD-5:\t\t\t", md5(string.encode()).hexdigest())

print ("UNIX hashes (with salt)")

print("DES:\t\t\t",  passlib.hash.des_crypt.hash(string.encode(), salt=salt[:2]))

print("Bcrypt:\t\t\t", bcrypt.kdf(string.encode(),salt=salt.encode(),desired_key_bytes=32,rounds=100 ).hex())

print("APR1:\t\t\t",  passlib.hash.apr_md5_crypt.hash(string.encode(), salt=salt))

print("PBKDF2 (SHA1):\t\t",  passlib.hash.pbkdf2_sha1.hash(string.encode(),rounds=5, salt=salt.encode()))
print("PBKDF2 (SHA-256):\t", passlib.hash.pbkdf2_sha256.hash(string,rounds=5, salt=salt.encode()))

print ("MS Windows Hashes")

print("LM Hash:\t\t",  passlib.hash.lmhash.hash(string.encode()))
print("NT Hash:\t\t",  passlib.hash.nthash.hash(string.encode()))
print("MS DCC:\t\t\t",  passlib.hash.msdcc.hash(string.encode(), salt))

print ("LDAP Hashes")

print ("LDAP (MD5):"+passlib.hash.ldap_md5.hash(string))
print ("LDAP (MD5 Salted):"+passlib.hash.ldap_salted_md5.hash(string, salt=salt.encode()))
print ("LDAP (SHA):"+passlib.hash.ldap_sha1.hash(string))
print ("LDAP (SHA1 Salted):"+passlib.hash.ldap_salted_sha1.hash(string, salt=salt.encode()))
print ("LDAP (DES Crypt):"+passlib.hash.ldap_des_crypt.hash(string))
print ("LDAP (BSDI Crypt):"+passlib.hash.ldap_bsdi_crypt.hash(string))
print ("LDAP (MD5 Crypt):"+passlib.hash.ldap_md5_crypt.hash(string))
print ("LDAP (Bcrypt):"+passlib.hash.ldap_bcrypt.hash(string))
print ("LDAP (SHA1):"+passlib.hash.ldap_sha1_crypt.hash(string))
print ("LDAP (SHA256):"+passlib.hash.ldap_sha256_crypt.hash(string))
print ("LDAP (SHA512):"+passlib.hash.ldap_sha512_crypt.hash(string))

print ("LDAP (Hex MD5):"+passlib.hash.ldap_hex_md5.hash(string))
print ("LDAP (Hex SHA1):",passlib.hash.ldap_hex_sha1.hash(string))

print ("LDAP (At Lass):",passlib.hash.atlassian_pbkdf2_sha1.hash(string))
print ("LDAP (FSHP):"+passlib.hash.fshp.hash(string))

print ("Database Hashes")

print("MS SQL 2000:\t\t",  passlib.hash.mssql2000.hash(string.encode()))
print("MySQL:\t\t\t",  passlib.hash.mysql41.hash(string.encode()))
print("Oracle 10:\t\t",  passlib.hash.oracle10.hash(string.encode(), user=salt))
print("Postgres (MD5):\t\t", passlib.hash.postgres_md5.hash(string.encode(), user=salt))



print ("Other Known Hashes")
print("Cisco PIX:\t\t",  passlib.hash.cisco_pix.hash(string[:16].encode(), user=salt))
print("Cisco Type 7:\t\t",  passlib.hash.cisco_type7.hash(string.encode()))
print ("Dyango DES:"+passlib.hash.django_des_crypt.hash(string, salt=salt))
print ("Dyango MD5:"+passlib.hash.django_salted_md5.hash(string, salt=salt[:2]))
print ("Dyango SHA1:"+passlib.hash.django_salted_sha1.hash(string, salt=salt))
print ("Dyango Bcrypt:"+passlib.hash.django_bcrypt.hash(string, salt=salt2[:22]))
print ("Dyango PBKDF2 SHA1:"+passlib.hash.django_pbkdf2_sha1.hash(string, salt=salt))
print ("Dyango PBKDF2 SHA1:"+passlib.hash.django_pbkdf2_sha256.hash(string, salt=salt))
# print ("Bcrypt:"+passlib.hash.bcrypt.hash(string, salt=salt2[:22]))

