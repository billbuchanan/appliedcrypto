![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Fake example paper

## Question 1

### Part A

Bob and Co is an ISP, and they have recently been hacked, and their passwords released to the Internet. Their lead Information Officer explains that the passwords use eight character passwords and were salted with a three-character hex value. The regular expression to filter the passwords defines the range of [a-z0-9].

1. What advice would you give to the company on their current policy on hashing their passwords? [4]
2. In the investigation, a hash cracker of 1 Tera hashes per second has been used. Can you estimate how long it would take to crack all the passwords in the data? Give the working-out. [2]
3. On examining the password database, it was found that most passwords had a lower case letter at the start, and always had a number at the end. What effect would this have on the strength of the password and can you estimate the equivalent key entropy [4].

Outline answers:

1. Only lower case and numbers used [1]. The company needs to add a wider range of characters [1]. Small salt value [1] and short password [1].
2. Max time to crack all passwords = 36^8/(1×10^{12})=2.82 seconds [2]. Average will be 1.42 seconds. The salt will be included with the hashed value.
3. Discussion around reduction in strength [2]. Calculation becomes 26×36<sup>6</sup>×10= 565,963,407,360. Key entropy = 39.0 bits [2]. We have 26 letters for the first character, then there will 36 possible characters for the next six characters, and then 10 digits at the end.

### Part B

The following is a password entry, outline the information that can be gained from this password entry and the process that is used when the user logs in. If the salt was lost, outline if it would be possible to recover the original password. For the size of salt used, how could you estimate the increase in difficulty in cracking the salted password? [5]

![esecurity](https://asecuritysite.com/public/hash.png)

Outline answers:

Identify user name, salt, hash [2]. Process [1]. 8×6=48 bits for salt … for every password 2<sup>48</sup> new hashes [2].

## Question 2

Calculate, for Diffie-Hellman, the shared key, if the agreed values are G=201, N=31, and Bob selects 15 and Alice selects 3. Give the working-out. [Marks: 3].

1. In RSA, Bob generates two prime numbers: 13 and 11. From this create the encryption and decryption key. Give the working-out. [Marks: 3].

2. Alice tells Bob that, in RSA, you can select any value of e and d, as long as they do not share the same factors. Is she correct? Outline the procedure that is used to select d, e and N, and why the values need to be selected carefully. [Marks: 6]

3. Mallory and Eve have been watched by law enforcement agencies, and they have been using symmetric encryption to pass messages, and public key to prove identifies and share the symmetric key. Eve now says that Trent the Investigator has been able to get access to her key pair (public and private key). What effect might this have on the security of the messages passed between Mallory and Eve? [Marks: 3]

Outline answers:

1. Standard Diffie-Hellman calculation [3].
2. Standard RSA calculation [3].
3. Standard method of selecting for RSA [2]. N too small ... easy to crack [1]. e to small then M^e less than N, easy to crack [1]. e too large … large overhead in calculations [1] and p and q constrained by key size (and computation limits) [1]. Session key from Eve to Mallory could have been compromised [1]. Trent could have pretended to be Eve [1].

## Question 3

1. PKI uses key pairs for encryption and digital certificates to prove identity. Explain how PKI can be used to keep messages between Bob and Alice secret, and also how we can prove Bob's identity and the integrity of the message. How might an intruder manage to pretend to be Bob? [Marks: 5]
2. PGP provides a method of securing email. Outline how PGP uses asymmetric and symmetric encryption in order to secure emails, while proving identities. [Marks: 4]
3. Bob is watching Alice's cipher stream and he says that he can determine some information about what her plain text is. If she is using ECB (Electronic Code Book) without salt and a 128-bit block cipher, outline what information Bob could gain from Alice's cipher stream. [Marks: 2]
4. Alice says she is using CBC (Cipher Block Chaining), and continually sends the message "Hello" to Bob. She tells him that the cipher message will always change, and will always be different, so that Eve can't tell that the message is repeating. Is she right? Justify your answer. How could Eve determine that the messages are the same? [Marks: 4]

Outline answers:

1. Outline usage of private key to sign and outline usage of public key to secure messages [2]. Digital certificate contains key pair [0.5]. Export to certificate to check identity [0.5]. Send Alice certificate [1] and signed by root authority [1].
2. Outline process of PGP eg generation of signature [1], session key [1], proving of signature [1], decryption of the message [1].
3. ECB repeated patterns may appear [1]. 128-bit cipher reveals the number of bytes in message [1].
4. Define salt [1]. The cipher is highly likely to change [1]. Eventually the IV vector come round again [1]. Eve matches IV, and knows the messages are the same [1].
