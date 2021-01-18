# Zero-knowledge Proof: Proving age with hash chains. 
# https://asecuritysite.com/encryption/age

import hashlib;
import passlib.hash;
import sys;

age_actual=19
age_to_prove=18
seed=b"12345667"

proof = hashlib.md5(seed)
encrypted_age = hashlib.md5(seed)

for i in range(1,1+age_actual-age_to_prove):
	proof = hashlib.md5(proof.digest())

for i in range(1,age_actual+1):
	encrypted_age = hashlib.md5(encrypted_age.digest())

verfied_age=proof

for i in range(0,age_to_prove):
	verfied_age = hashlib.md5(verfied_age.digest())



print "Peggy's Age:\t\t",age_actual
print "Age to prove:\t\t",age_to_prove

print "...."


print "Proof:\t\t",proof.hexdigest()
print "Encr Age:\t",encrypted_age.hexdigest()
print "Verified Age:\t",verfied_age.hexdigest()

if (encrypted_age.hexdigest()==verfied_age.hexdigest()):
	print "You have proven your age ... please come in"
else:
	print "You have not proven you age!"
    