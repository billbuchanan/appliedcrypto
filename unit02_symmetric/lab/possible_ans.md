## A OpenSSL
### A.1 - A.7

A.1) 

     openssl list -cipher-commands

     openssl version

A.2) 

     openssl prime –hex 1111

A.3)

     openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin

A.4)

     openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin -base64

A.6)

If you used ***napier*** as the password, you can decrypt the file using:

     openssl enc -d -aes-256-cbc -in encrypted.bin -pass pass:napier -base64

A.7)

Encrypt the file using blowfish:

     openssl enc -blowfish -in myfile.txt -out encrypted.bin -base64
     
If you used ***napier*** as the password, you can decrypt the file using:

     openssl enc -d -blowfish -in encrypted.bin -pass pass:napier -base64 
     
**NOTE:** if you get an empty output, ensure that you have added a super secret message in the *myfile.txt* and execute again the previous commands.

## D Python Coding (Encrypting)
### D.1

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding

import hashlib
import sys
import binascii

val='hello'
password='hello'

plaintext=val

def encrypt(plaintext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method, mode)
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return(ct)

def decrypt(ciphertext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method, mode)
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)

def pad(data,size=128):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return(padded_data)

def unpad(data,size=128):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)

key = hashlib.sha256(password.encode()).digest()

plaintext=pad(plaintext.encode())

print("After padding (CMS): ",binascii.hexlify(bytearray(plaintext)))

ciphertext = encrypt(plaintext,key,modes.ECB())
print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,modes.ECB())

plaintext = unpad(plaintext)
print("  decrypt: ",plaintext.decode())

```


### D.2
```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

import hashlib
import binascii

val='hello'
password='hello123'

plaintext=val

def encrypt(plaintext,key, mode):
    method=algorithms.TripleDES(key)
    cipher = Cipher(method,mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return(ct)

def decrypt(ciphertext,key, mode):
    method=algorithms.TripleDES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)

def pad(data,size=64):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return(padded_data)

def unpad(data,size=64):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)

key = hashlib.sha256(password.encode()).digest()[:16]

print("Before padding: ",plaintext)

plaintext=pad(plaintext.encode())

print("After padding (CMS): ",binascii.hexlify(bytearray(plaintext)))

ciphertext = encrypt(plaintext,key,modes.ECB())
print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,modes.ECB())

plaintext = unpad(plaintext)
print("  decrypt: ",plaintext.decode())
```
A sample is [here](https://replit.com/@billbuchanan/des2#main.py).

A sample run is:

```
$ python d1.py hello hello123
Before padding:  hello
Passphrase:  hello123
After padding (CMS):  b'68656c6c6f030303'
Cipher (ECB):  b'4cd924baf0c9ac60'
  decrypt:  hello
$ python padding_des2.py inkwell orange
Before padding:  inkwell
Passphrase:  orange
After padding (CMS):  b'696e6b77656c6c01'
Cipher (ECB):  b'9e0971175e4dfd5a'
  decrypt:  inkwell
$ python d1.py security qwerty
Before padding:  security
Passphrase:  qwerty
After padding (CMS):  b'73656375726974790808080808080808'
Cipher (ECB):  b'c043b5bba3191fd888223899ba2bcbea'
  decrypt:  security
$ python d1.py Africa changme
Before padding:  Africa
Passphrase:  changeme
After padding (CMS):  b'4166726963610202'
Cipher (ECB):  b'b2a350deec0b0718'
  decrypt:  Africa
```




## E Python Coding (Decrypting)
### E.1
Answers:
* germany
* france
* england
* scotland

Possible solution for E.1:

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

import hashlib
import sys
import binascii

password='hello'
cipher='b436bd84d16db330359edebf49725c62'


def encrypt(plaintext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method,mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return(ct)

def decrypt(ciphertext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)

def pad(data,size=128):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return(padded_data)

def unpad(data,size=128):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)

key = hashlib.sha256(password.encode()).digest()


ciphertext = binascii.unhexlify(cipher)
print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,modes.ECB())

plaintext = unpad(plaintext)
print("  decrypt: ",plaintext.decode())
```
A sample is [here](https://replit.com/@billbuchanan/ansaes01#main.py).

A sample run gives:

```
Cipher: b436bd84d16db330359edebf49725c62
Password: hello
  decrypt: germany
```
### E.2
Answers:
* germany
* france
* england
* scotland

DES uses a 64-bit key, of which we have use 56 bits for the actual key. We thus need to truncate our SHA-256 generated key, down to a 64-bit key. We can do that in Python with [:8]. A possible solution for E.2:

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import sys
import hashlib
import binascii

val='hello'
password='hello'

plaintext=val

def encrypt(plaintext,key, mode):
    method=algorithms.TripleDES(key)
    cipher = Cipher(method,mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return(ct)

def decrypt(ciphertext,key, mode):
    method=algorithms.TripleDES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)

def pad(data,size=64):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return(padded_data)

def unpad(data,size=64):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)



if (len(sys.argv)>1):
    plaintext=str(sys.argv[1])
if (len(sys.argv)>2):
    password=str(sys.argv[2])
  


print("Before padding: ",plaintext)
print("Passphrase: ",password)
  
key = hashlib.sha256(password.encode()).digest()[:16]



plaintext=pad(plaintext.encode())

ciphertext=binascii.unhexlify("0b8bd1e345e7bbf0")
print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,modes.ECB())

plaintext = unpad(plaintext)
print("  decrypt: ",plaintext.decode())
```

A sample is [here](https://replit.com/@billbuchanan/desdec#main.py).

If you want to pass as arguments:

```Python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import sys
import hashlib
import binascii

val='hello'
password='hello'

plaintext=val

def encrypt(plaintext,key, mode):
    method=algorithms.TripleDES(key)
    cipher = Cipher(method,mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return(ct)

def decrypt(ciphertext,key, mode):
    method=algorithms.TripleDES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)

def pad(data,size=64):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return(padded_data)

def unpad(data,size=64):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)



if (len(sys.argv)>1):
    digest=str(sys.argv[1])
if (len(sys.argv)>2):
    password=str(sys.argv[2])
  
 
key = hashlib.sha256(password.encode()).digest()[:16]

ciphertext=binascii.unhexlify(digest)

plaintext = decrypt(ciphertext,key,modes.ECB())

plaintext = unpad(plaintext)
print("  decrypt: ",plaintext.decode())
```

### E.3
In this case we will convert from Base-64 into a byte array and then try to decrypt:

Answer:
* /vA6BD+ZXu8j6KrTHi1Y+w== - italy

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

import hashlib
import binascii
import base64

password='hello'


def encrypt(plaintext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method,mode, default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return(ct)

def decrypt(ciphertext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)

def pad(data,size=128):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return(padded_data)

def unpad(data,size=128):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)

key = hashlib.sha256(password.encode()).digest()


cipher='/vA6BD+ZXu8j6KrTHi1Y+w=='
ciphertext = base64.b64decode(cipher)
print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,modes.ECB())

plaintext = unpad(plaintext)
print("  decrypt: ",plaintext.decode())
```
A sample is [here](https://repl.it/@billbuchanan/ch02ans05#main.py).

## F Catching exceptions
### F.1
Plaintext: norway

Key: changeme

A sample code is:

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

import hashlib
import base64
import binascii

password='hello'
cipher='b436bd84d16db330359edebf49725c62'
pw = ["hello","ankle","changeme","123456"]


def decrypt(ciphertext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method, mode, default_backend())
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)


def unpad(data,size=128):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)


c='1jDmCTD1IfbXbyyHgAyrdg=='
ciphertext = base64.b64decode(c)
print ("Cipher (ECB): ",binascii.hexlify(ciphertext))

for password in pw:

  try:
    key = hashlib.sha256(password.encode()).digest()

    plaintext = decrypt(ciphertext,key,modes.ECB())
    
    plaintext = unpad(plaintext)
    print ("  decrypt: ",plaintext)
    print ("  Key found: ",password)
  except:	
    print(".")
 ```
A sample is [here](https://replit.com/@billbuchanan/aescrack01#main.py).

## G Stream Ciphers
### G.1
Answers:
* e47a2bfe646a - orange
* ea783afc66 - apple
* e96924f16d6e - banana

Just convert the hex value to a byte array:

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
import sys
import binascii
from cryptography.hazmat.backends import default_backend


msg = "edinburgh"
key = "qwerty"

if (len(sys.argv)>1):
	msg=str(sys.argv[1])

if (len(sys.argv)>2):
	key=str(sys.argv[2])

print ("Data:\t",msg)
print ("Key:\t",key)

digest = hashes.Hash(hashes.SHA256(),default_backend())
digest.update(key.encode())
k=digest.finalize()

nonce = b'\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0'
add=''

algorithm = algorithms.ChaCha20(k, nonce)


cipher = Cipher(algorithm, mode=None, backend=default_backend())
# encryptor = cipher.encryptor()
# ct = encryptor.update(msg.encode())

ct=binascii.unhexlify("e47a2bfe646a")
pt = cipher.decryptor()
pt=pt.update(ct)


print ("\nKey:\t",binascii.b2a_hex(key.encode()).decode())
print ("Nonce:\t",binascii.b2a_hex(nonce).decode())
print ("\nCipher:\t",binascii.b2a_hex(ct).decode())
print ("Decrypted:\t",pt.decode())
```

<!--
```javascript
var chacha20 = require("chacha20");
var crypto = require('crypto');

var keyname="qwerty";

var key = crypto.createHash('sha256').update(keyname).digest();

var nonce = new Buffer.alloc(8);

nonce.fill(0);

console.log( key);

var ciphertext="e96924f16d6e" 
// var ciphertext="ea783afc66"
// var ciphertext="e47a2bfe646a"

console.log("Ciphertext:\t",ciphertext);

console.log("Decipher\t",chacha20.decrypt(key,nonce, new Buffer(ciphertext,"hex")).toString());
```
-->

A sample run is:
<pre>
$ <b>npm install chacha20</b>
$ <b>cat fruit.js</b>
var chacha20 = require("chacha20");
var crypto = require('crypto');

var keyname="qwerty";

var key = crypto.createHash('sha256').update(keyname).digest();

var nonce = new Buffer.alloc(8);

nonce.fill(0);

console.log( key);

var ciphertext="e96924f16d6e" 
// var ciphertext="ea783afc66"
// var ciphertext="e47a2bfe646a"

console.log("Ciphertext:\t",ciphertext);

console.log("Decipher\t",chacha20.decrypt(key,nonce, new Buffer(ciphertext,"hex")).toString())

$ <b>node fruit.js</b>
<Buffer 65 e8 4b e3 35 32 fb 78 4c 48 12 96 75 f9 ef f3 a6 82 b2 71 68 c0 ea 74 4b 2c f5 8e e0 23 37 c5>
Ciphertext:	 e96924f16d6e
Decipher	 banana
</pre>

### G.2
Answers:
* 8d1cc8bdf6da - orange
* 911adbb2e6dda57cdaad - strawberry
* 8907deba - kiwi

```javascript
// RC4

var crypto = require('crypto');

var keyname="napier";

var key = crypto.createHash('sha256').update(keyname).digest();

var cipher = crypto.createCipheriv('rc4', key,'' );
var ciphertext = '8d1cc8bdf6da'
console.log("Ciphertext:\t",ciphertext);


var decipher = crypto.createDecipheriv('rc4', key,'' );
var text = decipher.update( new Buffer(ciphertext,"hex"), 'hex','utf8');
console.log("Decipher:\t",text);
```
A sample run is:
<pre>
$ <b>nano fruit2.js</b>
$ <b>cat fruit2.js</b>
var crypto = require('crypto');

var keyname="napier";

var key = crypto.createHash('sha256').update(keyname).digest();

var cipher = crypto.createCipheriv('rc4', key,'' );
var ciphertext = '8d1cc8bdf6da'
console.log("Ciphertext:\t",ciphertext);


var decipher = crypto.createDecipheriv('rc4', key,'' );
var text = decipher.update( new Buffer(ciphertext,"hex"), 'hex','utf8');
console.log("Decipher:\t",text);

$ <b>node fruit2.js </b>
Ciphertext:	 8d1cc8bdf6da
Decipher:	 orange
</pre>
