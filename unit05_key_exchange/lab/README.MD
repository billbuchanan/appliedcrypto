![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

## Lab 5: Key Exchange
Objective: Key exchange allows us to pass a shared secret key between Bob and Alice. The main methods for doing this are either encrypting with the public key, the Diffie Hellman Method and the Elliptic Curve Diffie Hellman (ECDH) method. This lab investigates these methods.

Web link (Demo): https://youtu.be/Lnw4FhiOwiU

## A	Diffie-Hellman
No	Description	Result
### A.1	
Bob and Alice have agreed on the values:

g=2879, N= 9929

Bob Select x=6, Alice selects y=9

Now calculate (using a calculator):

Bob’s A value (g<sup>x</sup> mod N):	
	
Alice’s B value (g<sup>y</sup> mod N):

### A.2	
Now they exchange the values. Next calculate the shared key:


Bob’s value (B<sup>x</sup> mod N):	
	
Alice’s value (A<sup>y</sup> mod N):

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
openssl dhparam -out dhparams.pem 768 -text
```

View your key with:

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
<pre>
openssl ecparam -list_curves
</pre>

We can create our elliptic parameter file with:

<pre>
openssl ecparam -name secp256k1 -out secp256k1.pem
</pre>

Now view the details with:
<pre>
openssl ecparam -in secp256k1.pem -text -param_enc explicit -noout
</pre>

What are the details of the key?

Now we can create our key pair:
<pre>
openssl ecparam -in secp256k1.pem -genkey -noout -out mykey.pem
</pre>

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
Copy and paste the code from (you may have to run “pip install eccsnacks”):

Web link (ECDH):  https://asecuritysite.com/encryption/curve

and confirm that Bob and Alice will always get the same shared key.
```python
import os
import binascii
from x25519 import base_point_mult,multscalar,bytes_to_int,int_to_bytes


a = os.urandom(32)
b = os.urandom(32)
# a = int_to_bytes(10,32) # just for testing a=10 (32 bytes - 256 bits)
# b = int_to_bytes(12,32) # just for testing b=12 (32 bytes - 256 bits)

print (f"\n\nBob private (b):\t{bytes_to_int(b)}")
print (f"Alice private (a): \t{bytes_to_int(a)}")



# Traditional ECDH: 
a_pub = base_point_mult(a)
b_pub = base_point_mult(b)

print ("\n\nBob public (bG):\t",binascii.hexlify(b_pub.encode()))

print ("Alice public (aG):\t",binascii.hexlify(a_pub.encode()))

k_a = multscalar(a, b_pub) # a (bG)
k_b = multscalar(b, a_pub) # b (aG)


print ("\n\nBob shared (b)aG:\t",binascii.hexlify(k_b.encode()))
print ("Alice shared (a)bG:\t",binascii.hexlify(k_a.encode()))
```
The code to implement Curve 25519 for key exchange (X25519) is:

```python
P = 2 ** 255 - 19
A24 = 121665
def bytes_to_int(bytes):

    result = 0
    
    for b in bytes:
        result = result * 256 + int(b)
    
    return result


def int_to_bytes(value, length):
    result = []
    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)
    
    return result

def cswap(swap, x_2, x_3):
    dummy = swap * ((x_2 - x_3) % P)
    x_2 = x_2 - dummy
    x_2 %= P
    x_3 = x_3 + dummy
    x_3 %= P
    return (x_2, x_3)

# Based on https://tools.ietf.org/html/rfc7748
def X25519(k, u):
    x_1 = u
    x_2 = 1
    z_2 = 0
    x_3 = u
    z_3 = 1
    swap = 0

    for t in reversed(range(255)):
        k_t = (k >> t) & 1
        swap ^= k_t
        x_2, x_3 = cswap(swap, x_2, x_3)
        z_2, z_3 = cswap(swap, z_2, z_3)
        swap = k_t

        A = x_2 + z_2
        A %= P

        AA = A * A
        AA %= P

        B = x_2 - z_2
        B %= P

        BB = B * B
        BB %= P

        E = AA - BB
        E %= P

        C = x_3 + z_3
        C %= P

        D = x_3 - z_3
        D %= P

        DA = D * A
        DA %= P

        CB = C * B
        CB %= P

        x_3 = ((DA + CB) % P)**2
        x_3 %= P

        z_3 = x_1 * (((DA - CB) % P)**2) % P
        z_3 %= P

        x_2 = AA * BB
        x_2 %= P

        z_2 = E * ((AA + (A24 * E) % P) % P)
        z_2 %= P

    x_2, x_3 = cswap(swap, x_2, x_3)
    z_2, z_3 = cswap(swap, z_2, z_3)

    return (x_2 * pow(z_2, P - 2, P)) % P

def decodeScalar25519(k):
  k_list = [(b) for b in k]
  k_list[0] &= 248
  k_list[31] &= 127
  k_list[31] |= 64
  return decodeLittleEndian(k_list)

def decodeLittleEndian(b):
    return sum([b[i] << 8*i for i in range( 32 )])

def unpack2(s):
    if len(s) != 32:
        raise ValueError('Invalid Curve25519 scalar (len=%d)' % len(s))
    t = sum((ord(s[i]) ) << (8 * i) for i in range(31))
    t += (((ord(s[31]) ) & 0x7f) << 248)
    return t    

def pack(n):
    return ''.join([chr((n >> (8 * i)) & 255) for i in range(32)])

def clamp(n):
    n &= ~7
    n &= ~(128 << 8 * 31)
    n |= 64 << 8 * 31
    return n

# Return nP
def multscalar(n, p):
    n = clamp(decodeScalar25519(n))
    p = unpack2(p)
    return pack(X25519(n, p))

# Start at x=9. Find point n times x-point
def base_point_mult(n):
    n = clamp(decodeScalar25519(n))
    return pack(X25519(n, 9))
```
A sample of this is [here](https://repl.it/@billbuchanan/simpleecdh).


Do Bob and Alice end up with the same key?


How large are the random numbers that Bob and Alice generate? 



Do you think that this program will be secure? How might Eve discover the shared secret? 



Estimate the time it would take her to discover the key if she can try one billion keys per second:



How would you modify that program so that it was more secure?

### D.2
We used Curve 25519 in D.1. Can you modify the code so that it uses secp256k1? The code for secp256k1 is defined in the secp256k1.py file [here](https://asecuritysite.com/encryption/python_secp256k1ecdh2). 

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

•	The basics of the Diffie Hellman method.
•	The basic method used with ECDH.



