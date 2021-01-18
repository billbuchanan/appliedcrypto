from phe import paillier
import sys
vote1=100
vote2=200

def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

if (len(sys.argv)>1):
	vote1=num(sys.argv[1])

if (len(sys.argv)>2):
	vote2=num(sys.argv[2])

public_key, private_key = paillier.generate_paillier_keypair()

keyring = paillier.PaillierPrivateKeyring()

keyring.add(private_key)

public_key1, private_key1 = paillier.generate_paillier_keypair(keyring)


print 'Votes 1=',vote1
print 'Votes 2=',vote2

encrypted1= public_key.encrypt(vote1)
print 'Encrypted1=',encrypted1

encrypted2= public_key.encrypt(vote2)

print 'Encrypted2=',encrypted2

print 'Result =',private_key.decrypt(encrypted1+encrypted2)
