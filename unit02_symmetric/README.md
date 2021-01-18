![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Unit 2: Symmetric Key

The key concepts involved are defining key entropy; key generators (such as using hashing methods to generate keys based on passphrases); symmetric key methods (AES, Twofish, 3DES, RC4 and ChaCha20); stream or block encryption; symmetric key modes (ECB/CBC/OFB); and salting/IV.

<!---
Back-up of content: [here](https://asecuritysite.com/csn11117/unit02)
-->

## What you should know at the end of unit?

* The differences between a stream cipher and a block cipher.
* How salting is used to change the cipher blocks.
* Use openssl to perform practical operations.
* Understand the encoding formats used for cipher text and keys.
* Define the difference between cipher block modes, such as between ECB and CBC.

## Presentations

* Week 2 Presentation (PPTX) - Symmetric Key Encryption: [here](https://github.com/billbuchanan/esecurity/blob/master/unit02_symmetric/lecture/chapter02_secret.pptx)
* Week 2 Presentation (Video) - Symmetric Key Encryption [here](https://youtu.be/nLRV34K3xIo)
* Week 2 Presentation (Lecture - Video) - Symmetric Key Encryption: [here](https://youtu.be/CCOt8Xk3ZVU)

## Lab

* Unit 2 Lab (PDF): [here](https://github.com/billbuchanan/esecurity/blob/master/unit02_symmetric/lab/new_lab02.pdf)
* Unit 2 Lab (Video): [here](https://youtu.be/N3UADaXmOik)

## Quick demos

* Introduction to AES: [here](https://www.youtube.com/watch?v=rSyvUYbMok8)
* Padding in ciphers: [here](https://www.youtube.com/watch?v=R3NosHMSi0o)
* Why EDE in 3DES?: [here](https://www.youtube.com/watch?v=ttayDxqfQkA)

## Sample exam questions
The following are sample exam questions for symmetric key:

* Explain the differences between stream and block ciphers, and why salt is required within the encryption process. 
  * **Where would I find this info?** Have a look at the penguin in [Unit 2](https://asecuritysite.com/public/chapter02_secret.pdf) (Slide 31), and here's an outline of the problem with ECB in this related [article](https://medium.com/asecuritysite-when-bob-met-alice/when-is-high-grade-encryption-not-high-grade-when-its-ecb-e1509ec56930?source=friends_link&sk=31ec28f1c2be74a81e53c67e71d5b259).
* What are the possible advantages of using stream ciphers over block ciphers?
* Bob encrypts his data using secret key encryption and sends it to Alice. Every time he produces the cipher text it changes, and he is worried that Alice will not be able to decipher the cipher text. He encrypts "Hello" and gets a different cipher stream each time. Why does the cipher text change, and why is she still able to decrypt it, even though it changes each time?
* AES uses an S-box to scramble the bits. How are the S-boxes for the encryption and decryption process linked?
* Bob is sending encrypted data to Alice, and Eve is listening. After listening for a while, Eve is able to send a valid encrypted message to Alice. By outlining ECB, discuss how this might be possible. 
  * **Where would I find this info?** Have a look at the penguin in [Unit 2](https://asecuritysite.com/public/chapter02_secret.pdf) (Slide 31), and here's an outline of the problem with ECB in this related article.
* Bob is using a password to generate a 128-bit encryption key. Explain why the key space is unlikely to be 2<sup>128</sup>, and why key entropy could be used to measure the equivalent key size. 
  * **Where would I find this info?** This is related to key entropy [here](https://asecuritysite.com/encryption/en), and try and understand how key entropy relates to the strength of the encryption.
* Bob says that the number of bytes used for the cipher text will change directly with the number of bytes used in the plain text. Alice disagrees and says that most encryption methods involve having block sizes. Who is correct? Explain why.
* With block encryption, how do we know where the ciphered data actually ends? Does it just use an end-of-file character or a NULL character?
* Alice says she is confused that Bob is sending her the same message as a cipher, but every time the cipher text changes. Apart from using the shared encryption key, what does Alice use to decipher the cipher text?
* Bob tells Alice that she won't be able to view the cipher text, but when she looks at the messages, they seem to be full of printable characters. What format is Bob likely to be using for the encoding of the cipher text, and what would you ask Alice to look for, in order to confirm your guess?
* Which of these is correct for CMS padding: "68656c6c6f3132330808080808080808", "68656c6c6f3132330909090909090909", and "68656c6c6f3132330A0A0A0A0A0A0A0A". 
  * **Where would I find information on this?** Look [here](https://asecuritysite.com/encryption/padding).
* Bob wants to cipher "edinburgh" with the key of "hello123" for a 256-bit AES key, and his encoding gives him "6564696e6275726768". What will be the padding that will be added?
* Eve says she thinks she can determine the number of characters within some ciphered plain-text. Is she correct? If so, how many plain-text characters were there in this ciphered message: "6920776f756c64206c696b6520746f2074616b65206120627265616b04040404".
* RC4 is a stream cipher, which is one of the recommended ciphers for IoT devices. Bob says that it has an infinitely long encryption key, and that his devices will not be able to cope with this size of key. How would you convince him that IoT devices will be able to cope with RC4?
* RC4 is used within Wifi systems. With WEP, a 40-bit encryption key which was shared over the network, and which had a 24-bit IV value. In relation to the key size, the scope of the key, and the size of the IV, what do you think were the fundamental problems with this setup?
* Bob says that he can creat two ciphers from a file with the word "hello", and which will always create the same cipher. If the cipher is "Z8onq9tXC3CL2oOwqLLWbg==" and the key is "password", which is the missing part of the command he used (find the replacement for [OPTION1] and [OPTION2]):

<pre>
openssl enc -e -[OPTION1] -in test.txt -pass pass:password -nosalt -[OPTION2]
</pre>

The following are encrypted with aes-256-cbc or 3-DES and have a password of "napier", "123456" or "password". Decode them:

* U2FsdGVkX18K9Dy9I/CewpNH2svvjyhNG3Bod77+uYo=
* U2FsdGVkX18pmUpnI7iopG3gsHVQPT1zyRwjlvAJ+aI=
* U2FsdGVkX19XlsCN50CFxZlBcCplPs9/

Please note: In the file you create, put one new line after the Base64 text. For example the answer to the first one is:
<pre>
openssl enc -d -aes-256-cbc -in test.txt -pass pass:123456 -base64
</pre>
## Addendum
In the lecture, the slide at the end of Unit 2 (Symmetric Key) should be (for an eight character password and with [a-z]):

![](https://github.com/billbuchanan/esecurity/blob/master/z_associated/unit02_update.png)


## Tests

* Test (Symmetric Key Encryption): [here](https://asecuritysite.com/tests/tests?sortBy=cryptobook02)

Note: There will be no multiple choice questions in the tests.
