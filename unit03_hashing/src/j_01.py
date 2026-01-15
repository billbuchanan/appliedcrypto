import hashlib;
import passlib.hash;
import sys;


salt="ZDzPE45C"
string="password"
salt2="1111111111111111111111"


if (len(sys.argv)>1):
	string=sys.argv[1]

if (len(sys.argv)>2):
	salt=sys.argv[2]

print ("General Hashes")
print ("MD5:"+hashlib.md5(string.encode()).hexdigest())
print ("SHA1:"+hashlib.sha1(string.encode()).hexdigest())
print ("SHA256:"+hashlib.sha256(string.encode()).hexdigest())
print ("SHA512:"+hashlib.sha512(string.encode()).hexdigest())

print ("UNIX hashes (with salt)")
print ("DES:"+passlib.hash.des_crypt.hash(string, salt=salt[:2]))
print ("MD5:"+passlib.hash.md5_crypt.hash(string, salt=salt))
print ("Sun MD5:"+passlib.hash.sun_md5_crypt.hash(string, salt=salt))
print ("SHA1:"+passlib.hash.sha1_crypt.hash(string, salt=salt))
print ("SHA256:"+passlib.hash.sha256_crypt.hash(string, salt=salt))
print ("SHA512:"+passlib.hash.sha512_crypt.hash(string, salt=salt))

print ("APR1:"+passlib.hash.apr_md5_crypt.hash(string, salt=salt))
print ("PHPASS:"+passlib.hash.phpass.hash(string, salt=salt))
print("PBKDF2 (SHA1):"+passlib.hash.pbkdf2_sha1.hash(string, salt=salt.encode()))
print ("PBKDF2 (SHA256):"+passlib.hash.pbkdf2_sha256.hash(string, salt=salt.encode()))
print("PBKDF2 (SHA512):"+passlib.hash.pbkdf2_sha512.hash(string, salt=salt.encode()))
print("CTA PBKDF2:"+passlib.hash.cta_pbkdf2_sha1.hash(string, salt=salt.encode()))
print ("DLITZ PBKDF2:"+passlib.hash.dlitz_pbkdf2_sha1.hash(string, salt=salt))

print ("MS Windows Hashes")
print ("LM Hash:"+passlib.hash.lmhash.hash(string))
print ("NT Hash:"+passlib.hash.nthash.hash(string))
print ("MS DCC:"+passlib.hash.msdcc.hash(string, salt))
print ("MS DCC2:"+passlib.hash.msdcc2.hash(string, salt))
        
#print ("LDAP Hashes")
#print ("LDAP (MD5):"+passlib.hash.ldap_md5.hash(string))
#print ("LDAP (MD5 Salted):"+passlib.hash.ldap_salted_md5.hash(string, salt=salt))
#print ("LDAP (SHA):"+passlib.hash.ldap_sha1.hash(string))
#print ("LDAP (SHA1 Salted):"+passlib.hash.ldap_salted_sha1.hash(string, salt=salt))
#print ("LDAP (DES Crypt):"+passlib.hash.ldap_des_crypt.hash(string))
#print ("LDAP (BSDI Crypt):"+passlib.hash.ldap_bsdi_crypt.hash(string))
#print ("LDAP (MD5 Crypt):"+passlib.hash.ldap_md5_crypt.hash(string))
#print ("LDAP (Bcrypt):"+passlib.hash.ldap_bcrypt.hash(string))
#print ("LDAP (SHA1):"+passlib.hash.ldap_sha1_crypt.hash(string))
#print ("LDAP (SHA256):"+passlib.hash.ldap_sha256_crypt.hash(string))
#print ("LDAP (SHA512):"+passlib.hash.ldap_sha512_crypt.hash(string))

print ("LDAP (Hex MD5):"+passlib.hash.ldap_hex_md5.hash(string))
print ("LDAP (Hex SHA1):"+passlib.hash.ldap_hex_sha1.hash(string))
print ("LDAP (At Lass):"+passlib.hash.atlassian_pbkdf2_sha1.hash(string))
print ("LDAP (FSHP):"+passlib.hash.fshp.hash(string))
        
print ("Database Hashes")
print ("MS SQL 2000:"+passlib.hash.mssql2000.hash(string))
print ("MS SQL 2000:"+passlib.hash.mssql2005.hash(string))
print ("MS SQL 2000:"+passlib.hash.mysql323.hash(string))
print ("MySQL:"+passlib.hash.mysql41.hash(string))
print ("Postgres (MD5):"+passlib.hash.postgres_md5.hash(string, user=salt))
print ("Oracle 10:"+passlib.hash.oracle10.hash(string, user=salt))
print ("Oracle 11:"+passlib.hash.oracle11.hash(string))
        
print( "Other Known Hashes")
print ("Cisco PIX:"+passlib.hash.cisco_pix.hash(string, user=salt))
print ("Cisco Type 7:"+passlib.hash.cisco_type7.hash(string))
print ("Dyango DES:"+passlib.hash.django_des_crypt.hash(string, salt=salt))
print ("Dyango MD5:"+passlib.hash.django_salted_md5.hash(string, salt=salt[:2]))
print ("Dyango SHA1:"+passlib.hash.django_salted_sha1.hash(string, salt=salt))
print ("Dyango Bcrypt:"+passlib.hash.django_bcrypt.hash(string, salt=salt2[:22]))
print ("Dyango PBKDF2 SHA1:"+passlib.hash.django_pbkdf2_sha1.hash(string, salt=salt))
print ("Dyango PBKDF2 SHA1:"+passlib.hash.django_pbkdf2_sha256.hash(string, salt=salt))
print ("Bcrypt:"+passlib.hash.bcrypt.hash(string, salt=salt2[:22]))

