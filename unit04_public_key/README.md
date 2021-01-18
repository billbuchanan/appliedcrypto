![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# e-Security Unit 4: Public Key

The key concepts are: Basics, RSA, Elliptic Curve and ElGamal.

## What you should know at the end of unit?

* Explain how public key provides both privacy and identity verification.
  * Where would I find this info? This unit explains public key.
* Understand how the RSA process works, with a simple example.
* Understand how elliptic curve cryptography works, with a simple example.
* Explain the operation of PGP.
* Understands how the private key is used to check the identity of the sender, and how public key is used to preserve the privacy of the message.
* Explain how the e and d values are determined within the RSA method.
  * Where would I find this info? There are some examples [here](https://asecuritysite.com/log/rsa_examples.pdf).

## Presentations

* Week 4 Presentation (PDF) - Public Key Encryption: [here](https://github.com/billbuchanan/esecurity/blob/master/unit04_public_key/lecture/chapter04_public_msc.pdf).
* Week 4 Presentation (video) - Public Key Encryption: [here](https://youtu.be/QEYqkxuzoTg).
* Week 4 Presentation (lecture video - 8 Feb 2020) - Public Key Encryption: [here](https://www.youtube.com/watch?v=PEdCHWdE3zk).

## Lab

* Week 4 Lab (PDF): [here](https://github.com/billbuchanan/esecurity/blob/master/unit04_public_key/lab/new_lab04.pdf)
* Week 4 Lab (Demo): [here](https://youtu.be/6T9bFA2nl3c)

## Public key challenge

1. Bob has the following keys:
<pre>
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQDoIhiWs15X/6xiLAVcBzpgvnuvMzHBJk58wOWrdfyEAcTY10oG
+6auNFGqQHYHbfKaZlEi4prAoe01S/R6jpx8ZqJUN0WKNn5G9nmjJha9Pag28ftD
rsT+4LktaQrxdNdrusP+qI0NiYbNBH6qvCrK0aGiucextehnuoqgDcqmRwIDAQAB
AoGAZCaJu0MJ2ieJxRU+/rRzoFeuXylUNwQC6toCfNY7quxkdDV2T8r038Xc0fpb
sdrix3CLYuSnZaK3B76MbO/oXQVBjDQZ7jVQ5K41nVCEZOtRDBeX5Ue6CBs4iNmC
+QyWx+u4OZPURq61YG7D+F1aWRvczdEZgKHPXl/+s5pIvAkCQQDw4V6px/+DJuZV
5Eg20OZe0m9Lvaq+G9UX2xTA2AUuH8Z79e+SCus6fMVl+Sf/W3y3uXp8B662bXhz
yheH67aDAkEA9rQrvmFj65n/D6eH4JAT4OP/+icQNgLYDW+u1Y+MdmD6A0YjehW3
suT9JH0rvEBET959kP0xCx+iFEjl81tl7QJBAMcp4GZK2eXrxOjhnh/Mq51dKu6Z
/NHBG3jlCIzGT8oqNaeK2jGLW6D5RxGgZ8TINR+HeVGR3JAzhTNftgMJDtcCQQC3
IqReXVmZaeXnrwu07f9zsI0zG5BzJ8VOpBt7OWah8fdmOsjXNgv55vbsAWdYBbUw
PQ+lc+7WPRNKT5sz/iM5AkEAi9Is+fgNy4q68nxPl1rBQUV3Bg3S7k7oCJ4+ju4W
NXCCvRjQhpNVhlor7y4FC2p3thje9xox6QiwNr/5siyccw==
-----END RSA PRIVATE KEY-----

-----BEGIN RSA PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDoIhiWs15X/6xiLAVcBzpgvnuv
MzHBJk58wOWrdfyEAcTY10oG+6auNFGqQHYHbfKaZlEi4prAoe01S/R6jpx8ZqJU
N0WKNn5G9nmjJha9Pag28ftDrsT+4LktaQrxdNdrusP+qI0NiYbNBH6qvCrK0aGi
ucextehnuoqgDcqmRwIDAQAB
-----END RSA PUBLIC KEY-----
</pre>

Alice sends him the following ciphered message:
<pre>
uW6FQth0pKaWc3haoqxbjIA7q2rF+G0Kx3z9ZDPZGU3NmBfzpD9ByU1ZBtbgKC8ATVZzwj15AeteOnbjO3EHQC4A5Nu0xKTWpqpngYRGGmzMGtblW3wBlNQYovDsRUGt+cJK7RD0PKn6PMNqK5EQKCD6394K/gasQ9zA6fKn3f0=
</pre>

What is the message? You might find some interesting code [here](https://asecuritysite.com/encryption/rsa_example).

2. Bob uses the following parameters for his public key:
<pre>
RSA Encryption parameters. Public key: [e,N].
e: 65537
N: 498702132445864856509611776937010471
Cipher: 96708304500902540927682601709667939
</pre>

Can you crack the cipher and find the value, if you know we are using using 60 bit primes [example](https://medium.com/asecuritysite-when-bob-met-alice/cracking-rsa-a-challenge-generator-2b64c4edb3e7)?

## A bit of fun

* A Python program to implement RSA in just 12 lines [here](https://asecuritysite.com/encryption/rsa12).
* A Python program to crack RSA in just 12 lines [here](https://asecuritysite.com/encryption/rsa12_2).
* Elliptic Curve methods are used in key handshaking (ECDH). If you want to see the curves that are used click [here](https://asecurity.site/encryption/ecdh3).

## Sample Exam Questions

The following are sample questions for public key:

* Bob selects a p value of 7 and a q value of 9, but he cannot get his RSA encryption to work. What is the problem?
* Bob has selected a p value of 11 and a q value of 7. Which of the following are possible encryption keys: (5,77), (3,77), (9,77), (11,77), and (24,77).
* Bob and Alice decide to use RSA encryption to send secure email, where Bob uses Alice's public key to encrypt, and she uses her private key to decrypt. What is the main problem caused with this, as apposed to using symmetric encryption?
* Bob tells Alice that she should send her private key in order that he should encrypt something for her. Outline the main problem caused by this.
* Security professionals say that RSA keys of over 1,024 bits are secure. What is the core protection against the RSA method being cracked for keys of 1,024 bits and more.
* Bob says he has had a look at a few RSA public keys and he says that the ones he looked at where all the same. Is he right? If so, what makes public keys different?
* Research: Netscape had to comply with an export [embargo](https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States) on the size of the keys which can be used for RSA. Which major vulnerabilities have resulted?
* Bob and Alice get into a debate about the size of the d and e values in the RSA encryption key. Bob says that, in real-life keys, the length of the e value in (e,n) is normally about the same size as the d value (d,n). Alice disagrees. Who is correct?
  * Where would I find this info? Have a look at some practical examples: [Here](https://asecuritysite.com/encryption/rsa2)

## Examples

RSA Examples: [here](https://asecuritysite.com/public/rsa_examples.pdf).
RSA Keygen: [here](https://asecuritysite.com/encryption/rsa_keygen).
ECC Keygen: [here](https://asecuritysite.com/encryption/ecc_keygen).

## Quick demos

* Introduction to RSA: [here](https://www.youtube.com/watch?v=pHES8eNor6k)
* Introduction to Elliptic Curve: [here](https://youtu.be/_CwIWk6XDmg)
* Picking the Generator Value (G): [here](https://www.youtube.com/watch?v=-TjSuch3VGU)



