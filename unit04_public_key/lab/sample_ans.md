
Try not to look at these answers, unless you really have too ..

# Introduction
## A.1
<pre>
pub  2048R/1AD74F42 2015-03-01 Bill Buchanan (None) <w.buchanan@napier.ac.uk>
sub  2048R/6F6AA48C 2015-03-01
</pre>

## A.2
The code used is:
```python
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode

msg="Pob7AQZZSml618nMwTpx3V74N45x/rTimUQeTl0yHq8F0dsekZgOT385Jls1HUzWCx6ZRFPFMJ1RNYR2Yh7AkQtFLVx9lYDfb/Q+SkinBIBX59ER3/fDhrVKxIN4S6h2QmMSRblh4KdVhyY6cOxu+g48Jh7TkQ2Ig93/nCpAnYQ="
privatekey = 'MIICXAIBAAKBgQCwgjkeoyCXm9v6VBnUi5ihQ2knkdxGDL3GXLIUU43/froeqk7q9mtxT4AnPAaDX3f2r4STZYYiqXGsHCUBZcI90dvZf6YiEM5OY2jgsmqBjf2Xkp/8HgN/XDw/wD2+zebYGLLYtd2u3GXx9edqJ8kQcU9LaMH+ficFQyfq9UwTjQIDAQABAoGAD7L1a6Ess+9b6G70gTANWkKJpshVZDGb63mxKRepaJEX8sRJEqLqOYDNsC+pkKO8IsfHreh4vrp9bsZuECrB1OHSjwDB0S/fm3KEWbsaaXDUAu0dQg/JBMXAKzeATreoIYJItYgwzrJ++fuquKabAZumvOnWJyBIs2z103kDz2ECQQDnn3JpHirmgVdf81yBbAJaXBXNIPzOcCth1zwFAs4EvrE35n2HvUQuRhy3ahUKXsKX/bGvWzmC2O6kbLTFEygVAkEAwxXZnPkaAY2vuoUCN5NbLZgegrAtmU+U2woa5A0fx6uXmShqxo1iDxEC71FbNIgHBg5srsUyDj3OsloLmDVjmQJAIy7qLyOA+sCc6BtMavBgLx+bxCwFmsoZHOSX3l79smTRAJ/HY64RREIsLIQ1q/yW7IWBzxQ5WTHgliNZFjKBvQJBAL3t/vCJwRz0Ebs5FaB/8UwhhsrbtXlGdnkOjIGsmV0vHSf6poHqUiay/DV88pvhN11ZG8zHpeUhnaQccJ9ekzkCQDHHG9LYCOqTgsyYms//cW4sv2nuOE1UezTjUFeqOlsgO+WN96b/M5gnv45/Z3xZxzJ4HOCJ/NRwxNOtEUkw+zY='

keyDER = b64decode(privatekey)
keys = RSA.importKey(keyDER)

dmsg = keys.decrypt(b64decode(msg))
print dmsg
```
The output is:
<pre>
Congrats! The flag is nothing_is_impossible
</pre>

## A.3
<pre>
napieraccount@ubuntu:~/.ssh$ cd ~/.ssh
napieraccount@ubuntu:~/.ssh$ ssh-keygen -t rsa -C "w.buchanan@napier.ac.uk"
Generating public/private rsa key pair.
Enter file in which to save the key (/home/napaccount/.ssh/id_rsa): 
/home/napaccount/.ssh/id_rsa already exists.
Overwrite (y/n)? 
napieraccount@ubuntu:~/.ssh$ cat id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,231906D9476629A1F38BF98A15E72E03

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
-----END RSA PRIVATE KEY-----
napieraccount@ubuntu:~/.ssh$ ls
id_rsa  id_rsa.pub  known_hosts
napieraccount@ubuntu:~/.ssh$ cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCjH32w6ZwaLvaFS2ngOdsc7LVvYiqMKg+z42lwX8Hs58N69gjnPFzrHDPr/BnoIGOEkAGUQxbbUJwLXPiy7X682e6S235+Gh3jSW/xKuGbF9Zq+a/gESZ7t4ReBNweg90Baz24438Zodr6wA7AUdQSO9H1qdb7r4gNN5lvr1zMRhitfZW4UtTF/kXyE5KIDicU2zOFwCJ+AmeuBJGx3NI3YX03JWloZqB2y8zRsBNJ8A8BpeszN95p75Xni1AiHLCXM2HdW87mbdD/lsdrgUTYpMco7srcybeI/1ukbbOsPG6tDbEz3o0KFHgvDWc/XfFG/9I/8mOK1pcQRLj9bYRFHd2O4qdKgSTwtw/PDFAQ+pvCjIzylQp/sTCYI/6KvEEiHxWrY10jF+LDe4CDrmxSFxbgXYIjVMFAwCb0fyxud8V4filZwyFAoeSJWW2lHIFiEJpshQhRvu2zlM1vZHBVmKdVtBBVhq5vJ69SKfMgA2Ms7DRhLoqeqcMmzM+egDBEfvW50w6TeAsB3zoocAkPAdaLmORMGLFS1J/KIeme2LpEryC5FaG8/gziM7RsqjrAcQ/ipeIb+fNYT6POX5z/KVM6x7VcdkV0vr/k+Zkb9qeVcsIlBUAQIAfz24wOQCYZ6UnB9va88JWnjVSgwxeL5KmqgHDelFt50LgXrN/KOw== w.buchanan@napier.ac.uk
</pre>

For the RSA private key, protecting it with 128-bit AES, CBC, and the salt used is "231906D9476629A1F38BF98A15E72E03":
<pre>
AES-128-CBC,231906D9476629A1F38BF98A15E72E03
</pre>

# OpenSSL RSA
## B.1
What is the type of public key method used? RSA

How long is the default key: 1024

A sample key:

<pre>
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC3qXK4kCxn3BNk87vJUMwIznU8pTjr10Kma9+Jkj4zEy/fiZtY
xvdmn1rKNq/8fEUDCcRVC8hQBpevqxFiJ3dbA7ZM6VjUAmztOfRfxSezgvkjswVS
F1/cgBM32AB4nx1dkCV/Wgedn3KFIFU+b8LH1ZLoyRMyLnwWmAkT/mBC/QIDAQAB
AoGAE8Yao+Rh44y+SdA0F6irTwdrd+wSBNJYSrKyjo1ARR97uAWIxDYnzNS7Yaoh
qH14sKsMiFuMZZFQI4m3hWnaX7OFjhJvxKjP6+BdXKsnwWxpwec7RS6n9ptA7qlE
aIFfVARyiWjG+q+8Bg8CTaHjGgtYPnfLzJM0Vef6gKg5vgECQQDZSKGxtdbpXwXw
VAC78SyfOOYmWKL1HiZs0nyTOnZmhMSkE4+S38zhDTjITh0cuKTksTFeUku/sRij
4T4Y9iz5AkEA2GMpeeRT3IQntmzQgTc7Rgez73Y/UWFynuErg++9gzI758TO3AoV
lFs4NOUAqhZ5fdwizs6sa0bjYm+BC1mbJQJBAMQVts4QItVSSqK6vDrfh/xctd4v
KUh5oAWe4otfPBCCio7jlDLgwxzp+K9TRxRvUWeMvNe4/uEMKgdiss6GAskCQQCf
MpVZMDriifgNppDgABqDszcWfhCnduI1McQqFT+APn0ETy9Bg8nMlDAN+k061b4c
ctDJBhSj+EtiKFbwWsRhAkAnEPn+6m3djTwJMw82DxK1q2fcIjTR0ng8pyrF2iIR
P7oBP8I4hGix/FOrV8M8virK6iCsslEcZBo39FkEqc0N
-----END RSA PRIVATE KEY-----
</pre>
## B.2
Start and end are:
<pre>
-----BEGIN RSA PRIVATE KEY-----
-----END RSA PRIVATE KEY-----
</pre>
## B.3
We get **modulus** (N), **publicExponent** (e), **privateExponent** (d), **prime1** (p), **prime2** (q). The other parameters are stored to speed up the RSA process, such as **exponent1** (d mod p-1), **exponent2** (d mod q-1) and **coefficient** (inv q mod p).
<pre>
Private-Key: (1024 bit)
modulus:
    00:b7:a9:72:b8:90:2c:67:dc:13:64:f3:bb:c9:50:
    cc:08:ce:75:3c:a5:38:eb:d7:42:a6:6b:df:89:92:
    3e:33:13:2f:df:89:9b:58:c6:f7:66:9f:5a:ca:36:
    af:fc:7c:45:03:09:c4:55:0b:c8:50:06:97:af:ab:
    11:62:27:77:5b:03:b6:4c:e9:58:d4:02:6c:ed:39:
    f4:5f:c5:27:b3:82:f9:23:b3:05:52:17:5f:dc:80:
    13:37:d8:00:78:9f:1d:5d:90:25:7f:5a:07:9d:9f:
    72:85:20:55:3e:6f:c2:c7:d5:92:e8:c9:13:32:2e:
    7c:16:98:09:13:fe:60:42:fd
publicExponent: 65537 (0x10001)
privateExponent:
    13:c6:1a:a3:e4:61:e3:8c:be:49:d0:34:17:a8:ab:
    4f:07:6b:77:ec:12:04:d2:58:4a:b2:b2:8e:8d:40:
    45:1f:7b:b8:05:88:c4:36:27:cc:d4:bb:61:aa:21:
    a8:7d:78:b0:ab:0c:88:5b:8c:65:91:50:23:89:b7:
    85:69:da:5f:b3:85:8e:12:6f:c4:a8:cf:eb:e0:5d:
    5c:ab:27:c1:6c:69:c1:e7:3b:45:2e:a7:f6:9b:40:
    ee:a9:44:68:81:5f:54:04:72:89:68:c6:fa:af:bc:
    06:0f:02:4d:a1:e3:1a:0b:58:3e:77:cb:cc:93:34:
    55:e7:fa:80:a8:39:be:01
prime1:
    00:d9:48:a1:b1:b5:d6:e9:5f:05:f0:54:00:bb:f1:
    2c:9f:38:e6:26:58:a2:f5:1e:26:6c:d2:7c:93:3a:
    76:66:84:c4:a4:13:8f:92:df:cc:e1:0d:38:c8:4e:
    1d:1c:b8:a4:e4:b1:31:5e:52:4b:bf:b1:18:a3:e1:
    3e:18:f6:2c:f9
prime2:
    00:d8:63:29:79:e4:53:dc:84:27:b6:6c:d0:81:37:
    3b:46:07:b3:ef:76:3f:51:61:72:9e:e1:2b:83:ef:
    bd:83:32:3b:e7:c4:ce:dc:0a:15:94:5b:38:34:e5:
    00:aa:16:79:7d:dc:22:ce:ce:ac:6b:46:e3:62:6f:
    81:0b:59:9b:25
exponent1:
    00:c4:15:b6:ce:10:22:d5:52:4a:a2:ba:bc:3a:df:
    87:fc:5c:b5:de:2f:29:48:79:a0:05:9e:e2:8b:5f:
    3c:10:82:8a:8e:e3:94:32:e0:c3:1c:e9:f8:af:53:
    47:14:6f:51:67:8c:bc:d7:b8:fe:e1:0c:2a:07:62:
    b2:ce:86:02:c9
exponent2:
    00:9f:32:95:59:30:3a:e2:89:f8:0d:a6:90:e0:00:
    1a:83:b3:37:16:7e:10:a7:76:e2:35:31:c4:2a:15:
    3f:80:3e:7d:04:4f:2f:41:83:c9:cc:94:30:0d:fa:
    4d:3a:d5:be:1c:72:d0:c9:06:14:a3:f8:4b:62:28:
    56:f0:5a:c4:61
coefficient:
    27:10:f9:fe:ea:6d:dd:8d:3c:09:33:0f:36:0f:12:
    b5:ab:67:dc:22:34:d1:d2:78:3c:a7:2a:c5:da:22:
    11:3f:ba:01:3f:c2:38:84:68:b1:fc:53:ab:57:c3:
    3c:be:2a:ca:ea:20:ac:b2:51:1c:64:1a:37:f4:59:
    04:a9:cd:0d
writing RSA key
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQC3qXK4kCxn3BNk87vJUMwIznU8pTjr10Kma9+Jkj4zEy/fiZtY
xvdmn1rKNq/8fEUDCcRVC8hQBpevqxFiJ3dbA7ZM6VjUAmztOfRfxSezgvkjswVS
F1/cgBM32AB4nx1dkCV/Wgedn3KFIFU+b8LH1ZLoyRMyLnwWmAkT/mBC/QIDAQAB
AoGAE8Yao+Rh44y+SdA0F6irTwdrd+wSBNJYSrKyjo1ARR97uAWIxDYnzNS7Yaoh
qH14sKsMiFuMZZFQI4m3hWnaX7OFjhJvxKjP6+BdXKsnwWxpwec7RS6n9ptA7qlE
aIFfVARyiWjG+q+8Bg8CTaHjGgtYPnfLzJM0Vef6gKg5vgECQQDZSKGxtdbpXwXw
VAC78SyfOOYmWKL1HiZs0nyTOnZmhMSkE4+S38zhDTjITh0cuKTksTFeUku/sRij
4T4Y9iz5AkEA2GMpeeRT3IQntmzQgTc7Rgez73Y/UWFynuErg++9gzI758TO3AoV
lFs4NOUAqhZ5fdwizs6sa0bjYm+BC1mbJQJBAMQVts4QItVSSqK6vDrfh/xctd4v
KUh5oAWe4otfPBCCio7jlDLgwxzp+K9TRxRvUWeMvNe4/uEMKgdiss6GAskCQQCf
MpVZMDriifgNppDgABqDszcWfhCnduI1McQqFT+APn0ETy9Bg8nMlDAN+k061b4c
ctDJBhSj+EtiKFbwWsRhAkAnEPn+6m3djTwJMw82DxK1q2fcIjTR0ng8pyrF2iIR
P7oBP8I4hGix/FOrV8M8virK6iCsslEcZBo39FkEqc0N
-----END RSA PRIVATE KEY-----
</pre>
## B.4
If someone gets your private key they could decrypt things sent to you with your public key, or sign things on your behalf.
## B.5
We see a PUBLIC KEY string:
<pre>
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC3qXK4kCxn3BNk87vJUMwIznU8
pTjr10Kma9+Jkj4zEy/fiZtYxvdmn1rKNq/8fEUDCcRVC8hQBpevqxFiJ3dbA7ZM
6VjUAmztOfRfxSezgvkjswVSF1/cgBM32AB4nx1dkCV/Wgedn3KFIFU+b8LH1ZLo
yRMyLnwWmAkT/mBC/QIDAQAB
-----END PUBLIC KEY-----
</pre>
## B.7
<pre>
napieraccount@ubuntu:~/test$ openssl rsautl -decrypt -inkey private.pem -in file.bin -out decrypted.txt
napieraccount@ubuntu:~/test$ cat decrypted.txt 
Hello
</pre>

## B.8
We have a hex format for the -hexdump output:
<pre>
napieraccount@ubuntu:~/test$ openssl rsautl -encrypt -inkey public.pem -pubin -in myfile.txt -out file.bin -hexdump
napieraccount@ubuntu:~/test$ cat file.bin
0000 - 88 a7 53 b6 da 09 6d 9f-c6 80 95 3b 23 2a bd 20   ..S...m....;#*. 
0010 - 46 fb 4b f0 51 ee 64 66-79 96 3a b4 5c 32 c4 2b   F.K.Q.dfy.:.\2.+
0020 - 62 b6 5b 1c da 99 1d 5f-1f 81 06 2e 2e 53 eb 7e   b.[...._.....S.~
0030 - c9 c4 4e 6c d4 60 86 e0-9f 52 8c aa d2 8f 65 c2   ..Nl.`...R....e.
0040 - 7c 08 83 13 d3 c0 3e ce-fc b6 be 01 75 ad ee bb   |.....>.....u...
0050 - 9a b6 56 b4 e5 22 7b ea-a5 85 2d 16 fa 7f 50 6f   ..V.."{...-...Po
0060 - d7 67 ff bd 97 c2 26 04-1f 8d 4d c7 52 ea 40 6e   .g....&...M.R.@n
0070 - 9a d9 03 10 67 52 a3 05-8f 0c fd 83 7b 1b 89 1b   ....gR......{...
napieraccount@ubuntu:~/test$ openssl rsautl -encrypt -inkey public.pem -pub
</pre>
We get a binary format with:
<pre>
napieraccount@ubuntu:~/test$ openssl rsautl -encrypt -inkey public.pem -pubin -in myfile.txt -out file.bin 
napieraccount@ubuntu:~/test$ cat file.bin
:�H�n�D.Y��?rѐ��XRfZ'����Rs��5|o��{�W��I�f��^9��LP.�z���bunn_�RX�N��%�9���w_��<�x��ɯ��G1�={|"�p��F��94.P[_
 </pre>

# ECC
## C.1
<pre>
napieraccount@ubuntu:~/test$ openssl ecparam -name secp256k1 -genkey -out priv.pem
napieraccount@ubuntu:~/test$ cat priv.pem 
-----BEGIN EC PARAMETERS-----
BgUrgQQACg==
-----END EC PARAMETERS-----
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIIjZk1BI+xwWQZ6XetT17JrQgGLdQzvDnTB6iqLEFsGCoAcGBSuBBAAK
oUQDQgAE4VZg4yjli491gWC+f7mNAtI8pdRyHYXhUVjVTFlVXKvflEd3BxRiMUWC
KJPzklyIgOZFAOMYzSv5YvMA/YovWQ==
-----END EC PRIVATE KEY-----
</pre>
## C.2
Values are A, B, Generator (G) and Prime (p), and where G is the generator point. The curve is:

y<sup>2</sup>=x<sup>3</sup>+a x + b (mod p)

<pre>
napieraccount@ubuntu:~/test$ openssl ecparam -in priv.pem -text -param_enc explicit -noout
Field Type: prime-field
Prime:
    00:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
    ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:fe:ff:
    ff:fc:2f
A:    0
B:    7 (0x7)
Generator (uncompressed):
    04:79:be:66:7e:f9:dc:bb:ac:55:a0:62:95:ce:87:
    0b:07:02:9b:fc:db:2d:ce:28:d9:59:f2:81:5b:16:
    f8:17:98:48:3a:da:77:26:a3:c4:65:5d:a4:fb:fc:
    0e:11:08:a8:fd:17:b4:48:a6:85:54:19:9c:47:d0:
    8f:fb:10:d4:b8
Order: 
    00:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
    ff:fe:ba:ae:dc:e6:af:48:a0:3b:bf:d2:5e:8c:d0:
    36:41:41
Cofactor:  1 (0x1)
</pre>
## C.3
We generate the public key from the private key. If we have a private key (priv) and a generator point (G). The public key is priv G. In this case we are using a curve of secp256k1.
<pre>
napieraccount@ubuntu:~/test$ openssl ec -in priv.pem -text -noout
read EC key
Private-Key: (256 bit)
priv:
    00:88:d9:93:50:48:fb:1c:16:41:9e:97:7a:d4:f5:
    ec:9a:d0:80:62:dd:43:3b:c3:9d:30:7a:8a:a2:c4:
    16:c1:82
pub: 
    04:e1:56:60:e3:28:e5:8b:8f:75:81:60:be:7f:b9:
    8d:02:d2:3c:a5:d4:72:1d:85:e1:51:58:d5:4c:59:
    55:5c:ab:df:94:47:77:07:14:62:31:45:82:28:93:
    f3:92:5c:88:80:e6:45:00:e3:18:cd:2b:f9:62:f3:
    00:fd:8a:2f:59
ASN1 OID: secp256k1
</pre>

How many bits and bytes does your private key have: **256 bits (32 bytes)**


How many bit and bytes does your public key have (Note the 04 is not part of the elliptic curve point): **512 bits (64 bytes)**



What is the ECC method that you have used? **secp256k1**

# ECC Encryption
## D.1
```python
import OpenSSL
import pyelliptic

secretkey="password"
test="Test123"

alice = pyelliptic.ECC() 
bob = pyelliptic.ECC()

print "++++Keys++++"
print "Bob's private key: "+bob.get_privkey().encode('hex')
print "Bob's public key: "+bob.get_pubkey().encode('hex')

print
print "Alice's private key: "+alice.get_privkey().encode('hex')
print "Alice's public key: "+alice.get_pubkey().encode('hex')


ciphertext = alice.encrypt(test, bob.get_pubkey())

print "\n++++Encryption++++"

print "Cipher: "+ciphertext.encode('hex')

print "Decrypt: "+bob.decrypt(ciphertext)

signature = bob.sign("Alice")

print 
print "Bob verified: "+ str(pyelliptic.ECC(pubkey=bob.get_pubkey()).verify
(signature, "Alice"))
```

<pre>
++++Keys++++
Bob's private key: 02f9f16a09b1e7dbb7b6697f94407616d9cd57965146f9fa93e6167c8d59239e09ec68da
Bob's public key: 040634cbbfe036049706a41449a8528bf0f72cb4ada794f57bcaffa7edf77106ac74ce86e605c488184302331d4586638a879b717e66d53ee65363330bfc9f0e780ffed18dab5ff6bf

Alice's private key: 037cfc7ee3bc58f54f213877003b0d3bf8e6d760cc4474ccf9d6fed2ae1b241c0bb9b733
Alice's public key: 04063eefc97bf6cf4b21f9cdad6899c77826f54c03db6c3b08b417bcaac605b53d9e1852f20369db917baa69e30b1a7eafaca8264028bee780701a957f81f8202c86c1f93515227a88

++++Encryption++++
Cipher: ad8e883133fcaf6d14bd7a8d66a610310406d6a7dfb1ea892d5a518ce9155abca28212ed103c4c194aef62462d62eb409e33e5203604291d73d25d0aa63228e1b91fca6339eb384c956b8df64bad1ec4b19883d6531c950ef9e53f4e4686cd8889bdef3edc6625263dd94360585bc3774273402f93d87211767ebd3bde961be86a121c52881873078a
Decrypt: Test123

Bob verified: True
</pre>
## D.2
y<sup>2</sup> = x<sup>3 + 7 (mod 89)
<pre>
A:  0
B:  7
Prime number:		89
Elliptic curve is:		y^2=x^3+ 7
Finding the first 20 points

(14, 9) (15, 0) (16, 3) (17, 5) (22, 8) (24, 6) (40, 4) (60, 2) (70, 1) (71, 7)
</pre>
## D.3
<pre>
napier@napier-virtual-machine:~$ python ecc1.py 
Message:	Hello
Type:		NIST192p
=========================
Signature:	ntghRZKzExfLcoR2TJOw9J+ZJ+Pwq1+n/5UPUQqM5qoM9BKu/hUV/KMFvVIgDmU1
=========================
Signatures match:	True
</pre>

# RSA
## E.1
```python
import rsa
(bob_pub, bob_priv) = rsa.newkeys(512)
print bob_pub
print bob_priv
ciphertext = rsa.encrypt('Here is my message', bob_pub)
message = rsa.decrypt(ciphertext, bob_priv)
print(message.decode('utf8'))
```

A sample run gives:

<pre>
PublicKey(7044152640361902500168576401792350494310726185372977704588682647070501920385795486653093710793158373161949147824992313215786223524754692116109993477603703, 
65537)
PrivateKey(7044152640361902500168576401792350494310726185372977704588682647070501920385795486653093710793158373161949147824992313215786223524754692116109993477603703, 
65537, 1031520101462581111343482730793310461173078401529280666355457029829494893917496934907266419334856470211959662572029962392609614789178286814805200163248601, 
7009636621105341733056641551350073875772161289792261672243040042003271353299512989, 1004924081107519375914073833480034561474534624800691686376057520755477027)
Here is my message
</pre>
The keys are (e,N) for the public key, and (d,N) for the private key. In this case the value of N is:
<pre>
7044152640361902500168576401792350494310726185372977704588682647070501920385795486653093710793158373161949147824992313215786223524754692116109993477603703
</pre>
And e is:
<pre>
65537
</pre>
For the decryption key, N is the same value as the encryption key, and d is:
<pre>
1031520101462581111343482730793310461173078401529280666355457029829494893917496934907266419334856470211959662572029962392609614789178286814805200163248601
</pre>
The two prime numbers used (p and q) are then:
<pre>
7009636621105341733056641551350073875772161289792261672243040042003271353299512989 1004924081107519375914073833480034561474534624800691686376057520755477027
</pre>
Sample:
<pre>
>>> 7009636621105341733056641551350073875772161289792261672243040042003271353299512989*1004924081107519375914073833480034561474534624800691686376057520755477027 
7044152640361902500168576401792350494310726185372977704588682647070501920385795486653093710793158373161949147824992313215786223524754692116109993477603703L
</pre>
# GPG
## F.1
<pre>
napieraccount@ubuntu:~/test$ gpg key01.key 
pub   512R/362DD998 2019-01-19 bill <bill@home.com>
sub   512R/4AA5846A 2019-01-19
</pre>
## F.3
<pre>
napieraccount@ubuntu:~/test$ gpg --gen-key
gpg (GnuPG) 1.4.20; Copyright (C) 2015 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

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
Comment: Test
You selected this USER-ID:
    "Bill Buchanan (Test) <w.buchanan@napier.ac.uk>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O
You need a Passphrase to protect your secret key.

We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
..+++++
......+++++
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
....+++++
+++++
gpg: key B3396725 marked as ultimately trusted
public and secret key created and signed.

gpg: checking the trustdb
gpg: 3 marginal(s) needed, 1 complete(s) needed, PGP trust model
gpg: depth: 0  valid:   3  signed:   0  trust: 0-, 0q, 0n, 0m, 0f, 3u
pub   2048R/B3396725 2020-02-05
      Key fingerprint = C6AA 3C69 9BB9 B49F 1E19  55B7 4CA0 F614 B339 6725
uid                  Bill Buchanan (Test) <w.buchanan@napier.ac.uk>
sub   2048R/F06888D7 2020-02-05

</pre>
Next we export to the public key:
<pre>
napieraccount@ubuntu:~/test$ gpg --export -a "Bill Buchanan" > mypub.key
napieraccount@ubuntu:~/test$ cat mypub.key 
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1

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
f4lt
=3RvZ
-----END PGP PUBLIC KEY BLOCK-----
</pre>
And the private key:
<pre>
napieraccount@ubuntu:~/test$ gpg --export-secret-key -a "Bill Buchanan" > mypriv.key
napieraccount@ubuntu:~/test$ cat mypriv.key 
-----BEGIN PGP PRIVATE KEY BLOCK-----
Version: GnuPG v1

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
=Ul23
-----END PGP PRIVATE KEY BLOCK-----

</pre>


## H.1
Password: napier
![tc](https://github.com/billbuchanan/esecurity/blob/master/unit04_public_key/lab/tc.png)




