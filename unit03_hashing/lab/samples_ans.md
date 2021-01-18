Try not to look at these answers, unless you really have too ..

## A.1
<pre>
Edinburgh - 03CF54D8CE19777B12732B8C50B3B66F
Glasgow - D586293D554981ED611AB7B01316D2D5
Falkirk - 48E935332AADEC763F2C82CDB4601A25
Stirling - EE19033300A54DF2FA41DB9881B4B723
</pre>

## A.3
<pre>
MD5: 32 hex characters (128 bits)
SHA-1: 40 hex characters (160 bits)
SHA-256: 64 hex characters (256 bits)
SHA-384: 96 hex characters (384 bits)
SHA-256: 128 hex characters (384 bits)
</pre>

## A.4
<pre>
napier - bill:$apr1$waZS/8Tm$jDZmiZBct/c2hysERcZ3m1 Use: openssl passwd -apr1 -salt waZS/8Tm napier
Ankle123 - mike:$apr1$mKfrJquI$Kx0CL9krmqhCu0SHKqp5Q0 Use: openssl passwd -apr1 -salt mKfrJquI Ankle123
inkwell - fred:$apr1$Jbe/hCIb$/k3A4kjpJyC06BUUaPRKs0 Use: openssl passwd -apr1 -salt Jbe/hCIb inkwell
password - ian:$apr1$0GyPhsLi$jTTzW0HNS4Cl5ZEoyFLjB. Use: openssl passwd -apr1 -salt 0GyPhsLi password
napier - jane: $1$rqOIRBBN$R2pOQH9egTTVN1Nlst2U7. Use: openssl passwd -1 -salt rqOIRBBN napier
</pre>



## A.5
The hash values are:
<pre>
$ cat 1.txt | openssl md5
(stdin)= 5d41402abc4b2a76b9719d911017c592
$ cat 2.txt | openssl md5
(stdin)= e3fc91b12a36c2334ebb5b66caa2d75b
$ cat 3.txt | openssl md5
(stdin)= fea0f1f6fede90bd0a925b4194deac11
$ cat 4.txt | openssl md5
(stdin)= d89b56f81cd7b82856231e662429bcf2
</pre>

We can see that **2.txt** has been modified.

## A.6
The files have the same MD5 signature, but are different in their content:
<pre>
$ cat letter_of_rec.ps | openssl md5
(stdin)= a25f7f0b29ee0b3968c860738533a4b9
$ cat order.ps | openssl md5
(stdin)= a25f7f0b29ee0b3968c860738533a4b9
</pre>

## B.1
<pre>
$ hashcat --help
       # | Name                                             | Category
  ======+==================================================+======================================
    900 | MD4                                              | Raw Hash
      0 | MD5                                              | Raw Hash
   5100 | Half MD5                                         | Raw Hash
    100 | SHA1                                             | Raw Hash
   1300 | SHA2-224                                         | Raw Hash
   1400 | SHA2-256                                         | Raw Hash
  10800 | SHA2-384                                         | Raw Hash
   1700 | >HA2-512                                         | Raw Hash
  17300 | SHA3-224                                         | Raw Hash
  17400 | SHA3-256                                         | Raw Hash
  17500 | SHA3-384                                         | Raw Hash
  17600 | SHA3-512                                         | Raw Hash
  17700 | Keccak-224                                       | Raw Hash
  17800 | Keccak-256                                       | Raw Hash
  17900 | Keccak-384                                       | Raw Hash
  18000 | Keccak-512                                       | Raw Hash
    600 | BLAKE2b-512                                      | Raw Hash
  10100 | SipHash                                          | Raw Hash
   6000 | RIPEMD-160                                       | Raw Hash
   6100 | Whirlpool                                        | Raw Hash
   6900 | GOST R 34.11-94                                  | Raw Hash
</pre>
<p>Sample benchmark for MD5:</p>
<pre>
$ hashcat -b -m 0
hashcat (v5.1.0-42-g471a8cc) starting in benchmark mode...

Hashmode: 0 - MD5

Speed.#1.........:   189.9 MH/s (10.87ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8

Started: Thu Jan 30 15:56:05 2020
Stopped: Thu Jan 30 15:56:12 2020
</pre>
This gives 189 MH/s. For SHA-1:
<pre>
$ hashcat -b -m 100
hashcat (v5.1.0-42-g471a8cc) starting in benchmark mode ...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Benchmark relevant options:
===========================
* --optimized-kernel-enable

Hashmode: 100 - SHA1

Speed.#1.........:   139.2 MH/s (14.44ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8

Started: Thu Jan 30 15:57:41 2020
Stopped: Thu Jan 30 15:57:47 2020
</pre>
We can 139.2 MH/s for SHA-1. For SHA-256:
<pre>
$ hashcat -b -m 1400
hashcat (v5.1.0-42-g471a8cc) starting in benchmark mode...


OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Benchmark relevant options:
===========================
* --optimized-kernel-enable

Hashmode: 1400 - SHA2-256

Speed.#1.........: 60286.7 kH/s (34.61ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8

Started: Thu Jan 30 15:59:16 2020
Stopped: Thu Jan 30 15:59:23 2020
</pre>
This gives 60.2 MH/s. And for APR-1:
<pre>
$ hashcat -b -m 1600
hashcat (v5.1.0-42-g471a8cc) starting in benchmark mode...

Benchmarking uses hand-optimized kernel code by default.
You can use it in your cracking session by setting the -O option.
Note: Using optimized kernel code limits the maximum supported password length.
To disable the optimized kernel code in benchmark mode, use the -w option.

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Benchmark relevant options:
===========================
* --optimized-kernel-enable

Hashmode: 1600 - Apache $apr1$ MD5, md5apr1, MD5 (APR) (Iterations: 1000)

Speed.#1.........:    14387 H/s (70.39ms) @ Accel:1024 Loops:500 Thr:1 Vec:8

Started: Thu Jan 30 16:01:15 2020
Stopped: Thu Jan 30 16:01:18 2020
</pre>
This is only 14.4 kH/s, and which is much slower than the other methods.

## B.2
Answers:
<pre>
napier
password
Ankle123
inkwell
</pre>
Here is a sample run:
<pre>
$ nano words
$ nano hash1
$ cat words
napier
password
Ankle123
inkwell
$ cat hash1
232DD5D7274E0D662F36C575A3BD634C
5F4DCC3B5AA765D61D8327DEB882CF99
6D5875265D1979BDAD1C8A8F383C5FF5
04013F78ACCFEC9B673005FC6F20698D
$ hashcat -m 0 hash1 words
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 4 digests; 4 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Dictionary cache built:
* Filename..: words
* Passwords.: 4
* Bytes.....: 33
* Keyspace..: 4
* Runtime...: 0 secs

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

232dd5d7274e0d662f36c575a3bd634c:napier          
5f4dcc3b5aa765d61d8327deb882cf99:password        
6d5875265d1979bdad1c8a8f383c5ff5:Ankle123        
04013f78accfec9b673005fc6f20698d:inkwell         
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: MD5
Hash.Target......: hash1
Time.Started.....: Thu Jan 30 16:06:47 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:06:47 2020 (0 secs)
Guess.Base.......: File (words)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:     9512 H/s (0.01ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 4/4 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 4/4 (100.00%)
Rejected.........: 0/4 (0.00%)
Restore.Point....: 0/4 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: napier -> inkwell

Started: Thu Jan 30 16:06:46 2020
Stopped: Thu Jan 30 16:06:48 2020
</pre>

## B.3 
The answers are:
<pre>
orange
apple
banana
pear
peach
</pre>
Here is a sample run:
<pre>
$ nano hash2
$ nano fruits
$ cat hash2
FE01D67A002DFA0F3AC084298142ECCD
1F3870BE274F6C49B3E31A0C6728957F
72B302BF297A228A75730123EFEF7C41
8893DC16B1B2534BAB7B03727145A2BB
889560D93572D538078CE1578567B91A
$ cat fruits 
apple
orange
kiwi
lemon
grape
banana
pear
peach
$ hashcat -m 0 hash2 fruits 
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 5 digests; 5 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Dictionary cache built:
* Filename..: fruits
* Passwords.: 8
* Bytes.....: 48
* Keyspace..: 8
* Runtime...: 0 secs

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

1f3870be274f6c49b3e31a0c6728957f:apple           
fe01d67a002dfa0f3ac084298142eccd:orange          
72b302bf297a228a75730123efef7c41:banana          
8893dc16b1b2534bab7b03727145a2bb:pear            
889560d93572d538078ce1578567b91a:peach           
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: MD5
Hash.Target......: hash2
Time.Started.....: Thu Jan 30 16:11:51 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:11:51 2020 (0 secs)
Guess.Base.......: File (fruits)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    16388 H/s (0.01ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 5/5 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 8/8 (100.00%)
Rejected.........: 0/8 (0.00%)
Restore.Point....: 0/8 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: apple -> peach

Started: Thu Jan 30 16:11:51 2020
Stopped: Thu Jan 30 16:11:53 2020
</pre>

## B.4
The word is "help". Here is a sample run:
<pre>
$ nano mywords.txt
$ nano file.txt
$ cat mywords.txt 
hello
goodbye
help
nowhere
$ cat file.txt 
106a5842fc5fce6f663176285ed1516dbb1e3d15c05abab12fdca46d60b539b7
$ hashcat -m 1400 file.txt mywords.txt 
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Dictionary cache built:
* Filename..: mywords.txt
* Passwords.: 4
* Bytes.....: 27
* Keyspace..: 4
* Runtime...: 0 secs

Approaching final keyspace - workload adjusted.  

106a5842fc5fce6f663176285ed1516dbb1e3d15c05abab12fdca46d60b539b7:help
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: SHA2-256
Hash.Target......: 106a5842fc5fce6f663176285ed1516dbb1e3d15c05abab12fd...b539b7
Time.Started.....: Thu Jan 30 16:16:54 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:16:54 2020 (0 secs)
Guess.Base.......: File (mywords.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    10317 H/s (0.00ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 4/4 (100.00%)
Rejected.........: 0/4 (0.00%)
Restore.Point....: 0/4 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: hello -> nowhere

Started: Thu Jan 30 16:16:53 2020
Stopped: Thu Jan 30 16:16:55 2020
</pre>
## B.5
A sample run is:
<pre>
$ nano nthash
$ cat nthash
0333c27eb4b9401d91fef02a9f74840e
$ hashcat -m 1000 nthash mywords.txt 
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Dictionary cache hit:
* Filename..: mywords.txt
* Passwords.: 4
* Bytes.....: 27
* Keyspace..: 4

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

0333c27eb4b9401d91fef02a9f74840e:help            
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: NTLM
Hash.Target......: 0333c27eb4b9401d91fef02a9f74840e
Time.Started.....: Thu Jan 30 16:22:39 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:22:39 2020 (0 secs)
Guess.Base.......: File (mywords.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    10770 H/s (0.00ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 4/4 (100.00%)
Rejected.........: 0/4 (0.00%)
Restore.Point....: 0/4 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: hello -> nowhere

Started: Thu Jan 30 16:22:38 2020
Stopped: Thu Jan 30 16:22:40 2020
</pre>
## B.6
<pre>
celtic
motherwell
aberdeen
livingston
</pre>
A sample run:
<pre>
$ nano football
$ cat football 
celtic
rangers
hearts
inverness
dundee
aberdeen
motherwell
hamilton
hibernian
kilmarnock
livingston
motherwell
$ cat hash3
635450503029fc2484f1d7eb80da8e25bdc1770e1dd14710c592c8929ba37ee9
b3cb6d04f9ccbf6dfe08f40c11648360ca421f0c531e69f326a72dc7e80a0912
bc5fb9abe8d5e72eb49cf00b3dbd173cbf914835281fadd674d5a2b680e47d50
6ac16a68ac94ca8298c9c2329593a4a4130b6fed2472a98424b7b4019ef1d968
$ rm ~/.hashcat/hashcat.potfile
$ hashcat -m 1400 hash3 football
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 4 digests; 4 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Dictionary cache hit:
* Filename..: football
* Passwords.: 12
* Bytes.....: 111
* Keyspace..: 12

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

635450503029fc2484f1d7eb80da8e25bdc1770e1dd14710c592c8929ba37ee9:celtic
bc5fb9abe8d5e72eb49cf00b3dbd173cbf914835281fadd674d5a2b680e47d50:aberdeen
6ac16a68ac94ca8298c9c2329593a4a4130b6fed2472a98424b7b4019ef1d968:livingston
                                                 
Session..........: hashcat
Status...........: Exhausted
Hash.Type........: SHA2-256
Hash.Target......: hash3
Time.Started.....: Thu Jan 30 16:42:24 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:42:24 2020 (0 secs)
Guess.Base.......: File (football)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    26495 H/s (0.01ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 3/4 (75.00%) Digests, 0/1 (0.00%) Salts
Progress.........: 12/12 (100.00%)
Rejected.........: 0/12 (0.00%)
Restore.Point....: 12/12 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: celtic -> motherwell

Started: Thu Jan 30 16:42:24 2020
Stopped: Thu Jan 30 16:42:26 2020

</pre>

## B.7
<pre>
hair
face
eye
</pre>
a->z: 26
aa->zz: 676
aaa->zzz:  17576
aaaa->zzzz:456976

A sample run is:
<pre>
$ nano face
$ cat face
4dc2159bba05da394c3b94c6f54354db1f1f43b321ac4bbdfc2f658237858c70
0282d9b79f42c74c1550b20ff2dd16aafc3fe5d8ae9a00b2f66996d0ae882775
47c215b5f70eb9c9b4bcb2c027007d6cf38a899f40d1d1da6922e49308b15b69
$ hashcat -a 3 -m 1400 face ?l?l?l?l?l?l?l?l --increment
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 3 digests; 3 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Brute-Force
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

Session..........: hashcat                       
Status...........: Exhausted
Hash.Type........: SHA2-256
Hash.Target......: face
Time.Started.....: Thu Jan 30 16:48:55 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:48:55 2020 (0 secs)
Guess.Mask.......: ?l [1]
Guess.Queue......: 1/8 (12.50%)
Speed.#1.........:    68915 H/s (0.00ms) @ Accel:1024 Loops:26 Thr:1 Vec:8
Recovered........: 0/3 (0.00%) Digests, 0/1 (0.00%) Salts
Progress.........: 26/26 (100.00%)
Rejected.........: 0/26 (0.00%)
Restore.Point....: 1/1 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-26 Iteration:0-26
Candidates.#1....: s -> x

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

Session..........: hashcat                       
Status...........: Exhausted
Hash.Type........: SHA2-256
Hash.Target......: face
Time.Started.....: Thu Jan 30 16:48:56 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:48:56 2020 (0 secs)
Guess.Mask.......: ?l?l [2]
Guess.Queue......: 2/8 (25.00%)
Speed.#1.........:  1527.7 kH/s (0.06ms) @ Accel:1024 Loops:26 Thr:1 Vec:8
Recovered........: 0/3 (0.00%) Digests, 0/1 (0.00%) Salts
Progress.........: 676/676 (100.00%)
Rejected.........: 0/676 (0.00%)
Restore.Point....: 26/26 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-26 Iteration:0-26
Candidates.#1....: sa -> xq

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

47c215b5f70eb9c9b4bcb2c027007d6cf38a899f40d1d1da6922e49308b15b69:eye
                                                 
Session..........: hashcat
Status...........: Exhausted
Hash.Type........: SHA2-256
Hash.Target......: face
Time.Started.....: Thu Jan 30 16:48:56 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:48:56 2020 (0 secs)
Guess.Mask.......: ?l?l?l [3]
Guess.Queue......: 3/8 (37.50%)
Speed.#1.........: 10092.9 kH/s (1.36ms) @ Accel:1024 Loops:26 Thr:1 Vec:8
Recovered........: 1/3 (33.33%) Digests, 0/1 (0.00%) Salts
Progress.........: 17576/17576 (100.00%)
Rejected.........: 0/17576 (0.00%)
Restore.Point....: 676/676 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-26 Iteration:0-26
Candidates.#1....: sar -> xqx

0282d9b79f42c74c1550b20ff2dd16aafc3fe5d8ae9a00b2f66996d0ae882775:face
4dc2159bba05da394c3b94c6f54354db1f1f43b321ac4bbdfc2f658237858c70:hair
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: SHA2-256
Hash.Target......: face
Time.Started.....: Thu Jan 30 16:48:56 2020 (0 secs)
Time.Estimated...: Thu Jan 30 16:48:56 2020 (0 secs)
Guess.Mask.......: ?l?l?l?l [4]
Guess.Queue......: 4/8 (50.00%)
Speed.#1.........: 22926.1 kH/s (2.09ms) @ Accel:1024 Loops:26 Thr:1 Vec:8
Recovered........: 3/3 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 212992/456976 (46.61%)
Rejected.........: 0/212992 (0.00%)
Restore.Point....: 6144/17576 (34.96%)
Restore.Sub.#1...: Salt:0 Amplifier:0-26 Iteration:0-26
Candidates.#1....: snts -> xolc

Started: Thu Jan 30 16:48:54 2020
Stopped: Thu Jan 30 16:48:57 2020
</pre>

## B.8
<pre>
passwordW
passowrd5
</pre>
A sample run is:
<pre>
napier@napier-virtual-machine:~/steg/python/lsb$ hashcat -a 3 -m 0 file.txt password?d
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 2 digests; 2 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Brute-Force
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.  

db0edd04aaac4506f7edab03ac855d56:password5       
                                                 
Session..........: hashcat
Status...........: Exhausted
Hash.Type........: MD5
Hash.Target......: file.txt
Time.Started.....: Thu Jan 30 17:00:38 2020 (0 secs)
Time.Estimated...: Thu Jan 30 17:00:38 2020 (0 secs)
Guess.Mask.......: password?d [9]
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:    23640 H/s (0.01ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/2 (50.00%) Digests, 0/1 (0.00%) Salts
Progress.........: 10/10 (100.00%)
Rejected.........: 0/10 (0.00%)
Restore.Point....: 10/10 (100.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: password1 -> password6

Started: Thu Jan 30 17:00:36 2020
Stopped: Thu Jan 30 17:00:39 2020
</pre>

## C.1
<pre>
bert: APPLE
fred: ORANGE
</pre>
A sample run is:
<pre>
$ rm -r ~/.john/
$ nano fruits 
$ cat pwdump 
fred:500:E79E56A8E5C6F8FEAAD3B435B51404EE:5EBE7DFA074DA8EE8AEF1FAA2BBDE876:::
bert:501:10EAF413723CBB15AAD3B435B51404EE:CA8E025E9893E8CE3D2CBF847FC56814:::	
$ cat fruits 
apple
orange
kiwi
lemon
grape
banana
pear
peach
$ john --wordlist=fruits pwdump
Created directory: /home/napier/.john
Loaded 2 password hashes with no different salts (LM [DES 128/128 SSE2-16])
Press 'q' or Ctrl-C to abort, almost any other key for status
ORANGE           (bert)
APPLE            (fred)
2g 0:00:00:00 100% 200.0g/s 800.0p/s 800.0c/s 1600C/s APPLE..PEACH
Use the "--show" option to display all of the cracked passwords reliably
Session completed
$ john --show
Password files required, but none specified
napier@napier-virtual-machine:~/steg/python/lsb$ john --show pwdump
fred:APPLE:500:E79E56A8E5C6F8FEAAD3B435B51404EE:5EBE7DFA074DA8EE8AEF1FAA2BBDE876:::
bert:ORANGE:501:10EAF413723CBB15AAD3B435B51404EE:CA8E025E9893E8CE3D2CBF847FC56814:::	

2 password hashes cracked, 0 left

</pre>

## C.2
<pre>
bert: DUNDEE
fred: ABERDEEN
Admin: PERTH
</pre>
A sample run:
<pre>
$ cat cities
DUNDEE
ABERDEEN
PERTH
EDINBURGH
GLASGOW
$ cat hash6
Admin:500:629E2BA1C0338CE0AAD3B435B51404EE:9408CB400B20ABA3DFEC054D2B6EE5A1:::
fred:501:33E58ABB4D723E5EE72C57EF50F76A05:4DFC4E7AA65D71FD4E06D061871C05F2:::
bert:502:BC2B6A869601E4D9AAD3B435B51404EE:2D8947D98F0B09A88DC9FCD6E546A711:::	
$ john --wordlist=cities hash6
Loaded 4 password hashes with no different salts (LM [DES 128/128 SSE2-16])
Press 'q' or Ctrl-C to abort, almost any other key for status
PERTH            (bert)
ABERDEE          (fred:1)
DUNDEE           (Admin)
3g 0:00:00:00 100% 300.0g/s 500.0p/s 500.0c/s 2000C/s DUNDEE..GLASGOW
Warning: passwords printed above might be partial
Use the "--show" option to display all of the cracked passwords reliably
Session completed
</pre>

## C.3
<pre>
Bert: TIGER
Fred: SNAKE
Admin: ELEPHANT
</pre>
A sample run is:
<pre>
napier@napier-virtual-machine:~/steg/python/lsb$ cat animals 
tiger
cat
snake
gorilla
elephant
napier@napier-virtual-machine:~/steg/python/lsb$ cat hash7
fred:500:5A8BB08EFF0D416AAAD3B435B51404EE:85A2ED1CA59D0479B1E3406972AB1928:::
bert:501:C6E4266FEBEBD6A8AAD3B435B51404EE:0B9957E8BED733E0350C703AC1CDA822:::
admin:502:333CB006680FAF0A417EAF50CFAC29C3:D2EDBC29463C40E76297119421D2A707:::	
napier@napier-virtual-machine:~/steg/python/lsb$ john --wordlist=animals hash7
Loaded 4 password hashes with no different salts (LM [DES 128/128 SSE2-16])
Press 'q' or Ctrl-C to abort, almost any other key for status
ELEPHAN          (admin:1)
TIGER            (bert)
SNAKE            (fred)
3g 0:00:00:00 100% 300.0g/s 500.0p/s 500.0c/s 2000C/s TIGER..ELEPHAN
Warning: passwords printed above might be partial
Use the "--show" option to display all of the cracked passwords reliably
Session completed
</pre>

## D.1
Answers:
<pre>
LM Hash:12b9c54f6fe0ec80aad3b435b51404ee
NT Hash:3ca6cef4b84985b6e3cd7b24843ea7d1
LM Hash:82121098b60f69f5aad3b435b51404ee
NT Hash:828f0524d3fffd8632ee97253183fef3
</pre>
A sample run is here:
<pre>
$ nano d1.py
$ cat d1.py
import passlib.hash;
string="Napier"
print "LM Hash:"+passlib.hash.lmhash.encrypt(string)
print "NT Hash:"+passlib.hash.nthash.encrypt(string)
string="Foxtrot"
print "LM Hash:"+passlib.hash.lmhash.encrypt(string)
print "NT Hash:"+passlib.hash.nthash.encrypt(string)
$ python d1.py
LM Hash:12b9c54f6fe0ec80aad3b435b51404ee
NT Hash:3ca6cef4b84985b6e3cd7b24843ea7d1
LM Hash:82121098b60f69f5aad3b435b51404ee
NT Hash:828f0524d3fffd8632ee97253183fef3
</pre>

## E.1
Answers:
<pre>
$ nano apr1.py
changeme - $apr1$PkWj6gM4$V2w1yci/N1HCLzcqo3jiZ/
123456 - $apr1$PkWj6gM4$opHu7xKPBmSPWdVO8vidC/
password - $apr1$PkWj6gM4$OupRScHgsxe5lQj4.azPy.
</pre>
The following is a sample run:
<pre>
$ nano apr1.py
$ cat apr1.py
import passlib.hash;

salt="PkWj6gM4"
string="changeme"
print "APR1:"+passlib.hash.apr_md5_crypt.encrypt(string, salt=salt)
string="123456"
print "APR1:"+passlib.hash.apr_md5_crypt.encrypt(string, salt=salt)
string="password"
print "APR1:"+passlib.hash.apr_md5_crypt.encrypt(string, salt=salt)

$ <strong>python apr1.py </strong>
APR1:$apr1$PkWj6gM4$V2w1yci/N1HCLzcqo3jiZ/
APR1:$apr1$PkWj6gM4$opHu7xKPBmSPWdVO8vidC/
APR1:$apr1$PkWj6gM4$OupRScHgsxe5lQj4.azPy.
</pre>

## F.1
Answers for "changeme":
<pre>
SHA1:$sha1$480000$8sFt66rZ$dNfLzeD4O48TgFqDKd0zBYc4SJ5a
SHA256:$5$rounds=535000$8sFt66rZ$yNCVBp7NMi3UNzMEIoGoGnQZ.HMGaUETwiQNCBi/cl5
SHA512:$6$rounds=656000$8sFt66rZ$B/.Msj2UuS3qH.Qxsy.RL82oni6MV75LZ8olN6eCw6.LSHCCcJ4IGnzdX9Qv299whMbpz4rR9e7A9Ab0L3ZA0/
</pre>
<pre>
$ nano sha1.py
$ cat sha1.py
import passlib.hash;
salt="8sFt66rZ"
string="changeme"
print "SHA1:"+passlib.hash.sha1_crypt.encrypt(string, salt=salt)
print "SHA256:"+passlib.hash.sha256_crypt.encrypt(string, salt=salt)
print "SHA512:"+passlib.hash.sha512_crypt.encrypt(string, salt=salt)
$ python sha1.py
SHA1:$sha1$480000$8sFt66rZ$dNfLzeD4O48TgFqDKd0zBYc4SJ5a
SHA256:$5$rounds=535000$8sFt66rZ$yNCVBp7NMi3UNzMEIoGoGnQZ.HMGaUETwiQNCBi/cl5
SHA512:$6$rounds=656000$8sFt66rZ$B/.Msj2UuS3qH.Qxsy.RL82oni6MV75LZ8olN6eCw6.LSHCCcJ4IGnzdX9Qv299whMbpz4rR9e7A9Ab0L3ZA0/
</pre>

## G.1
Answers:
<pre>
$pbkdf2$131000$WkR6UEU0NUM$qS7S53GV52Ha3Qq1SUna.XlrS1U
$pbkdf2-sha256$29000$WkR6UEU0NUM$gWsN0JM2s94YGo0W9On0Mz6yFvRMCFRE1Ms4dXIpCE4

$pbkdf2$131000$WkR6UEU0NUM$Ax363Np0kPa.8vfjSkepDqEMFYg
$pbkdf2-sha256$29000$WkR6UEU0NUM$GHyI8vXC/POt8bfLR35D.9uLvLtPCoBiUDa1O00Ef28

$pbkdf2$131000$WkR6UEU0NUM$.L1L.AVXTBSsc0FuHRQz4PNMVXc
$pbkdf2-sha256$29000$WkR6UEU0NUM$pd1VbFkOA/VwbhJZhJ.25kHPsKVXika2XsuKYoudcug
</pre>
A sample run is:
<pre>
$ nano pb.py
$ cat pb.py 
import hashlib;
import passlib.hash;
import sys;


salt="ZDzPE45C"
string="password"

if (len(sys.argv)>1):
	string=sys.argv[1]

if (len(sys.argv)>2):
	salt=sys.argv[2]

print "PBKDF2 (SHA1):"+passlib.hash.pbkdf2_sha1.encrypt(string, salt=salt)
print "PBKDF2 (SHA256):"+passlib.hash.pbkdf2_sha256.encrypt(string, salt=salt)
$ python pb.py changeme ZDzPE45C
PBKDF2 (SHA1):$pbkdf2$131000$WkR6UEU0NUM$qS7S53GV52Ha3Qq1SUna.XlrS1U
PBKDF2 (SHA256):$pbkdf2-sha256$29000$WkR6UEU0NUM$gWsN0JM2s94YGo0W9On0Mz6yFvRMCFRE1Ms4dXIpCE4
$ python pb.py 123456 ZDzPE45C
PBKDF2 (SHA1):$pbkdf2$131000$WkR6UEU0NUM$Ax363Np0kPa.8vfjSkepDqEMFYg
PBKDF2 (SHA256):$pbkdf2-sha256$29000$WkR6UEU0NUM$GHyI8vXC/POt8bfLR35D.9uLvLtPCoBiUDa1O00Ef28
$ python pb.py password ZDzPE45C
PBKDF2 (SHA1):$pbkdf2$131000$WkR6UEU0NUM$.L1L.AVXTBSsc0FuHRQz4PNMVXc
PBKDF2 (SHA256):$pbkdf2-sha256$29000$WkR6UEU0NUM$pd1VbFkOA/VwbhJZhJ.25kHPsKVXika2XsuKYoudcug
</pre>

## H.1
A sample run:
<pre>
napier@napier-virtual-machine:~/steg/python/lsb$ nano bc.py
napier@napier-virtual-machine:~/steg/python/lsb$ cat bc.py
import hashlib;
import passlib.hash;

salt="ZDzPE45C"
string="hello"
salt2="1111111111111111111111"

print "General Hashes"
print "MD5:"+hashlib.md5(string).hexdigest()
print "SHA1:"+hashlib.sha1(string).hexdigest()
print "SHA256:"+hashlib.sha256(string).hexdigest()
print "SHA512:"+hashlib.sha512(string).hexdigest()

print "UNIX hashes (with salt)"
print "DES:"+passlib.hash.des_crypt.encrypt(string, salt=salt[:2])
print "MD5:"+passlib.hash.md5_crypt.encrypt(string, salt=salt)
print "Sun MD5:"+passlib.hash.sun_md5_crypt.encrypt(string, salt=salt)
print "SHA1:"+passlib.hash.sha1_crypt.encrypt(string, salt=salt)
print "SHA256:"+passlib.hash.sha256_crypt.encrypt(string, salt=salt)
print "SHA512:"+passlib.hash.sha512_crypt.encrypt(string, salt=salt)
print "Bcrypt:"+passlib.hash.bcrypt.encrypt(string, salt=salt2[:22])
napier@napier-virtual-machine:~/steg/python/lsb$ python bc.py
General Hashes
MD5:5d41402abc4b2a76b9719d911017c592
SHA1:aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
SHA256:2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
SHA512:9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043
UNIX hashes (with salt)
DES:ZDVX7N5Bz.8wk
MD5:$1$ZDzPE45C$dOTT0LUnoqs6J7mNLdyse0
Sun MD5:$md5,rounds=34000$ZDzPE45C$$fdZ8uoSiWj6RcJOoMiaKX1
SHA1:$sha1$480000$ZDzPE45C$LnzxSENDwEXBWKTQ1fc9/6BervKU
SHA256:$5$rounds=535000$ZDzPE45C$TTN/Qd.elve1rHLazTSL0KCFxi7z5X9B/5l3xwFniaD
SHA512:$6$rounds=656000$ZDzPE45C$6VWOiufRnOnxxetIEuLTZiM709Z3SBuNxhCf0Y0N4MUOgSTE85Nf9lI7FJJO4Autc2WEahI4URTibVYNy9V8w.
Bcrypt:$2b$12$111111111111111111111u/oq5MIbCQah3/a.C6KTM0d7mD3wwZw.
</pre>

## L.3
<pre>
$ hashcat -m 0 bfield.hash rockyou.txt 
hashcat (v5.1.0-42-g471a8cc) starting...

OpenCL Platform #1: Intel(R) Corporation
========================================
* Device #1: Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz, 495/1982 MB allocatable, 2MCU

Hashes: 54
8686 digests; 423623 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Salt
* Raw-Hash

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

INFO: Removed 48467 hashes found in potfile.

Dictionary cache built:
* Filename..: rockyou.txt
* Passwords.: 14344391
* Bytes.....: 139921497
* Keyspace..: 14344384
* Runtime...: 1 sec

918c3d1d8ac71df1a6c95a0407db3e35:njimko          
74cf7b73890729e7fe254c52d0838613:nitelife        
40da4fc12d91011e7d5783c60c89c687:nirvana88       
cd098dcb28426b386e2478cc1fae3551:niroshan        
b5da44cbaab293884a6bc0ad739263fa:nintendo2       
a590351c72b9e2f599d811cdba71e938:ninjax          
e287555a4a59ca14d9245d2c4171fb89:ninja666        
4593b12596f75c7467552db8cfb69650:ninguem         
75f287c3315f44f9468dd9610de3a366:nine999         
19f60e1296d8dda0ba697b5dbbb5e761:nincsen         
5264b5abc7024da723dc6eaa9235526c:nikol1          
7eb86783ed219ac7e68c4eea10a0b11e:nikodemus       
eaa01bc7f7edb9dde5e9fb3b15013332:nikki75         
72a04413aa1a15f601aa8cd0da073ec3:nightshadow     
d7981c305d9a7a4fdcaba1eb6721de6b:nightmare3      
bbfce983b6a0eab91928b0ab07594e8f:moffitt         
4f5854c3caf75317aa0454840b2da6d3:nicolette1      
c4edaf1aab98ca062f4ecc6883256bf2:mnbbnm          
a056c888fd268ee001d9ae257915c41e:nicolas15       
4b0f4761b8020fa4dccebb638e4ae3cb:mkonji          
ef0256e05069f3ee0a568fdcc03af116:nick91          
f623d7d7ee0f2f8ebf624f45071245c1:mitcho          
d504d64a1062b1bac22de2b01b4ef0c3:mister12        
4d85e8c7d14c1dd1497f039e1c807b24:nice1234        
392da4c651b8e054c40e3d893c1c7cde:missy911        

</pre>
