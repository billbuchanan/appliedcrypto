
Try not to look at these answers, unless you really have too ..

# Key Exchange

## A	Diffie-Hellman

### A.1	Bob and Alice have agreed on the values:

g=2879, N= 9929

Bob Select x=6, Alice selects y=9

Now calculate (using a calculator): 

Bob’s A value (gx mod N):	**9381**
	
Alice’s B value (gy mod N): **1067**

### A.2	Now they exchange the values. Next calculate the shared key:


Bob’s value (Bx mod N):	 **210**
	
Alice’s value (AY mod N): **210**

Do they match? **[Yes]** 


## B	OpenSSL (Diffie-Hellman and ECC)

### B.1	Generate 768-bit Diffie-Hellman parameters:
<pre>
openssl dhparam -out dhparams.pem 768 -text
cat dhparams.pem	
</pre>

<pre>
napier@napier-virtual-machine:~$ openssl dhparam -out dhparams.pem 768 -text
Generating DH parameters, 768 bit long safe prime, generator 2
This is going to take a long time
....+..........+..................+.....+...............................+.......................................+...............................................+..+.....................+.............+.........................+.............................................................................................................................................................+..............................+.............................................................+............................+..+.......+..................................................+.................+....++*++*++*++*
napier@napier-virtual-machine:~$ cat dhparams.pem 
    DH Parameters: (768 bit)
        prime:
            00:d2:1c:e6:9c:77:ec:ea:c5:46:20:84:74:b0:b1:
            1f:46:4b:00:f4:0d:91:db:c6:d6:a5:9f:a7:88:0b:
            77:da:7b:80:c6:3f:b1:e3:33:c3:8a:ab:a5:62:b5:
            69:9d:d4:55:a2:54:2f:a4:ba:bd:cf:7d:58:04:8d:
            1a:f2:de:90:bd:42:30:6a:02:d6:0c:e8:6f:2b:f1:
            10:8a:99:9d:f9:8a:6e:23:5a:dd:be:0f:87:3b:13:
            b5:22:9c:5e:63:47:0b
        generator: 2 (0x2)
-----BEGIN DH PARAMETERS-----
MGYCYQDSHOacd+zqxUYghHSwsR9GSwD0DZHbxtaln6eIC3fae4DGP7HjM8OKq6Vi
tWmd1FWiVC+kur3PfVgEjRry3pC9QjBqAtYM6G8r8RCKmZ35im4jWt2+D4c7E7Ui
nF5jRwsCAQI=
-----END DH PARAMETERS-----
</pre>

What is the value of g: **2**

How many bits does the prime number have? **768 bits**

How long does it take to produce the parameters for 1,024 bits (Group 2)? **6 seconds**


How long does it take to produce the parameters for 1536 bits (Group 5)? **6 seconds**


How would we change the g value?

<pre>
napier@napier-virtual-machine:~$ openssl dhparam -out dhparams.pem 768 -5 -text
Generating DH parameters, 768 bit long safe prime, generator 5
This is going to take a long time
.....+...........+..................+................+....+....................+...+.........+.........+...+.................................................................+.........................................................+.++*++*++*++*
napier@napier-virtual-machine:~$ cat dhparams.pem 
    DH Parameters: (768 bit)
        prime:
            00:d6:fd:ec:bc:c7:fa:67:7a:03:2e:88:0a:1c:a4:
            0b:d6:6a:b4:d7:1e:72:b8:51:da:84:16:6c:b5:83:
            c6:84:02:8a:6b:76:ba:50:d5:10:5c:48:1a:15:2b:
            a6:00:e7:8a:a2:57:ec:f6:91:67:38:af:0d:76:ea:
            a5:0a:51:40:bf:db:fa:31:25:8c:e0:fd:3b:29:29:
            2c:27:7e:2b:82:7c:7a:b9:e5:0a:fa:33:43:96:24:
            8d:27:df:73:c2:2a:1f
        generator: 5 (0x5)
-----BEGIN DH PARAMETERS-----
MGYCYQDW/ey8x/pnegMuiAocpAvWarTXHnK4UdqEFmy1g8aEAoprdrpQ1RBcSBoV
K6YA54qiV+z2kWc4rw126qUKUUC/2/oxJYzg/TspKSwnfiuCfHq55Qr6M0OWJI0n
33PCKh8CAQU=
-----END DH PARAMETERS-----
</pre>

### B.2	Lets look at the Elliptic curves we can create:
<pre>
openssl ecparam -list_curves
openssl ecparam -name secp256k1 -out secp256k1.pem
openssl ecparam -in secp256k1.pem -text -param_enc explicit -noout
</pre>

What are the details of the key?

<pre>
napier@napier-virtual-machine:~$ openssl ecparam -in secp256k1.pem -text -param_enc explicit -noout
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

**Prime, A, B and Generator**

Now we can create our key pair:
<pre>
openssl ecparam -in secp256k1.pem -genkey -noout -out mykey.pem
</pre>

Name three 160-bit curves:

**secp112r1, secp112r2, ...**

By doing a search on the Internet, which curve does Bitcoin use?

**secp256k1**


### Curve 2559 is a popular curve. Using Google, can you find some popular uses of Curve 25519?
Tor network, IoT, etc

### Can you explain how you would use these EC parameters to perform the ECDH key exchange?
Alice generates a, and then a value of aG (mod p).

Bob generates b, and then a value of bG (mod p).

Alice passes aG (mod p) to Bob.

Bob passes bG (mod p) to Alice.

Alice computes abG (mod p), and Bob also computes abG (mod p), and they have a shared secret.





