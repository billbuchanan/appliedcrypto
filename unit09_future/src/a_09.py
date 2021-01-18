import sys
import uuid
import hashlib
import random
 
def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
bob=random.randint(1, 1000)
hash_bob = hash_password(str(bob))
alice=random.randint(1, 1000)
hash_alice = hash_password(str(alice))
print '\n===Bob random and hash=====\n'
print 'Bob random=',bob
print 'Bob hash=',hash_bob
print '\n===Alice random and hash=====\n'
print 'Alice random=',alice
print 'Alice hash=',hash_alice
coin=(bob & 0x1) ^ (alice & 0x1)
if (coin==0):
	print 'Heads ',
else:
	print 'Tails ',
print '\n====Checking the flips ====\n'
print 'Alice checks value with salt: ',check_password(hash_bob,str(bob))
print 'Bob checks value with salt: ',check_password(hash_alice,str(alice))
print '\n====10 random flips====\n'
for i in range(1,10):
	bob=random.randint(1, 1000)
	hash_bob = hash_password(str(bob))
	alice=random.randint(1, 1000)
	hash_alice = hash_password(str(alice))
	coin=(bob & 0x1) ^ (alice & 0x1)
	if (coin==0):
		print 'Heads ',
	else:
		print 'Tails ',