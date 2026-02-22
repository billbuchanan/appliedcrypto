![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

Either complete Part 1 first and then do Part 2, or start with Part 1 and then do Part 2.

# Part 1 (Lab 4: Asymmetric (Public) Key)
Objective: The key objective of this lab is to provide a practical introduction to public key encryption, and with a focus on RSA and Elliptic Curve methods. This includes the creation of key pairs and in the signing process.

Video demo: [here](https://youtu.be/6T9bFA2nl3c )

Note: If you are using Python 3, instead of "pip install pycrypto" you can install pycryptodome with "pip3 install pycryptodome".

## A	RSA Encryption
### A.1	

With public key encryption, we can use the public key to either encrypt data, or it can be used to prove a digital signature. The following is a public key generated with the GPG program:
```
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
n+wpRYh/3mkaDswQf93n
=zhEX
-----END PGP PUBLIC KEY BLOCK-----
```

Using the following Web page, determine the owner of the key, and the ID on the key:

[https://asecuritysite.com/encryption/pgp1](https://asecuritysite.com/pgp/pgp1)


By searching on-line, what is an ASCII Armored Message?


### A.2	
Bob has a private RSA key of:
```
-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDoIhiWs15X/6xiLAVcBzpgvnuvMzHBJk58wOWrdfyEAcTY10oG\n+6auNFGqQHYHbfKaZlEi4prAoe01S/R6jpx8ZqJUN0WKNn5G9nmjJha9Pag28ftD\nrsT+4LktaQrxdNdrusP+qI0NiYbNBH6qvCrK0aGiucextehnuoqgDcqmRwIDAQAB\nAoGAZCaJu0MJ2ieJxRU+/rRzoFeuXylUNwQC6toCfNY7quxkdDV2T8r038Xc0fpb\nsdrix3CLYuSnZaK3B76MbO/oXQVBjDQZ7jVQ5K41nVCEZOtRDBeX5Ue6CBs4iNmC\n+QyWx+u4OZPURq61YG7D+F1aWRvczdEZgKHPXl/+s5pIvAkCQQDw4V6px/+DJuZV\n5Eg20OZe0m9Lvaq+G9UX2xTA2AUuH8Z79e+SCus6fMVl+Sf/W3y3uXp8B662bXhz\nyheH67aDAkEA9rQrvmFj65n/D6eH4JAT4OP/+icQNgLYDW+u1Y+MdmD6A0YjehW3\nsuT9JH0rvEBET959kP0xCx+iFEjl81tl7QJBAMcp4GZK2eXrxOjhnh/Mq51dKu6Z\n/NHBG3jlCIzGT8oqNaeK2jGLW6D5RxGgZ8TINR+HeVGR3JAzhTNftgMJDtcCQQC3\nIqReXVmZaeXnrwu07f9zsI0zG5BzJ8VOpBt7OWah8fdmOsjXNgv55vbsAWdYBbUw\nPQ+lc+7WPRNKT5sz/iM5AkEAi9Is+fgNy4q68nxPl1rBQUV3Bg3S7k7oCJ4+ju4W\nNXCCvRjQhpNVhlor7y4FC2p3thje9xox6QiwNr/5siyccw==\n-----END RSA PRIVATE KEY-----
```

And receives a ciphertext message of:

```
uW6FQth0pKaWc3haoqxbjIA7q2rF+G0Kx3z9ZDPZGU3NmBfzpD9ByU1ZBtbgKC8ATVZzwj15AeteOnbjO3EHQC4A5Nu0xKTWpqpngYRGGmzMGtblW3wBlNQYovDsRUGt+cJK7RD0PKn6PMNqK5EQKCD6394K/gasQ9zA6fKn3f0=
```

Use the following code:

```python
# https://asecuritysite.com/rsa/rsa_example
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

binPrivKey = "-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDoIhiWs15X/6xiLAVcBzpgvnuvMzHBJk58wOWrdfyEAcTY10oG\n+6auNFGqQHYHbfKaZlEi4prAoe01S/R6jpx8ZqJUN0WKNn5G9nmjJha9Pag28ftD\nrsT+4LktaQrxdNdrusP+qI0NiYbNBH6qvCrK0aGiucextehnuoqgDcqmRwIDAQAB\nAoGAZCaJu0MJ2ieJxRU+/rRzoFeuXylUNwQC6toCfNY7quxkdDV2T8r038Xc0fpb\nsdrix3CLYuSnZaK3B76MbO/oXQVBjDQZ7jVQ5K41nVCEZOtRDBeX5Ue6CBs4iNmC\n+QyWx+u4OZPURq61YG7D+F1aWRvczdEZgKHPXl/+s5pIvAkCQQDw4V6px/+DJuZV\n5Eg20OZe0m9Lvaq+G9UX2xTA2AUuH8Z79e+SCus6fMVl+Sf/W3y3uXp8B662bXhz\nyheH67aDAkEA9rQrvmFj65n/D6eH4JAT4OP/+icQNgLYDW+u1Y+MdmD6A0YjehW3\nsuT9JH0rvEBET959kP0xCx+iFEjl81tl7QJBAMcp4GZK2eXrxOjhnh/Mq51dKu6Z\n/NHBG3jlCIzGT8oqNaeK2jGLW6D5RxGgZ8TINR+HeVGR3JAzhTNftgMJDtcCQQC3\nIqReXVmZaeXnrwu07f9zsI0zG5BzJ8VOpBt7OWah8fdmOsjXNgv55vbsAWdYBbUw\nPQ+lc+7WPRNKT5sz/iM5AkEAi9Is+fgNy4q68nxPl1rBQUV3Bg3S7k7oCJ4+ju4W\nNXCCvRjQhpNVhlor7y4FC2p3thje9xox6QiwNr/5siyccw==\n-----END RSA PRIVATE KEY-----"

ciphertext=base64.b64decode("uW6FQth0pKaWc3haoqxbjIA7q2rF+G0Kx3z9ZDPZGU3NmBfzpD9ByU1ZBtbgKC8ATVZzwj15AeteOnbjO3EHQC4A5Nu0xKTWpqpngYRGGmzMGtblW3wBlNQYovDsRUGt+cJK7RD0PKn6PMNqK5EQKCD6394K/gasQ9zA6fKn3f0=")

privKeyObj = RSA.importKey(binPrivKey)
cipher = PKCS1_OAEP.new(privKeyObj)
message = cipher.decrypt(ciphertext)

print ("====Decrypted===")
print ("Message:",message)
```


What is the plaintext message that Bob has been sent?






## B	OpenSSL (RSA)
We will use OpenSSL to perform the following:

### B.1	

First we need to generate a key pair with:

```
openssl genrsa -out private.pem 1024	
```

This file contains both the public and the private key.


 


What is the type of public key method used:


How long is the default key:


How long did it take to generate a 1,024 bit key?


Use the following command to view the keys:

```
 cat private.pem 
```

### B.2	
Use following command to view the output file:

```
cat private.pem
```

What can be observed at the start and end of the file:


### B.3	
Next we view the RSA key pair:
```
openssl rsa -in private.pem -text 
```

Which are the attributes of the key shown:



How many bits does the RSA modulus have, and how many bits are used for the two prime numbers. What is the value of e?





### B.4	
Let’s now secure the encrypted key with 128-bit AES (and based on a key generated from a passphrase):
```
openssl rsa -in private.pem -aes128 -out keyaes.pem 
```
	

 
Why should you have a password on the usage of your private key?

### B.5 	
Next we will export the public key:

```
openssl rsa -in private.pem -out public.pem -outform PEM -pubout 
```

View the output key. What does the header and footer of the file identify?



### B.6	

Now create a file named “myfile.txt” and put a message into it. Next encrypt it with your public key:


```
openssl pkeyutl -encrypt -inkey public.pem -pubin -in myfile.txt -out file.bin	
```


### B.7	
And then decrypt with your private key:

```
openssl pkeyutl -decrypt -inkey private.pem -in file.bin -out decrypted.txt
```

What are the contents of decrypted.txt?

### B.8
What can you observe between these two commands for differing output formats:

```
openssl pkeyutl -encrypt -inkey public.pem -pubin -in myfile.txt -out file.bin

cat file.bin
```
and:
```
openssl pkeyutl -encrypt -inkey public.pem -pubin -in myfile.txt -out file.bin -hexdump

cat file.bin
```




## C	OpenSSL (ECC)
Elliptic Curve Cryptography (ECC) is now used extensively within public key signing and key exchange. This includes  with Bitcoin, Ethereum, Tor, and  IoT applications. In this part of the lab we will use OpenSSL to create an EC key pair. For this we generate a random 256-bit private key (priv), and then generate a public key point (which is priv multiplied by G). This will use a generator point (G), and which is an (x,y) point on the selected elliptic curve.


### C.1	
First we need to generate a private key with:
```
openssl ecparam -name secp256k1 -genkey -out priv.pem	
```

The file will only contain the private key (and should have 256 bits).

Now use “cat priv.pem” to view your key. 

Can you view your key?

### C.2	
We can view the details of the ECC parameters used with:
```
openssl ecparam -in priv.pem -text -param_enc explicit -noout
```

Outline these values:

Prime (last two bytes):

A:

B:

Generator (last two bytes):

Order (last two bytes):

### C.3	
Now generate your public key based on your private key with:
```
openssl ec -in priv.pem -text -noout
```

How many bits and bytes does your private key have:



How many bit and bytes does your public key have (Note the 04 is not part of the elliptic curve point):



What is the ECC method that you have used?



### C.4	
First we need to generate a private key with:

```
openssl ecparam -list_curves 
```

Outline three curves supported:

### C.5	

Let’s select two other curves:
```
openssl ecparam -name secp128r1 -genkey -out priv.pem
openssl ecparam -in priv.pem -text -param_enc explicit -noout
```

and:

```
openssl ecparam -name secp521r1 -genkey -out priv.pem
openssl ecparam -in priv.pem -text -param_enc explicit -noout
```

How does secp128k1, secp256k1 and secp512r1 different in the parameters used? Perhaps identify the length of the prime number used, and the size of the base point (G).

If you want to see an example of ECC, try [here](https://asecuritysite.com/encryption/ecc) 

## D	Elliptic Curve Encryption



### D.2 	
Let’s say we create an elliptic curve with y<sup>2</sup> = x<sup>3</sup> + 7, and with a prime number of 89, generate the first five (x,y) points for the finite field elliptic curve. You can use the Python code at the following to generate them:

https://asecuritysite.com/encryption/ecc_points

First five points:



<!--
### D.3	
Elliptic curve methods are often used to sign messages, and where Bob will sign a message with his private key, and where Alice can prove that he has signed it by using his public key. With ECC, we can use ECDSA, and which was used in the first version of Bitcoin. Enter the following code:

```python
from ecdsa import SigningKey,NIST192p,NIST224p,NIST256p,NIST384p,NIST521p,SECP256k1
import base64
import sys

msg="Hello"
type = 1
cur=NIST192p


sk = SigningKey.generate(curve=cur) 

vk = sk.get_verifying_key()

signature = sk.sign(msg.encode())

print ("Message:\t",msg)
print ("Type:\t\t",cur.name)
print ("=========================")

print ("Signature:\t",base64.b64encode(signature))

print ("=========================")

print ("Signatures match:\t",vk.verify(signature, msg.encode()))
```

What are the signatures (you only need to note the first four characters) for a message of “Bob”, for the curves of NIST192p, NIST521p and SECP256k1:

NIST192p:

NIST521p:

SECP256k1:


By searching on the Internet, can you find in which application areas that SECP256k1 is used?


What do you observe from the different hash signatures from the elliptic curve methods?

-->


## E	RSA
### E.1 
A simple RSA program to encrypt and decrypt with RSA is given next. Prove its operation:

```python
import rsa
(bob_pub, bob_priv) = rsa.newkeys(512)

msg='Here is my message'
ciphertext = rsa.encrypt(msg.encode(), bob_pub)
message = rsa.decrypt(ciphertext, bob_priv)
print(message.decode('utf8'))
```

Now add the lines following lines after the creation of the keys:

```python
print (bob_pub)
print (bob_priv)
```


Can you identify what each of the elements of the public key (e,N), the private key (d,N), and the two prime number (p and q) are (if the numbers are long, just add the first few numbers of the value):




When you identity the two prime numbers (p and q), with Python, can you prove that when they are multiplied together they result in the modulus value (N):

Proven Yes/No


#### Note
You may find that the rsa library may not run on some systems, so the following is an equivalent:

```
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import sys

size=512
M=5

if (len(sys.argv)>1):
	size=int(sys.argv[1])
if (len(sys.argv)>2):
	M=int(sys.argv[2])

try:
	print(f"RSA key size: {size}\nM={M}\n")

	private_key = rsa.generate_private_key(public_exponent=65537,key_size=size)

	priv= private_key.private_numbers()
	p=priv.p
	q=priv.q 
	d=priv.d
	n=p*q
	print("=== RSA Private key ===")
	print (f"p={p} q={q} d={d} N={n}")
	print (f"\nBit length of p and q is {p.bit_length()}")
	print (f"Bit length of N is {n.bit_length()}")

	print("\n=== RSA Public key ===")
	pub = private_key.public_key()
	e=pub.public_numbers().e
	n=pub.public_numbers().n
	print (f"\nN={n} e={e}")



	C = pow(M,e,n)
	Plain = pow(C,d,n)
	print (f"\nMessage={M}")
	print (f"Cipher={C}")
	print (f"Decrypt={Plain}")



	print("\n=== Private Key PEM format ===")
	pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())
	print ("Private key: ",pem.decode())


	pem = pub.public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)

	print("\n=== Public Key PEM format ===")
	print ("Public key: ",pem.decode())

except Exception as e:
    print(e)
```

### E.2	
We will follow a basic RSA process. If you are struggling here, have a look at the following page:

https://asecuritysite.com/encryption/rsa

First, pick two prime numbers:

p=

q=

Now calculate N (p.q) and PHI [(p-1).(q-1)]:

N=

PHI = 

Now pick a value of e which does not share a factor with PHI [gcd(PHI,e)=1]:

e=

Now select a value of d, so that (e.d) (mod PHI) = 1:

[Note: You can use this page to find d: https://asecuritysite.com/encryption/inversemod]

d=

Now for a message of M=5, calculate the cipher as:

C = M<sup>e</sup> (mod N) = 

Now decrypt your ciphertext with:

M = C<sup>d</sup> (mod N) =

Did you get the value of your message back (M=5)? If not, you have made a mistake, so go back and check.

Now run the following code and prove that the decrypted cipher is the same as the message: 

```python
import libnum

p=11
q=3
N=p*q
PHI=(p-1)*(q-1)
e=3

d= libnum.invmod(e,PHI)

print (e,N)
print (d,N)
M=4
print ("\nMessage:",M)
cipher = M**e % N
print ("Cipher:",cipher)
message = cipher**d % N
print ("Message:",message)
```


Select three more examples with different values of p and q, and then select e in order to make sure that the cipher will work:




### E.2	
In the RSA method, we have a value of e, and then determine d from (d.e) (mod PHI)=1. But how do we use code to determine d? Well we can use the Euclidean algorithm. The code for this is given at:

https://asecuritysite.com/encryption/inversemod

Using the code, can you determine the following:

```
Inverse of 53 (mod 120) = 
Inverse of 65537 (mod 1034776851837418226012406113933120080) = 
```

Using this code, can you now create an RSA program where the user enters the values of p, q, and e, and the program determines (e,N) and (d,N)?


### E.3	
Run the following code and observe the output of the keys. If you now change the key generation key from ‘PEM’ to ‘DER’, how does the output change:





```python
from Crypto.PublicKey import RSA

key = RSA.generate(2048)

binPrivKey = key.exportKey('PEM')
binPubKey =  key.publickey().exportKey('PEM')

print (binPrivKey)
print (binPubKey)
```


### E.4	
A simple RSA program to encrypt and decrypt with RSA is given next. Prove its operation:
```python
import rsa
(bob_pub, bob_priv) = rsa.newkeys(512)
ciphertext = rsa.encrypt('Here is my message'.encode(), bob_pub)
message = rsa.decrypt(ciphertext, bob_priv)
print(message.decode('utf8'))
```
A sample [here](https://repl.it/@billbuchanan/rsanew01#main.py)

## F	PGP
### F.1	
The following is a PGP key pair. Using https://asecuritysite.com/encryption/pgp, can you determine the owner of the keys:
```
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: OpenPGP.js v4.4.5
Comment: https://openpgpjs.org

xk0EXEOYvQECAIpLP8wfLxzgcolMpwgzcUzTlH0icggOIyuQKsHM4XNPugzU
X0NeaawrJhfi+f8hDRojJ5Fv8jBI0m/KwFMNTT8AEQEAAc0UYmlsbCA8Ymls
bEBob21lLmNvbT7CdQQQAQgAHwUCXEOYvQYLCQcIAwIEFQgKAgMWAgECGQEC
GwMCHgEACgkQoNsXEDYt2ZjkTAH/b6+pDfQLi6zg/Y0tHS5PPRv1323cwoay
vMcPjnWq+VfiNyXzY+UJKR1PXskzDvHMLOyVpUcjle5ChyT5LOw/ZM5NBFxD
mL0BAgDYlTsT06vVQxu3jmfLzKMAr4kLqqIuFFRCapRuHYLOjw1gJZS9p0bF
S0qS8zMEGpN9QZxkG8YEcH3gHxlrvALtABEBAAHCXwQYAQgACQUCXEOYvQIb
DAAKCRCg2xcQNi3ZmMAGAf9w/XazfELDG1W35l2zw12rKwM7rK97aFrtxz5W
XwA/5gqoVP0iQxklb9qpX7RVd6rLKu7zoX7F+sQod1sCWrMw
=cXT5
-----END PGP PUBLIC KEY BLOCK-----

-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: OpenPGP.js v4.4.5
Comment: https://openpgpjs.org

xcBmBFxDmL0BAgCKSz/MHy8c4HKJTKcIM3FM05R9InIIDiMrkCrBzOFzT7oM
1F9DXmmsKyYX4vn/IQ0aIyeRb/IwSNJvysBTDU0/ABEBAAH+CQMIBNTT/OPv
TJzgvF+fLOsLsNYP64QfNHav5O744y0MLV/EZT3gsBwO9v4XF2SsZj6+EHbk
O9gWi31BAIDgSaDsJYf7xPOhp8iEWWwrUkC+jlGpdTsGDJpeYMIsVVv8Ycam
0g7MSRsL+dYQauIgtVb3dloLMPtuL59nVAYuIgD8HXyaH2vsEgSZSQn0kfvF
+dWeqJxwFM/uX5PVKcuYsroJFBEO1zas4ERfxbbwnsQgNHpjdIpueHx6/4EO
b1kmhOd6UT7BamubY7bcma1PBSv8PH31Jt8SzRRiaWxsIDxiaWxsQGhvbWUu
Y29tPsJ1BBABCAAfBQJcQ5i9BgsJBwgDAgQVCAoCAxYCAQIZAQIbAwIeAQAK
CRCg2xcQNi3ZmORMAf9vr6kN9AuLrOD9jS0dLk89G/XfbdzChrK8xw+Odar5
V+I3JfNj5QkpHU9eyTMO8cws7JWlRyOV7kKHJPks7D9kx8BmBFxDmL0BAgDY
lTsT06vVQxu3jmfLzKMAr4kLqqIuFFRCapRuHYLOjw1gJZS9p0bFS0qS8zME
GpN9QZxkG8YEcH3gHxlrvALtABEBAAH+CQMI2Gyk+BqVOgzgZX3C80JRLBRM
T4sLCHOUGlwaspe+qatOVjeEuxA5DuSs0bVMrw7mJYQZLtjNkFAT92lSwfxY
gavS/bILlw3QGA0CT5mqijKr0nurKkekKBDSGjkjVbIoPLMYHfepPOju1322
Nw4V3JQO4LBh/sdgGbRnwW3LhHEK4Qe70cuiert8C+S5xfG+T5RWADi5HR8u
UTyH8x1h0ZrOF7K0Wq4UcNvrUm6c35H6lClC4Zaar4JSN8fZPqVKLlHTVcL9
lpDzXxqxKjS05KXXZBh5wl8EGAEIAAkFAlxDmL0CGwwACgkQoNsXEDYt2ZjA
BgH/cP12s3xCwxtVt+Zds8NdqysDO6yve2ha7cc+Vl8AP+YKqFT9IkMZJW/a
qV+0VXeqyyru86F+xfrEKHdbAlqzMA==
=5NaF
-----END PGP PRIVATE KEY BLOCK-----
```

### F.2	
Using the code at the following link, generate a key:
https://asecuritysite.com/encryption/openpgp

### F.3	
An important element in data loss prevention is encrypted emails. In this part of the lab we will use an open source standard: PGP.  


#### 1. Create a key pair with (RSA and 2,048-bit keys):

```
> gpg --gen-key
gpg (GnuPG) 1.4.23; Copyright (C) 2015 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

gpg: keyring `C:/Users/Administrator/AppData/Roaming/gnupg\secring.gpg' created
gpg: keyring `C:/Users/Administrator/AppData/Roaming/gnupg\pubring.gpg' created
Please select what kind of key you want:
   (1) RSA and RSA (default)
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (2048)
Requested keysize is 2048 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0)
Key does not expire at all
Is this correct? (y/N) y

You need a user ID to identify your key; the software constructs the user ID
from the Real Name, Comment and Email Address in this form:
    "Heinrich Heine (Der Dichter) <heinrichh@duesseldorf.de>"

Real name: Bill Buchanan
Email address: w.buchanan@napier.ac.uk
Comment: My Key
You selected this USER-ID:
    "Bill Buchanan (My Key) <w.buchanan@napier.ac.uk>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
You need a Passphrase to protect your secret key.

We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
..+++++
.......+++++
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
+++++
+++++
gpg: C:/Users/Administrator/AppData/Roaming/gnupg\trustdb.gpg: trustdb created
gpg: key E343DC3A marked as ultimately trusted
public and secret key created and signed.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   1  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 1u
pub   2048R/E343DC3A 2023-02-12
      Key fingerprint = 745F 2F35 1244 943C 5997  5AF5 5F00 436C E343 DC3A
uid                  Bill Buchanan (My Key) <w.buchanan@napier.ac.uk>
```

Now export your public key using the form of:
```
gpg --export -a "Your name" > mypub.key
```
Now export your private key using the form of:
```
gpg --export-secret-key -a "Your name" > mypriv.key
```

How is the randomness generated?



Outline the contents of your key file:

#### 2. Now send your lab partner your public key in the contents of an email, and ask them to import it onto their key ring (if you are doing this on your own, create another set of keys to simulate another user, or use Bill’s public key – which is defined at http://asecuritysite.com/public.txt and send the email to him):
```
gpg --import theirpublickey.key
```

Now list your keys with:
```
gpg --list-keys
```

Which keys are stored on your key ring and what details do they have:




#### 3. Create a text file, and save it. Next encrypt the file with their public key:
```
gpg -e -a -u "Your Name" -r "Your Lab Partner Name" hello.txt
```

What does the –a option do:


What does the –r option do:


What does the –u option do:


Which file does it produce and outline the format of its contents:


#### 4. Send your encrypted file in an email to your lab partner, and get one back from them.

Now create a file (such as myfile.asc) and decrypt the email using the public key received from them with:
```
gpg –d myfile.asc > myfile.txt
```

Can you decrypt the message:

#### 5. Next, using this public key file, send Bill (w.buchanan@napier.ac.uk) a question (http://asecuritysite.com/public.txt):

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

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
n+wpRYh/3mkaDswQf93n
=zhEX
-----END PGP PUBLIC KEY BLOCK-----
```


Did you receive a reply:

#### 6. Next send your public key to Bill (w.buchanan@napier.ac.uk), and ask for an encrypted message from him.
	



## G GitHub Keys

### G.1
On your VM, go into the ~/.ssh folder. Now generate your SSH keys:

```
ssh-keygen -t rsa -C "your email address"
```

The public key should look like this:

```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLrriuNYTyWuC1IW7H6yea3hMV+rm029m2f6IddtlImHrOXjNwYyt4Elkkc7AzOy899C3gpx0kJK45k/CLbPnrHvkLvtQ0AbzWEQpOKxI+tW06PcqJNmTB8ITRLqIFQ++ZanjHWMw2Odew/514y1dQ8dccCOuzeGhL2Lq9dtfhSxx+1cBLcyoSh/lQcs1HpXtpwU8JMxWJl409RQOVn3gOusp/P/0R8mz/RWkmsFsyDRLgQK+xtQxbpbodpnz5lIOPWn5LnT0si7eHmL3WikTyg+QLZ3D3m44NCeNb+bOJbfaQ2ZB+lv8C3OxylxSp2sxzPZMbrZWqGSLPjgDiFIBL w.buchanan@napier.ac.uk
```

View the private key. What is the DEK-Info part, and how would it be used to protect the key, and what information does it contain?


On your Ubuntu instance setup your new keys for ssh:

```
ssh-add ~/.ssh/id_git
```

Now create a GitHub account and upload your public key to Github (select Settings-> New SSH key or Add SSH key).  Create a new repository on your GitHub site, and add a new file to it. Next go to your Ubuntu instance and see if you can clone of a new directory:

git clone ssh://git@github.com/<user>/<repository name>.git

If this doesn’t work, try the https connection that is defined on GitHub.




## H	What I should have learnt from this lab?
The key things learnt:

* The basics of the RSA method.
* The process of generating RSA and Elliptic Curve key pairs.
* To illustrate how the private key is used to sign data, and then using the public key to verify the signature.

A reflective statement:

* In ECC, we use a 256-bit private key. This is used to generate the key for signing Bitcoin transactions. Do you think that a 256-bit key is largest enough? If we use a cracker that performs 1 Tera keys per second, will someone be able to determine our private key?

## Additional
The following is code which performs RSA key generation, and the encryption and decryption of a message (https://asecuritysite.com/encryption/rsa_example):

```python
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64encode
from Crypto.Cipher import PKCS1_OAEP
import sys

msg = "hello..."

if (len(sys.argv)>1):
        msg=str(sys.argv[1])

key = RSA.generate(1024)

binPrivKey = key.exportKey('PEM')
binPubKey =  key.publickey().exportKey('PEM')

print
print ("====Private key===")
print (binPrivKey)
print
print ("====Public key===")
print (binPubKey)

privKeyObj = RSA.importKey(binPrivKey)
pubKeyObj =  RSA.importKey(binPubKey)


cipher = PKCS1_OAEP.new(pubKeyObj)
ciphertext = cipher.encrypt(msg.encode())

print
print ("====Ciphertext===")
print (b64encode(ciphertext))

cipher = PKCS1_OAEP.new(privKeyObj)
message = cipher.decrypt(ciphertext)


print
print ("====Decrypted===")
print ("Message:",message)
```

The code is [here](https://repl.it/@billbuchanan/rsanewcode#main.py). Can you decrypt this:

```
fIVuuWFLVANs9MjatXbIbtH7/n0dBpDirXKi82jZovXS/krxy43cP0J9jlNz4dqxLgdiqtRe1AcymX06JUo1SrcqDEh3lQxoU1KUvV7jG9GE3pSxHq4dQlcWdHz95b9go6QYbe/5S/uJgolR+S9qaDE8tXYysP8FeXIPd0dXxHo=
```

The private key is:

```
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQCfQfirYVXgzT90v6SqgeID7q/WK1XaVTNGVFolDUOcrXl/egRG
4iag5tiTbrMYCQ8CSTYn7q0U4AmBXihlbWDqf6MMk6OEoDxdWZTiG1MmQ1wZikFE
s7sYSog/poYleCeYW8kVzHNWnt9IuQWekIg6ZHkwp4NE/aW8HxvEwYRqCQIDAQAB
AoGAE6rkiFmxbt06GHNwZQQ8QssP2Q2qARgjiGxzY38DWg6MYiNR8uUL6zQHDBIQ
OQgpW9lpwD24D0tpsRnNOFVtMeafcxmykX+qHGtNeKJuTtqSm2eTI6gNbC8iosGT
XJEPM8tc/dfZ2sDobLfi0alWFOzWo8vKaLnnAdMHoZ8mDo8CQQDCMx08JVlTW1zl
+4UTEnyyYmIezw5ORfMqPtN1LpQ4ptYnHNMVJPWcpRwBYZfHlPOPtuVwo6gzv82G
QpgQsd4PAkEA0fA8e8R6JbeUR1HxsqWeCnPz3Ahq5Ya5WA6HyJQml9aDVqKDDp2L
3AcqsvFEKJ/T34r31so2yW6hj2yFBnzOZwJBAIqanrgJ1CpJYBGJJd6J6FQNIgjp
MUWuaTJyqsvNFd8lPF2oFgPWYDKQKV/W/tRkvD2LhVCSjf95WsADkbMAsAMCQAHo
wWQOwV2eccbERAJv5yQJMeqKWQ6FTyIx36I/VqqC1Obwy2hSnnb9ybGe6BPGgFLE
HMTjSeRDEU0Qm5UXhXkCQQCPlZJqlgksBN/TULHC4RgsXIx+oFylBrkiFamYsuEt
Kn52h41pX7FI5TXcqIDPw+uqAu50JnwDR0dLYY6fvIce
-----END RSA PRIVATE KEY-----
```

# Part 2: AWS Lab for RSA Encryption
The steps to perform RSA encryption using the AWS KMS is here:

[https://asecuritysite.com/aws/lab04](https://asecuritysite.com/aws/lab04)

Follow the steps to create RSA encryption.



