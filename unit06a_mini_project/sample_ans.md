Try not to look at these answers, unless you really have too ..

# Introduction

## 1
Sample run with Firefox on Mac OSX

<pre>
RSA 1,024   161 ms
RSA 2,048   924 ms
ECC 128-bit  34 ms
ECC 160-bit  43 ms
ECC 256-bit  27 ms
</pre>

What can you observe about the performance of the key pair generation?

**RSA increases greatly with an increasing key size, but ECC is fairly constant.**

## 3. 
Function	Word to hash	Result from your Web page (first two hex characters)	Test using Python [see code below](first two hex characters)	Prove with Openssl

MD5	“Hello”	 	 8b1a9953c4611296a827abf8c47804d7	 

SHA1	“Hello”			f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0

SHA256	“Hello”		 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969	

SHA3	“Hello”			06b3dfaec148fb1bb2b066f10ec285e7c9bf402ab32aa78a5d38e34566810cd2

RIPEMD	“Hello”			d44426aca8ae0a69cdbc4021c64fa5ad68ca32fe

PBKDF2 256-bit	“Hello”			2071f2b297b8373d87489ffa202fe92aef0e710e799af3119d6c44fd8402d463

<pre>
apieraccount@ubuntu:~$ echo -n Hello | openssl md5
(stdin)= 8b1a9953c4611296a827abf8c47804d7
napieraccount@ubuntu:~$ echo -n Hello | openssl sha1
(stdin)= f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0
napieraccount@ubuntu:~$ echo -n Hello | openssl sha256
(stdin)= 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
napieraccount@ubuntu:~$ echo -n Hello | openssl sha1 -ripemd160
(stdin)= d44426aca8ae0a69cdbc4021c64fa5ad68ca32fe
</pre>

A sample run from the Python code is:
<pre>
napieraccount@ubuntu:~$ python f.py
General Hashes
MD5:8b1a9953c4611296a827abf8c47804d7
SHA1:f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0
SHA256:185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
SHA512:3615f80c9d293ed7402687f94b22d58e529b8cc7916f8fac7fddf7fbd5af4cf777d3d795a7a00a16bf7e7f3fb9561ee9baae480da9fe7a18769e71886b03f315
</pre>

For PBKDF2:
<pre>
napieraccount@ubuntu:~$ python g.py
Salt is  C3KthONMn8IY3JK8E0Y/0w==

PBKDF2 (SHA1):$pbkdf2$1000$C3KthONMn8IY3JK8E0Y/0w$KDpgt4.NFrl.WBzjAsWXJ/T0Kgk
PBKDF2 (SHA256):$pbkdf2-sha256$1000$C3KthONMn8IY3JK8E0Y/0w$ZQaitGxMChAxH.aFdG/WMquvQjigz8EIlDB6jUyKa3w
</pre>

## 4.
<pre>
napieraccount@ubuntu:~$ echo -n Hello | openssl md5 -hmac qwerty
(stdin)= 7f43007a026d9696566dc8c7bb2172e4
napieraccount@ubuntu:~$ echo -n Hello | openssl sha1 -hmac qwerty
(stdin)= 8c7cd4cb162bc91e4ee4573aba50ca00474e7c5d
napieraccount@ubuntu:~$ echo -n Hello | openssl sha256 -hmac qwerty
(stdin)= c51283c48610dd9b433ce4bf9e7b0b44b808f98bb056fca45953101b1d8fc973
</pre>

For HMAC:

<pre>
napieraccount@ubuntu:~$ cat 1.js
var crypto = require('crypto');

var key = 'qwerty';
var message = 'Hello';
var hash = crypto.createHmac('md5', key).update(message);

console.log(hash.digest('hex'));
console.log(hash.digest('base64'));

napieraccount@ubuntu:~$ node 1.js
7f43007a026d9696566dc8c7bb2172e4
</pre>

## 5.
<pre>
napieraccount@ubuntu:~$ echo -n Hello | openssl enc -aes-256-cbc  -pass pass:"qwerty" -e -base64 -S 241fa86763b85341 
U2FsdGVkX18kH6hnY7hTQZAGxV2faF01w6uhO+X6+9Q=
</pre>

<pre>
napieraccount@ubuntu:~$ echo -n Hello | openssl enc -aes-256-cbc  -pass pass:"qwerty" -e  -S 241fa86763b85341 
Salted__$�gc�SA��]�h]5ë�;����
</pre>

We can see the word "Salted__".

When we convert we get:
<pre>
(53 61 6C 74 65 64 5F 5F 24)  (1F A8 67 63 B8 53 41 90) (06C55D9F685D35C3ABA13BE5FAFBD4)
</pre>
The format is (signature "Salted__"), (Salt), and (Cipher).

For encryption/decryption:
<pre>
napieraccount@ubuntu:~$ cat enc.txt 
U2FsdGVkX18kH6hnY7hTQZAGxV2faF01w6uhO+X6+9Q=
napieraccount@ubuntu:~$ openssl enc -aes-256-cbc  -pass pass:"qwerty" -d -base64 -S 241fa86763b85341 -in enc.txt -out out.txt
napieraccount@ubuntu:~$ cat out.txt 
Hello
</pre>



