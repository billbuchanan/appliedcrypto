# Encryption CTFs
These are a collection of CTFs related to encryption.
## Cracking an encrypted key
Bob has encrypted this RSA key pair with 128-bit AES. But he can't remember the password he applied. All he can remember is that it might have been his favouriate colour. Can you determine the two prime numbers (in hex) which make up the modulus?
```
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIBvTBXBgkqhkiG9w0BBQ0wSjApBgkqhkiG9w0BBQwwHAQIZY3Pgqla6lACAggA
MAwGCCqGSIb3DQIJBQAwHQYJYIZIAWUDBAECBBCcN0BAWWQwD5+pgSGvnHOpBIIB
YGdKvIl5FzpYbFa7pKWUKyQlKY/QxA4Jhh6iMNU1osXVvczb08lFf7q1tB3Q4QTz
Z8LZaQdnfD5ZGyUbOkEAZnIGThtClqGQQoxwMx226n5efyQvkhCjSfpLFHboY2m1
+tG3OvoO/BmRDbY5PGWURGGwXgsFCgLgV7OfqC6qCfYqPtgBFbNjVZQSM6ojC7dd
p6x3FnU9wvEuVbkuyHjTgVgA8CegeRY+hSXAprd2SD46Y6JqjLHoCA+jbLqJtsXW
cJo88VgUfaz08Ehr4t+gQxl0vS0bm6bevbI1Boe9rQgKGThrqqWrvTXlY17nK48m
4W+Si67DeIIBG5JHIHWQ45Gh/zdjxZdjFXGZi+VSNfgryDPWViPZuhxvR7t1UKpo
JQpHMvfLrgOeLzO5uH8ToAzySJxXIsJKqKXdL7Y41wyF9+C/ahbZppMzzANrjhWc
pXVqFsHfEJRcW9zZXuxCk20=
-----END ENCRYPTED PRIVATE KEY-----
```
The method is defined [https://asecuritysite.com/openssl/rsa_keygen2](https://asecuritysite.com/openssl/rsa_keygen2).
### Answer
For this we can basically try with a batch file, and substitute colours. This one works:
```
% cat 1.key | openssl rsa -passin pass:blue -text
Private-Key: (512 bit, 2 primes)
modulus:
    00:c3:da:b8:08:4e:88:5e:23:11:52:e0:b8:25:42:
    52:40:40:22:58:5d:80:f7:34:2b:f6:ff:5d:1f:7e:
    e3:1d:29:9f:65:77:6d:71:76:97:57:5f:f8:d7:4d:
    b8:9c:0a:4f:7e:93:ff:f5:46:8f:e8:c1:89:b5:b1:
    a2:1e:64:23:71
publicExponent: 65537 (0x10001)
privateExponent:
    14:31:67:ca:0b:76:c9:e5:e9:b2:56:d3:05:9c:69:
    e8:8f:f4:3a:92:21:6a:db:69:31:05:31:2f:bf:20:
    61:70:2b:ef:1e:b4:a8:40:23:6b:1c:fd:58:0e:66:
    aa:0c:d4:e1:3c:47:a2:8b:08:f2:a6:5a:c2:1e:7d:
    76:d4:bd:f5
prime1:
    00:ec:14:d3:2a:06:c3:bf:0d:68:e0:83:3f:7c:7f:
    ec:87:16:30:dd:9a:bc:57:0d:e7:0b:db:39:16:5b:
    12:4c:df
prime2:
    00:d4:61:05:b7:59:ff:93:ee:91:33:56:fb:87:86:
    68:4e:fa:82:8c:10:68:85:b3:70:9e:f2:c8:e1:a3:
    ca:49:af
exponent1:
    74:62:ab:db:bb:2c:03:63:24:02:13:12:58:59:64:
    8d:10:56:94:d9:74:e2:61:fb:36:b0:23:cb:ae:a8:
    2d:f7
exponent2:
    00:9e:cf:da:85:6c:20:49:0f:d9:b6:69:71:f7:bb:
    13:5f:13:c6:f1:54:07:c5:0b:14:c9:57:45:ce:2d:
    3b:c4:73
coefficient:
    00:95:4f:6d:16:84:7f:2b:cc:ca:c9:19:0d:81:db:
    42:b7:ef:82:3c:8c:4d:3c:96:55:32:2c:01:92:c7:
    5e:f1:69
writing RSA key
-----BEGIN PRIVATE KEY-----
MIIBVQIBADANBgkqhkiG9w0BAQEFAASCAT8wggE7AgEAAkEAw9q4CE6IXiMRUuC4
JUJSQEAiWF2A9zQr9v9dH37jHSmfZXdtcXaXV1/41024nApPfpP/9UaP6MGJtbGi
HmQjcQIDAQABAkAUMWfKC3bJ5emyVtMFnGnoj/Q6kiFq22kxBTEvvyBhcCvvHrSo
QCNrHP1YDmaqDNThPEeiiwjyplrCHn121L31AiEA7BTTKgbDvw1o4IM/fH/shxYw
3Zq8Vw3nC9s5FlsSTN8CIQDUYQW3Wf+T7pEzVvuHhmhO+oKMEGiFs3Ce8sjho8pJ
rwIgdGKr27ssA2MkAhMSWFlkjRBWlNl04mH7NrAjy66oLfcCIQCez9qFbCBJD9m2
aXH3uxNfE8bxVAfFCxTJV0XOLTvEcwIhAJVPbRaEfyvMyskZDYHbQrfvgjyMTTyW
VTIsAZLHXvFp
-----END PRIVATE KEY-----
```
## Cracking RSA with Chinese Remainder Theory - Håstad’s Broadcast 

Bob has used the RSA method with three different moduli to encrypt the same message for Alice. These modulus values are 181573934956808382047424502743618497959, 263663189152094019455553753982108272769, and 150466971419052326232703131045351509419. The corresponding ciphered values are 89486828865161621017578261527117772610, 176405275524632787228669332980053978025, and 120736618872251736750094696442087698014. Determine the English city in the message (assume he has used an exponent of 3).

The method is defined [https://asecuritysite.com/cracking/rsa_ctf01](https://asecuritysite.com/cracking/rsa_ctf01).

### Answer

The method is defined [here](https://asecuritysite.com/cracking/rsa_ctf01). In this case, we have used 64-bit primes here and which generates 128-bit modulus values. The values of:

Cipher 1: 89486828865161621017578261527117772610, N1=181573934956808382047424502743618497959
Cipher 2: 176405275524632787228669332980053978025, N2=263663189152094019455553753982108272769
Cipher 3: 120736618872251736750094696442087698014, N3=150466971419052326232703131045351509419

We can solved M^e with CRT to get 8445460724692873078755117519791553896065429140561722150551706781

If we assume e=3, we take the third root to get: 2036453269898309954661
Next we convert this integer to bytes, and display as a string.

Decipher: b'newcastle'

## RSA with a different public exponent and the same modulus (N)

Two RSA ciphers of:
Cipher 1: 285ff85d5d3eaf05cf1724fd469e3d
Cipher 2: 0ad53fff1bb9aec32f124e6a3bbf15
These have been created by the following RSA public keys:
Key 1: e1=65539, N=719418927376937392469793631028788573
Key 2: e2=65537, N=719418927376937392469793631028788573

Determine the Scottish city.

Method is here: [https://asecuritysite.com/cracking/rsa_e](https://asecuritysite.com/cracking/rsa_e) 

### Answer

Plaintext message recovered: stirling

Other information: p=753157364191008241, q=955204000626999853, bits=60, cipher1=209638380732875581317199500772023869, cipher2=56248192157359843908741632748142357

## Fermat's attack

Bob has used RSA to cipher a message to Alice. The cipher value is 19523604121706482215558200036877169200 with a modulus of 102424133664786548527964377021117628383 and using e=65537. His generator, though, has created the two primes numbers fairly near to each other. Using this information, find the original message.

Theory: [https://asecuritysite.com/cracking/fermat_fact](https://asecuritysite.com/cracking/fermat_fact)

### Answer:
```
C:  19523604121706482215558200036877169200
N:  102424133664786548527964377021117628383
Number of bits in p and q:  64
Number of bits in modulus (N): 128

p= 10120480900865301167
q= 10120480900866013649
d= 42017071785064716978655477336057510113
PHI= 102424133664786548507723415219386313568
Message: b'swansea'
```



