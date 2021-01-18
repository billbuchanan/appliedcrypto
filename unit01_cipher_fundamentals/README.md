![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Unit 1: Cipher Fundamentals

The key concepts are: 

* Ciphers. 
* Encoding methods (ASCII, UTF-16, Base64, Hex). 
* Prime Numbers. 
* GCD.
* Large numbers. 
* Random Number Generators. 
* Data Integrity (CRC-32). 
* Frequency Analysis. 
* Key-based encryption. 
* Key sizes. 

## What you should know at the end of unit?

* **Understand the conversion of characters between hex, decimal and octal**. Sample question: Convert "hello" into a hex stream. Related material: [here](https://asecuritysite.com/Coding/ascii). 
  * *Why are we studying this?* Encrypted content is converted into a range of different formats, so we need to understand the process of taking plain text and then converting it into other encoding formats. Encryption keys, ciphertext and digital certificates are examples of binary content which must be represented in a text format.
* **Compute the GCD for values**. Sample question: What is the GCD for 42 and 56? Related material: [here](https://asecuritysite.com/encryption/gcd). 
  * *Why are we studying this?* GCD is a fundamental building block used in public key encryption, where we must find two numbers who do not share a common divisor. When we look at public key encryption we will see how GCD is used.
* **Compute the MOD for values**. Sample question: What is the result of 13 MOD 7? 
  * *Why are we studying this?* Within many of the public key methods we use the MOD operator with a prime number, and where it is difficult to find the value of x for Y=g<sup>x</sup>(mod p), even though we know Y, g and p. 
* **Understand how to manually convert from ASCII to Base-64, and vice-versa**. Sample question: What is the Base-64 conversion of “hello”? [here](https://asecuritysite.com/Coding/ascii). 
  * *Why are we studying this?* Base-64 is used extensively in encryption, and many of the keys and cipher text are transported and stored in a Base-64 format.
* **Calculate the time taken to crack a code given a time to try each key, and for the number of processing elements**. Sample question: If it takes 100 years to crack a cipher code, and computing power doubles each year. How long will it take to crack a code after five years? 
  * *Why are we studying this?* We always need to understand the strengths of your encrypted data, especially in the face of GPU based crackers, so we need to understand how quickly it will take to crack our cipher.

## Presentations

* Week 1 Presentation (PDF): [here](https://github.com/billbuchanan/esecurity/tree/master/unit01_cipher_fundamentals/lecture)
* Week 1 Presentation (video): [here](https://www.youtube.com/watch?v=zqmjUpJNcJA)
* Week 1 Class Lecture (video): [here](https://youtu.be/3hkRjzl8B8w)

## Lab

* Week 1 Lab (PDF): [here](https://github.com/billbuchanan/esecurity/tree/master/unit01_cipher_fundamentals/lab) [demo](https://www.youtube.com/watch?v=v6H7lHblKes)

## Sample exam questions

1. Using the table [here](https://asecuritysite.com/public/test_table.pdf), what is the Base-64 encoding for "test"?

1. Using the table [here](https://asecuritysite.com/public/test_table.pdf), is the Base-64 encoding for "help"?

1. If it takes 1ns to test an encryption key. How long will it take to crack a 32-bit key?

1. If it takes 10ns to test an encryption key. How long will it take to crack a 20-bit key?

1. Bob tells Alice that she won't be able to view the cipher text, but when she looks at the messages, they seem to be full of printable characters. What format is Bob likely to be using for the encoding of the cipher text, and what would you ask Alice to look for, in order to confirm your guess?

1. Alice has been reading her crypto books, and she reads that there should be an '=' symbol at the end of the encoding. She observes her encoding of cipher messages to Bob, and sees that some do not have an '=' sign at the end. Is there a problem with her encoder? If not, how often, on average, should she see an '=' sign at the end of her ciphered messages?

1. Bob has two numbers which give a GCD of 1. Trent says that this happens because the numbers are prime. Is Trent correct? Explain your answer.

1. Bob deals in Bitcoins and tells Alice that he has a Base-58 ID? Alice says he is crazy, and has only heard of Base-64. What is Base-58 and how does it differ from Base-64?

1. Bob encrypted a message in 1980, and it took a million years to crack at the time. Assuming that computing power doubles each year, do you think the message will be safe against cracking for existing computer systems?

## Tests

* Take fun cipher code challenge: [here](https://asecuritysite.com/challenges/hex). Go see what score you can achieved. If you can get more than 30, you are doing every well. Something over 90 enters a genius level.
* Five minute challenge: [here](https://asecuritysite.com/challenges/scramb). See if you can solve a scrambled alphabet cipher in just five minutes.
* Test 1 (Caesar): [here](https://asecuritysite.com/tests/tests?sortBy=caesar)
* Test 2 (Hex): [here](https://asecuritysite.com/tests/tests?sortBy=hex01)

Note: There will be no cipher challenges in the assessments, and these tests are just a bit of fun, and for background.

## Answers

Q1
<pre>
test -> 01110100 01100101 01110011 01110100 
test -> 011101 000110 010101 110011 011101 00 
test ->  d       G       V       z      d   A  ==
</pre>

Q2
<pre>
help -> 01101000 01100101 01101100 01110000 
help -> 011101 000110 010101 110011 011101 00 
help ->  a     G        V      s      c    A  ==
</pre>

Q3
<pre>
Max time to crack = 1e-9 x 2^32
Max time to crack = 4.3 seconds
</pre>

Q4
<pre>
Max time to crack = 10e-9 x 2^20
Max time to crack = 0.01 seconds
</pre>

Q8: Have a look [here](https://asecuritysite.com/encryption/base58)







