# Encryption CTFs
These are a collection of CTFs related to encryption.
## Cracking an encrypted key
Bob has encrypted this RSA key pair with 128-bit AES. But he can't remember the password he applied. All he can remember is that it might have been his favouriate colour. Can you determine the two prime numbers (in hex) which make up the modulus?
```
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIBvTBXBgkqhkiG9w0BBQ0wSjApBgkqhkiG9w0BBQwwHAQIzZS/FkAl8o8CAggA
MAwGCCqGSIb3DQIJBQAwHQYJYIZIAWUDBAECBBDQG9NEvzkLxz9ywcanUMSQBIIB
YJgi4T/Ko02Uwc2rYbWtXmgElqtso2LmSSOLQ6SyTOqaNvOiCn3F+AmUpF4XGHuH
2Oig7U9afUfnk9MAqQf+/hSi5Lc+kbyvLCJjy881Gd8URiqNDhfQM9B0PUljnPY6
de4rGXAg9rzqIfpOxfNEggADegEEN8T1EdxWtrFLViEuZ11h1FWQ92Nsiv9HUi3T
36dC+zRgKeeze2C0REPtd7xWugHocyQL+YtGtGGbSUnukhrTAXAFsZxNDQfy+D9U
o8B3YhPUC1z47nhhmTNtVYiIvFgDDJCa9NOPPnOQ4G5rwcLgpbplsksXfXLM/ONj
gCnrJ7dIt+1ZXsr9K+oynBw86hVBppiQhVar19B4ftPfWDoSieKBuihwIYW0mXqT
P0Jn92jXdCHM0b/9NwO9XkFNvGCRetJHnXuY7oD/7HRH9WkcftloO0r/cAxW0JVl
uvAJRPcSU9/nYqpQT6uOwXQ=
-----END ENCRYPTED PRIVATE KEY-----
```
The method is defined [https://asecuritysite.com/openssl/rsa_keygen2](https://asecuritysite.com/openssl/rsa_keygen2).
### Answer
For this we can basically try with a batch file, and substitute colours. This one works:
```
% cat 1.key | openssl rsa -passin pass:blue -text
Private-Key: (512 bit, 2 primes)
modulus:
    00:eb:3a:72:f0:05:d5:3f:de:f9:5e:7f:77:0a:86:
    f0:a4:bd:ca:51:d1:ac:a7:6a:a7:1d:af:9b:dd:cc:
    a1:37:c5:12:0c:59:57:4d:59:d8:d4:b8:fa:7c:34:
    d8:8b:ab:e6:5b:5e:2e:f1:85:48:27:89:45:bc:cc:
    3a:1f:71:ee:31
publicExponent: 65537 (0x10001)
privateExponent:
    00:b4:bc:85:21:9d:29:bb:d8:a3:fc:12:ae:31:9d:
    7a:fa:e9:84:b1:97:0c:34:da:82:ab:11:8a:0e:42:
    b3:40:b8:26:c5:9e:8a:4e:a9:9d:a2:df:a9:e6:e4:
    89:fa:6b:f1:5e:b4:14:12:60:e4:0f:89:45:b9:db:
    6c:ba:eb:45:1d
prime1:
    00:f8:07:29:8d:3e:20:d4:ee:1d:0d:fd:36:cd:26:
    36:d2:15:5d:f2:3e:6b:fd:ee:2c:29:01:98:4f:a8:
    68:6f:63
prime2:
    00:f2:c9:f7:bf:f2:50:e7:2a:02:8c:74:04:e0:c0:
    b2:d5:9d:b9:fb:d8:d4:eb:5b:33:53:87:ae:86:c8:
    7b:32:5b
exponent1:
    5b:d0:2a:ed:82:06:1d:4c:57:ad:0a:02:f3:46:26:
    1c:f6:93:e4:4c:7f:25:6c:b9:24:24:d7:01:05:d2:
    43:09
exponent2:
    00:95:a8:a5:cd:6e:43:2c:9b:9a:c2:95:69:c4:59:
    44:63:a5:3c:55:e0:4d:2f:5f:22:7e:64:ee:d2:2a:
    96:b6:6d
coefficient:
    3f:01:70:5e:21:bc:ff:6c:a1:a9:23:ff:9f:15:76:
    ab:a0:29:f0:cb:a4:71:51:da:2f:06:cb:ac:ad:00:
    b9:75
writing RSA key
-----BEGIN PRIVATE KEY-----
MIIBVQIBADANBgkqhkiG9w0BAQEFAASCAT8wggE7AgEAAkEA6zpy8AXVP975Xn93
CobwpL3KUdGsp2qnHa+b3cyhN8USDFlXTVnY1Lj6fDTYi6vmW14u8YVIJ4lFvMw6
H3HuMQIDAQABAkEAtLyFIZ0pu9ij/BKuMZ16+umEsZcMNNqCqxGKDkKzQLgmxZ6K
Tqmdot+p5uSJ+mvxXrQUEmDkD4lFudtsuutFHQIhAPgHKY0+INTuHQ39Ns0mNtIV
XfI+a/3uLCkBmE+oaG9jAiEA8sn3v/JQ5yoCjHQE4MCy1Z25+9jU61szU4euhsh7
MlsCIFvQKu2CBh1MV60KAvNGJhz2k+RMfyVsuSQk1wEF0kMJAiEAlailzW5DLJua
wpVpxFlEY6U8VeBNL18ifmTu0iqWtm0CID8BcF4hvP9soakj/58VdqugKfDLpHFR
2i8Gy6ytALl1
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



