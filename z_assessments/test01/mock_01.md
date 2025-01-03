![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Assessments
Here  are few short test question. 

## Q1. Diffie-Hellman

1. G=2351, N=5683, x=7, y=14. What is the shared key?

## Q2. Key Entropy

2. If we have a 16-bit key, but only use 200 phrases. What is the key entropy?

## Q3. Key Cracking

3. If it takes 10ns to test an encryption key. How long will it take to crack a 20-bit key?

## Q4. Public key

4. Outline how Bob proves his identity to Alice using public key.

## Q5. Public key generation

5. With RSA, Bob selects two prime numbers of: p=3, q=5. What are the encryption and decryption keys? For a message of 4, prove that the decrypted value is the same of the message.

## Q6. Encoding

6. What is the Base-64 encoding for "test"?

## Q7. Salting

7. On a Linux system, using APR1, how is the salt defined in the password file?

# Answers
## Q1.

A=(2351^7) mod 5683 = 4612
B=(2351^14) mod 5683 = 4758
Key = 4758^7 mod 5683 = 4614

## Q2.

Key entropy = log (phases) / log (2) 
Key entropy = log (200) / log (2) = 7.6 bits

## Q.3.

Max time to crack = 10e-9 x 2^20
Max time to crack = 0.01 seconds

## Q.5.

N=p x q = 3 x 5 = 15
PHI = (p-1)(q-1) = 8
Pick e for no factors of PHI (1, 2, 4). So let's pick 3.
(3 x d) mod 8 = 1
d = 3

encryption key [15,3]
Decryption key [15,3]

Message = 4
Encrypt: 4^3 mod 15 = 4
Decrypt: 4^3 mod 15 = 4

## Q6.

test -> 01110100 01100101 01110011 01110100 
test -> 011101 000110 010101 110011 011101 00 
test ->  d       G       V       z      d   A  ==

