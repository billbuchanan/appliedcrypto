<!---
B.4
```python
print (chars//16+1)*32
```
--->
<!---
C.4
```python
print (chars//16+1)*16
```
--->

Commands in Section A:

* openssl list-cipher-commands
* openssl version
* openssl prime –hex 1111
* openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin
* openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin –base64
* openssl enc -d -aes-256-cbc -in encrypted.bin -pass pass:napier -base64
## A.1
<pre>
$ openssl list-cipher-commands
aes-128-cbc
aes-128-ecb
aes-192-cbc
aes-192-ecb
aes-256-cbc
aes-256-ecb
base64
bf
bf-cbc
bf-cfb
bf-ecb
bf-ofb
camellia-128-cbc
camellia-128-ecb
camellia-192-cbc
camellia-192-ecb
camellia-256-cbc
camellia-256-ecb
cast
cast-cbc
cast5-cbc
cast5-cfb
cast5-ecb
cast5-ofb
des
des-cbc
des-cfb
des-ecb
des-ede
des-ede-cbc
des-ede-cfb
des-ede-ofb
des-ede3
des-ede3-cbc
des-ede3-cfb
des-ede3-ofb
des-ofb
des3
desx
rc2
rc2-40-cbc
rc2-64-cbc
rc2-cbc
rc2-cfb
rc2-ecb
rc2-ofb
rc4
rc4-40
seed
seed-cbc
seed-cfb
seed-ecb
seed-ofb
</pre>
And:
<pre>
napier@napier-virtual-machine:~$ openssl version
OpenSSL 1.0.2g  1 Mar 2016
</pre>

## A.3
<pre>
napier@napier-virtual-machine:~$ nano myfile.txt
napier@napier-virtual-machine:~$ openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin
enter aes-256-cbc encryption password: napier
Verifying - enter aes-256-cbc encryption password: 
napier@napier-virtual-machine:~$ cat encrypted.bin 
Salted__��kBֿ��O�;�|`�"����ե
napier@napier-virtual-machine:~$ openssl enc -d -aes-256-cbc -in encrypted.bin
enter aes-256-cbc decryption password: napier
Hello
</pre>

## A.4
<pre>
napier@napier-virtual-machine:~$ openssl enc -aes-256-cbc -in myfile.txt -out encrypted.bin -base64
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
napier@napier-virtual-machine:~$ cat encrypted.bin 
U2FsdGVkX18Z7N1ZzT9+up7rmoTInUto8HAflAvIEPE=
napier@napier-virtual-machine:~$ openssl enc -d -aes-256-cbc -in encrypted.bin -base64
enter aes-256-cbc decryption password: napier
Hello
</pre>

## A.7
We can use the -bf-cbc option for Blowfish:

<pre>
openssl enc -bf-cbc -in myfile.txt -out encrypted1.bin 
openssl enc -d -bf-cbc -pass pass:password -in encrypted1.bin 
</pre>

A sample run is:
<pre>
$ openssl enc -bf-cbc -in myfile.txt -out encrypted1.bin 
enter bf-cbc encryption password: password
Verifying - enter bf-cbc encryption password: password
$ openssl enc -d -bf-cbc -pass pass:password -in encrypted1.bin 
Hello
</pre>

##  B.2
You may need to install "Crypto" with:
<pre>
pip install pycrypto
</pre>
And Padding with:
<pre>
pip install padding
</pre>

```python
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')
print "\nAfter padding (Bit): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')
print "  decrypt: "+plaintext


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')
print "\nAfter padding (Null): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')
print "  decrypt: "+plaintext


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Random')
print "\nAfter padding (Random): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='Random')
print "  decrypt: "+plaintext
```

## C.2

```python
from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'

plaintext=val


def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))


print "\nDES"
key = hashlib.sha256(password).digest()[:8]

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,DES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext
```

## D.1
```python
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'

if (len(sys.argv)>1):
	val=sys.argv[1]

if (len(sys.argv)>2):
	password=sys.argv[2]

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val
```
A sample run is:
<pre>
napier@napier-virtual-machine:~$ python d1.py hello hello123
After padding (CMS): 68656c6c6f0b0b0b0b0b0b0b0b0b0b0b
Cipher (ECB): 0a7ec77951291795bac6690c9e7f4c0d
  decrypt: hello
napier@napier-virtual-machine:~$ python d1.py inkwell orange
After padding (CMS): 696e6b77656c6c090909090909090909
Cipher (ECB): 484299ceec1ad83b1ce848b0a9733c8d
  decrypt: inkwell
napier@napier-virtual-machine:~$ python d1.py security qwerty
After padding (CMS): 73656375726974790808080808080808
Cipher (ECB): 6be35165e2c9a624de4f401692fe7161
  decrypt: security
napier@napier-virtual-machine:~$ python d1.py Africa changme
After padding (CMS): 4166726963610a0a0a0a0a0a0a0a0a0a
Cipher (ECB): ab453ac52cd3b1a61b35d6e85e4568f8
  decrypt: Africa
</pre>

## D.2
Sample code is:
```python
from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

val='hello'
password='hello'

if (len(sys.argv)>1):
	val=sys.argv[1]

if (len(sys.argv)>2):
	password=sys.argv[2]

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')
print "After padding (CMS): "+binascii.hexlify(bytearray(plaintext))

ciphertext = encrypt(plaintext,key[:8],DES.MODE_ECB)
print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

plaintext = decrypt(ciphertext,key[:8],DES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val
```
A sample run is:

<pre>
napier@napier-virtual-machine:~$ python d2.py hello hello123
After padding (CMS): 68656c6c6f030303
Cipher (ECB): 8f770898ddb9fb38
  decrypt: hello
napier@napier-virtual-machine:~$ python d2.py inkwell orange
After padding (CMS): 696e6b77656c6c01
Cipher (ECB): 1086a73ab5273254
  decrypt: inkwell
napier@napier-virtual-machine:~$ python d2.py security qwerty
After padding (CMS): 73656375726974790808080808080808
Cipher (ECB): d19c86b3fc7e924f148652c183caa922
  decrypt: security
napier@napier-virtual-machine:~$ python d2.py Africa changeme
After padding (CMS): 4166726963610202
Cipher (ECB): 6e11929fe6a3c081
  decrypt: Africa
</pre>

## D.3
Answer:
* /vA6BD+ZXu8j6KrTHi1Y+w== - italy

```python
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding
import base64

val='fox'
password='hello'
cipher=''

import sys

if (len(sys.argv)>1):
	cipher=(sys.argv[1])
if (len(sys.argv)>2):
	password=(sys.argv[2])

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()

cipher='/vA6BD+ZXu8j6KrTHi1Y+w=='

ciphertext = base64.b64decode(cipher)
plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
print plaintext
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val
```


## E.1
Answers:
* germany
* france
* england
* scotland

Possible solution for E.1:

```python
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='fox'
password='hello'
cipher='b436bd84d16db330359edebf49725c62'

import sys

if (len(sys.argv)>1):
	cipher=(sys.argv[1])
if (len(sys.argv)>2):
	password=(sys.argv[2])

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


ciphertext=binascii.unhexlify(cipher)

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
print ('Cipher: '+ cipher)
print ('Password: '+ password)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print ("  decrypt: "+plaintext)
```

A sample run gives:
<pre>
Cipher: b436bd84d16db330359edebf49725c62
Password: hello
  decrypt: germany
 </pre>
## E.2
Answers:
* germany
* france
* england
* scotland

DES uses a 64-bit key, of which we have use 56 bits for the actual key. We thus need to truncate our SHA-256 generated key, down to a 64-bit key. We can do that in Python with [:8]. A possible solution for E.2:

```python
from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

val='fox'
password='hello'
cipher=''

import sys

def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password).digest()


ciphertext=binascii.unhexlify("f37ee42f2267458d")

plaintext = decrypt(ciphertext,key[:8],DES.MODE_ECB)
print plaintext

plaintext = Padding.removePadding(plaintext,mode='CMS')
print "  decrypt: "+plaintext


plaintext=val
```


## F.1
Plaintext: norway

Key: changeme

A sample code is:

```python
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding
import base64

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

pw = ["hello","ankle","changeme","123456"]

c='1jDmCTD1IfbXbyyHgAyrdg=='

for password in pw:

	try:
		key = hashlib.sha256(password).digest()
		cipherhex = base64.b64decode(c).encode('hex')
		ciphertext = binascii.unhexlify(cipherhex)

		print "Cipher (ECB): "+binascii.hexlify(bytearray(ciphertext))

		plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
		plaintext = Padding.removePadding(plaintext,mode='CMS')
		print "  decrypt: "+plaintext
		print "  Key found: "+password

	except:	
		print(".")
 ```


## G.1
Answers:
* e47a2bfe646a - orange
* ea783afc66 - apple
* e96924f16d6e - banana

Just convert the hex value to a byte array:

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
## G.2
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
