![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Unit 3: Hashing and MAC

The key concepts are: MD2. MD4. MD5. SHA-1. Salting. Collisions. Murmur and FNV. Bloom Filter. LM Hash. SHA-3. Bcrypt. PBKDF2. Open SSL Hash passwords. One Time Passwords. Timed One Time Password (TOTP). Hashed One Time Password (HOTP). HMAC.

## What you should know at the end of unit?

* How the lengths of the hashes vary with the number of bits in the hash.
* How we can calculate the strengths on passwords.
* Understand how salt is applied to the hashing process.
* Define how collisions can occur within hashing.
* Implement hash cracking methods (John the Ripper and Hashcat).
* Defines the usage of signed hashes (eg HMAC).
* Outlines the usage of OTP and Timed Passwords.


## Presentations

* Week 3 Presentation (PDF) - Hashing: [here](https://github.com/billbuchanan/esecurity/blob/master/unit03_hashing/lecture/chapter03_hashing_authentication.pdf)
* Week 3 Presentation (video) - Hashing: [here](https://youtu.be/3D11YGD4vFQ)
* Week 3 Presentation (live lecture) - Hashing: [here](https://youtu.be/gh2CI5m2W6Y)

## Lab

* Unit 3 Lab (PDF): [here](https://github.com/billbuchanan/esecurity/blob/master/unit03_hashing/lab/new_lab03.pdf)
* Unit 3 Lab (video): [here](https://www.youtube.com/watch?v=rnTLr6iUbf0)
* Unit 3 Lab Part 2 (video): [here](https://www.youtube.com/watch?v=FKO6Pjsbp3g)

## Tests

* Test (Hash Encryption): [here](https://asecuritysite.com/tests/tests?sortBy=cryptobook03)

## Sample Exam Questions

The following are some sample questions for hashing:

* Outline the importance of storing the salt value with the hashed value when storing hashed passwords.
* Bob is using a password to generate a 128-bit encryption key. Explain why the key space is unlikely to be 2<sup>128</sup>, and why key entropy could be used to measure the equivalent key size.
  * Where would I find this info? This is related to key enthropy [here](https://asecuritysite.com//encryption/en), and try and understand how key enthopy relates to the strengh of the encryption.
* Bob has just produced a key pair, in a Base-64 format, and now wants to send this to Alice. What advice would you give him on sending the key pair to Alice?
  * Where would I find this info? Have a think about the certificate which is distributed. You can observe it here.
* Bob sends an encrypted message to Alice, and also sends his digital certificate to Alice to prove his identity. How does Alice prove that it is Bob who sent the message?
* Eve has captured a hashed password. How might she use the Cloud to be able to crack the hashed password, and what is a likely too for this?
  * Where would I find this info? This [article](https://www.linkedin.com/pulse/quantum-v-supercomp-cloud-gpu-race-ultimate-cracking-william-buchanan) outlines a number of methods which might be used, included within Cloud cracking.
* Bob is an administrator for a network, and he tells his management team that user passwords are now salted, and they are thus completely secure against attacks. Is he correct? Explain your viewpoint.
  * Where would I find this info? Have a read of the following [article](https://www.linkedin.com/pulse/salting-password-only-secure-when-you-keep-salt-secret-buchanan?forceNoSplash=true).
* Bob looks at the passwd file on his server, and wants to know the type of salting that is used. How would he do this?
  * Where would I find this info? Have a quick look at the additional lab on [Software Hashes](https://asecuritysite.com/lab04_software_hash.pdf). If you can get the Python script to run in Section G, you'll see them all.
* Bob is looking for a new hashing method for storing passwords, and thinks that he will pick the fastest one. Is this a good approach? Explain your answer.
  * Where would I find this info? Think about whether being fast for hashing is a good idea. Have a look at this [article](https://www.linkedin.com/pulse/when-slow-good-great-slowcoach-bcrypt-william-buchanan). But make up your own mind on the subject.
* What are the typical tools that are used to crack hashed password, and what are the methods they will use to crack them?
  * Where would I find this info? Unit 3 and [Lab 2](https://asecuritysite.com/lab03_hashing_and_certs.pdf).
* Why would Eve have an aversion to salt?
* A password is defined as [a-z]. For a four character password, show that there are 456,976 different passwords.
  * Where would I find this info? Have a look [here](https://asecuritysite.com/encryption/passes).
* A password is defined as [a-zA-Z]. For a four character password, show that there are 7,311,616 different passwords.
  * Where would I find this info? Have a look [here](https://asecuritysite.com/encryption/passes).
* A password is defined as [a-zA-Z0-9]. For a four character password, show that there are 14,776,336 different passwords.
  * Where would I find this info? Have a look [here](https://asecuritysite.com/encryption/passes).
* You are working with a security consultant, and he says that you don't need to check the hashing of passwords, as it should work without testing. You disagree with him, and decide to test your hashing method. Initially you must find test vectors for MD5, SHA-1 and SHA-256. Can you find three test vectors, and test them against an on-line calculator?
* At a security presentation a researcher gives a demonstration of Scrypt. In the presentation he shows a demonstration with a password of "password" and fixed salt of "NaCl". For each run he runs the hashing function, the hashed value changes, but, each time, the computation took longer. Which parameter is the researcher likely to be changing, and why does that parameter exist? Can the researcher select any value for the parameter? [Example](https://asecuritysite.com/encryption/scrypt).
* There has been a major data breach within your company, and you are to appear on Sky News to report it. Your company has used PBKDF2 to hash its passwords. How do you explain to your customers that their passwords are unlikely to be breached?
* It was stated in the recent Yahoo hack that:

"We have confirmed, based on a recent investigation, that a copy of certain user account information was stolen from our networks in late 2014 by what we believe is a state-sponsored actor," Lord wrote. "The account information may have included names, e-mail addresses, telephone numbers, dates of birth, hashed passwords (the vast majority with bcrypt), and, in some cases, encrypted or unencrypted security questions and answers."

Do you think the vast majority of the hashed passwords will be cracked? Do you think they had good practice in place for hashed passwords?



## Addendum

In the lecture, the slide at the end of Unit 2 (Symmetric Key) should be (for an eight character password and with [a-z]):

![](https://asecuritysite.com/public/unit02_update.png)

## Important points
* [BCrypt](https://asecuritysite.com/encryption/bcrypt), [PBKDF2](https://asecuritysite.com/encryption/PBKDF2_2) and [Scrypt](https://asecuritysite.com/encryption/Scrypt) are slow hashing methods, which also have salt, and are highly recommended for password storage.
* The strength of the encryption implementation is measured by key entropy. Anything less than 72 bits is likely to be weak.

## Interested in knowing more?

Hashcat with 8xGPUs in Cloud: [here](https://youtu.be/He_bbEkjF8o)

