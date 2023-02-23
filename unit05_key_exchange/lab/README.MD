![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

## Lab 5: Key Exchange
Objective: Key exchange allows us to pass a shared secret key between Bob and Alice. The main methods for doing this are either encrypting with the public key, the Diffie Hellman Method and the Elliptic Curve Diffie Hellman (ECDH) method. This lab investigates these methods.

Web link (Demo): https://youtu.be/Lnw4FhiOwiU

## A	Diffie-Hellman

### A.1	
Bob and Alice have agreed on the values:

g=2879, N= 9929

Bob Select x=6, Alice selects y=9

Now calculate (using a calculator):

Alice’s A value (g<sup>x</sup> mod N):	
	
Bob’s B value (g<sup>y</sup> mod N):

### A.2	
Now they exchange the values. Next calculate the shared key:


Alice’s value (B<sup>x</sup> mod N):	
	
Bobs’s value (A<sup>y</sup> mod N):

Do they match? [Yes] [No]


### A.3	
If you are in the lab, select someone to share a value with. Next agree on two numbers (g and N). 

You should generate a random number, and so should they. Do not tell them what your random number is. Next calculate your A value, and get them to do the same.



Next exchange values.





Numbers for g and N:

Your x value:

Your A value:


The B value you received:

Shared key:

Do they match: [Yes] [No]

## B	OpenSSL (Diffie-Hellman and ECC)


### B.1	
Generate 768-bit Diffie-Hellman parameters:
```
openssl dhparam -out dhparams.pem -text 768 
```

View your key exchange parameters with:

```
cat dhparams.pem	
```

What is the value of g:

How many bits does the prime number have?

How long does it take to produce the parameters for 1,024 bits (Group 2)?


How long does it take to produce the parameters for 1536 bits (Group 5)?


How would we change the g value?







### B.2	
Let’s look at the Elliptic curves we can create:
```
openssl ecparam -list_curves
```

We can create our elliptic parameter file with:

```
openssl ecparam -name secp256k1 -out secp256k1.pem
```

Now view the details with:
```
openssl ecparam -in secp256k1.pem -text -param_enc explicit -noout
```

What are the details of the key?

Now we can create our key pair:
```
openssl ecparam -in secp256k1.pem -genkey -noout -out mykey.pem
```

Name three 160-bit curves:

By doing a search on the Internet, which curve does Bitcoin use?


Curve 2559 is a popular curve. Using Google, can you find some popular uses of Curve 25519?





Can you explain how you would use these EC parameters to perform the ECDH key exchange?







## C	Discrete Logarithms
### C.1	
ElGamal and Diffie Hellman use discrete logarithms. This involves a generator value (g) and a prime number. A basic operation is g<sup>x</sup> (mod p). If p=11, and g=2, determine the results (the first two have already been completed):

g=2, p=11

x | g<sup>x</sup> (mod p)
------------ | -------------
1|	2
2|	4
3|	
4|	
5|	
6|	
7|	
8|	
9|	
10|	
11|	
12|	

Note: In Python you can implement this as:

```python
g=2
p=11
x=3
print (g**x % p)
```


What happens to the values once we go past 10?



What happens to this sequence if we use g=3?






### C.2	
We can determine the values of g which will work for a given prime number with the following:
```python
import sys

p=11

def getG(p):

  for x in range (1,p):
	  rand = x
	  exp=1
	  next = rand % p

	  while (next != 1 ):
		  next = (next*rand) % p
		  exp = exp+1
	  if (exp==p-1):
	    print (rand)

print (getG(p))
```

Run the program and determine the possible g values for these prime numbers:

p=11:

p=41:

On the Internet, find a large prime number, and determine the values of g that are possible:







### C.3	
We can write a Python program to implement this key exchange. Enter and run the following program:
```python
import random
import hashlib
import sys

g=9
p=997

a=random.randint(5, 10)

b=random.randint(10,20)

A = (g**a) % p
B = (g**b) % p

print ('g: ',g,' (a shared value), n: ',p, ' (a prime number)')

print ('\nAlice calculates:')
print ('a (Alice random): ',a)
print ('Alice value (A): ',A,' (g^a) mod p')

print ('\nBob calculates:')
print ('b (Bob random): ',b)
print ('Bob value (B): ',B,' (g^b) mod p')

print ('\nAlice calculates:')
keyA=(B**a) % p
print ('Key: ',keyA,' (B^a) mod p')
print ('Key: ',hashlib.sha256(str(keyA).encode()).hexdigest())

print ('\nBob calculates:')
keyB=(A**b) % p
print ('Key: ',keyB,' (A^b) mod p')
print ('Key: ',hashlib.sha256(str(keyB).encode()).hexdigest())
```

Pick three different values for g and p, and make sure that the Diffie Hellman key exchange works.


g =        p=


g=        p=


g=       p=

Can you pick a value of g and p which will not work?




The following program sets up a man-in-the-middle attack for Eve:
```python
import random
import base64
import hashlib
import sys

g=15
p=1011

a= 5
b = 9
eve = 7

message=21

A=(g**a) % p

B=(g**b) % p

Eve1 = (A**eve) % p
Eve2 = (B**eve) % p

Key1= (Eve1**a) % p
Key2= (Eve2**b) % p

print ('g: ',g,' (a shared value), n: ',p, ' (a prime number)')

print ('\n== Random value generation ===')

print ('\nAlice calculates:')
print ('a (Alice random): ',a)
print ('Alice value (A): ',A,' (g^a) mod p')


print ('\nBob calculates:')
print ('b (Bob random): ',b)
print ('Bob value (B): ',B,' (g^b) mod p')

print ('\n==Alice sends value to Eve ===')

print ('Eve takes Alice\'s value and calculates: ',Eve1)
print ('Alice gets Eve\'s value and calculates key of: ',Key1)

print ('\n==Bob sends value to Eve ===')

print ('Eve takes Bob\'s value and calculates: ',Eve2)
print ('Bob gets Eve\'s value and calculates key of: ',Key2)
```

## D	Elliptic Curve Diffie-Hellman (ECDH)
ECDH is now one of the most used key exchange methods, and uses the Diffie Hellman method, but adds in elliptic curve methods. With this Alice generates (a) and Bob generates (b). We select a point on a curve (G), and Alice generates aG, and Bob generates bG. They pass the values to each other, and then Alice received bG, and Bob receives aG. Alice multiplies by a, to get abG, and Bob will multiply by b, and also get abG. This will be their shared key.

### D.1	
In the following we will implement ECDH using the secp256k1 curve (as used in Bitcoin). Confirm that Bob and Alice will have the same shared key.

Web link (ECDH):  [here](https://asecuritysite.com/hazmat/hashnew13)

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import binascii
import sys

Bob_private_key = ec.generate_private_key(ec.SECP256K1(),default_backend())
Alice_private_key = ec.generate_private_key(ec.SECP256K1(),default_backend())

Bob_shared_key = Bob_private_key.exchange(ec.ECDH(), Alice_private_key.public_key())

Bob_derived_key = HKDF(algorithm=hashes.SHA256(),length=size,salt=None,info=b'',backend=default_backend()).derive(Bob_shared_key)

Alice_shared_key = Alice_private_key.exchange(ec.ECDH(), Bob_private_key.public_key())

Alice_derived_key = HKDF(algorithm=hashes.SHA256(),length=size,salt=None,info=b'',backend=default_backend()).derive(Alice_shared_key)

print ("Name of curve: ",Bob_private_key.public_key().curve.name)
print (f"Generated key size: {size} bytes ({size*8} bits)")

vals = Bob_private_key.private_numbers()
print (f"\nBob private key value: {vals.private_value}")
vals=Bob_private_key.public_key()
enc_point=binascii.b2a_hex(vals.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
print("Bob's public key: ",enc_point)

vals = Alice_private_key.private_numbers()
print (f"\nAlice private key value: {vals.private_value}")
vals=Alice_private_key.public_key()
enc_point=binascii.b2a_hex(vals.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
print("Alice's public key: ",enc_point)


print ("\nBob's derived key: ",binascii.b2a_hex(Bob_derived_key).decode())
print("Alice's derived key: ",binascii.b2a_hex(Alice_derived_key).decode())())
```

Now modify the code to implement the SECP192R1 and also for the SECP521R1 curve. What do you notice about the sizes of the keys created between the different curve types?


### D.2
The code to implement Curve 25519 for key exchange (X25519) is:

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import binascii
import sys

Bob_private_key = X25519PrivateKey.generate()

Alice_private_key = X25519PrivateKey.generate()

size=32 # 256 bit key

Bob_shared_key = Bob_private_key.exchange(Alice_private_key.public_key())

Bob_derived_key = HKDF(algorithm=hashes.SHA256(),length=size,salt=None,info=b'',backend=default_backend()).derive(Bob_shared_key)

Alice_shared_key = Alice_private_key.exchange(Bob_private_key.public_key())

Alice_derived_key = HKDF(algorithm=hashes.SHA256(),length=size,salt=None,info=b'',backend=default_backend()).derive(Alice_shared_key)

print ("Name of curve: Curve 25519")

vals = binascii.b2a_hex(Bob_private_key.private_bytes(serialization.Encoding.Raw,serialization.PrivateFormat.Raw,serialization.NoEncryption()))
print (f"\nBob private key value: {vals}")
vals=Bob_private_key.public_key()
enc_point=binascii.b2a_hex(vals.public_bytes(encoding=serialization.Encoding.DER,format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
print("Bob's public key: ",enc_point)

vals = binascii.b2a_hex(Alice_private_key.private_bytes(serialization.Encoding.Raw,serialization.PrivateFormat.Raw,serialization.NoEncryption()))
print (f"\nAlice private key value: {vals}")
vals=Alice_private_key.public_key()
enc_point=binascii.b2a_hex(vals.public_bytes(encoding=serialization.Encoding.DER,format=serialization.PublicFormat.SubjectPublicKeyInfo)).decode()
print("Alice's public key: ",enc_point)


print ("\nBob's derived key: ",binascii.b2a_hex(Bob_derived_key).decode())
print("Alice's derived key: ",binascii.b2a_hex(Alice_derived_key).decode())
```
A sample of this is [here](https://asecuritysite.com/hazmat/hashnew29).


Do Bob and Alice end up with the same key?

In this case we have DER format for the public key. This normally starts with a "03". From the test run, copy the DER value and paste it [here](https://asecuritysite.com/encryption/sigs4). Can you view the public key point?

If you change the "DER" to "PEM" how does it change the viewing of the keys (remember to remove binascii.b2a_hex() method)?


## E	Simple Key Distribution Centre (KDC)
Rather than using key exchange, we can setup a KDC, and where Bob and Alice can have long-term keys. These can be used to generate a session key for them to use.  Enter the following Python program, and prove its operation:
```python
import hashlib
import sys
import binascii
import Padding
import random

from Crypto.Cipher import AES
from Crypto import Random

msg="test"

def encrypt(word,key, mode):
	plaintext=pad(word)
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	rtn = encobj.decrypt(ciphertext)
	return(rtn)

def pad(s):
	extra = len(s) % 16
	if extra > 0:
    		s = s + (' ' * (16 - extra))
	return s


rnd = random.randint(1,2**128)

keyA= hashlib.md5(str(rnd).encode()).digest()

rnd = random.randint(1,2**128)

keyB= hashlib.md5(str(rnd).encode()).digest()
 
print('Long-term Key Alice=',binascii.hexlify(keyA))
print('Long-term Key Bob=',binascii.hexlify(keyB))

rnd = random.randint(1,2**128)
keySession= hashlib.md5(str(rnd).encode()).hexdigest()

ya = encrypt(keySession.encode(),keyA,AES.MODE_ECB)
yb = encrypt(keySession.encode(),keyB,AES.MODE_ECB)

print("Encrypted key sent to Alice:",binascii.hexlify(ya))
print("Encrypted key sent to Bob:",binascii.hexlify(yb))

decipherA = decrypt(ya,keyA,AES.MODE_ECB)
decipherB = decrypt(yb,keyB,AES.MODE_ECB)

print("Session key:",decipherA)
print("Session key:",decipherB)
```
 
Web link (Simple KDC): https://asecuritysite.com/encryption/kdc01
   
The program above uses a shared 128-bit session key (generated by MD5). Now change the program so that you generate a 256-bit session key. What are the changes made:










## F	Challenge
### F.1	
Bob and Alice agree on a g value of 5, and a prime number of 97. They then use the Diffie-Hellman key exchange method. Alice passes a value of 32, and Bob passes a value of 41. Can you determine the secret value that Bob and Alice have generated, and the resultant key value? Outline the code here:








What happens if we use a g value of 2? Why is there a problem?






Can you now write a generate DH key cracker for any value of g, p, A (passed by Alice), and B (passed by Bob) Outline code and run to evaluate the perform of our code with different ranges of the prime number (p):
 









## G	What I should have learnt from this lab?
The key things learnt:

* The basics of the Diffie Hellman method.
* The basic method used with ECDH.



