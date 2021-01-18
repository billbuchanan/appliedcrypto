![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Test 2
There will be four questions from the units based on units 6 to 10. The following are a few sample questions that will get you thinking in the right areas.

## Digital Certificates

[6. Trust and Digital Certificates] Key concepts: Digital Certificates, Certificate Signing Requests

Learning Outlines:

* Define how PKI is used to secure communications, and how digital certificates would be used in this.
* Understand the signing process involved within the trust infrastructrue.
* Understand the basics of the Code Signing Request (CSR).

Sample questions:

* Bob sends an encrypted message to Alice, and also sends his digital certificate to Alice to prove his identity. How does Alice prove that it is Bob who sent the message?
* The core trust on the Internet is based around PKI (Public Key Infrastructure). Outline how digital certificates are used to provide a degree of trustworthiness.
* Bob has just produced a key pair, in a Base-64 format, and now wants to send this to Alice. What advice would you give him on sending the key pair to Alice? **Where would I find this info?** Have a think about the certificate which is distributed. You can observe it here.
* Bob sends an encrypted message to Alice, and also sends his digital certificate to Alice to prove his identity. How does Alice prove that it is Bob who sent the message?

## 7. Tunnelling

[7. Tunnelling] Key concepts: SSL/TLS Handshaking, Key Exchange, Client Hello, Server Hello, HTTPs communications, and Tor networking. You must understand how to analyse network traces for tunnels:

Learning Outlines:

* Able to explain the handshaking involved in setting up an SSL/TLS tunnel, especially on how the key exchange and encryption methods are defined.
* Able to examine a network trace file (PCAP) for the handshaking involved an identify the key elements of the tunnel.
* Able to understand the scope of the tunnel, and where encryption is applied.

You should be able to analyse each of the following for the key elements of creating a secure tunnel:

* IPSec (PCAP file): here
* SSL (PCAP file): here. Background on SSL: [Link].
* Client Server Connection on Port 443 (See lab, Section E.1): here
* HTTPs (PCAP file): here
* ECDHE (PCAP file): here
* SFTP (PCAP file): here
* TOR (PCAP file): here. Background on Tor: [here]
    

## 8. Cryptocurrencies and Blockchain

[8. Cryptocurrencies and Blockchain] Key concepts: Key generation, Consensus, Transactions, Smart contracts, Ethereum and Signing.

Learning Outlines:

* Understand how distributed ledger technology differs from a traditional financial transaction.
* Understand the usage of the private key to sign Bitcoin transactions, and in creating a signature.
* Understand how the private and public key are created for a Bitcoin wallet.
* Identify the important elements of a Bitcoin transaction on blockchain.info.
* Define the process of a Bitcoin transaction.
* Define the proof of work process for Bitcoin and the rewards for miners.

Sample questions:

* Bob wants to send some Bitcoins to Alice. What are the steps that he will take in order for her to receive them? [Ref: Bitcoin]
* Bitcoin technology has a major problem with its proof-of-work method of gaining a consensus. What are the current drawbacks? [Ref: Blockchain]
* How does Ethereum overcome the problems of the proof-of-work method? [Ref: Blockchain]
* How does the payment of gas focus developers to create efficient coding? [Ref: Blockchain]
* Alice says that her Bitcoin ID address uses Base-64. Is this the case? If not, what format does it use? [Ref: Blockchain]
* Trent says that no way that anyone can track his transactions on Bitcoin. Is this true? If not, explain your argument. [Ref: Bitcoin]
* What evidence does a miner have to give to show it has found the required hash for a block? [Ref: Blockchain]
* How many bits does a Bitcoin ID have? Outline the process of generating the ID. [Ref: Bitcoin]
* With Ethereum, with the genesis block, what are the difficulty, the gaslimit and alloc used for? [Ref: Ethereum]
* Alice tells you that Ethereum uses JavaScript to create a smart contract. You are worried that JavaScript doesn't seem to be a trustworthy language. What is required to make the code running on the blockchain trustworthy? [Ref: Ethereum]
* Bob generates his private key and views it. Can you explain to him what the following listing defines:

<pre>
    C \> openssl ec -in priv.pem -text -noout
    read EC key
    Private-Key  (256 bit)
    priv 
        46 b9 e8 61 b6 3d 35 09 c8 8b 78 17 27 5a 30 
        d2 2d 62 c8 cd 8f a6 48 6d de e3 5e f0 d8 e0 
        49 5f
    pub 
        04 25 00 e7 f3 fb dd f2 84 29 03 f5 44 dd c8 
        74 94 ce 95 02 9a ce 4e 25 7d 54 ba 77 f2 bc 
        1f 3a 88 37 a9 46 1c 4f 1c 57 fe cc 49 97 53 
        38 1e 77 2a 12 8a 58 20 a9 24 a2 fa 05 16 2e 
        b6 62 98 7a 9f
    ASN1 OID  secp256k1
 </pre>       

## 9. Future Cryptography

[9. Future Cryptography. Future cryptography, Zero-knowledge Proofs, Pedersen Commitments.]

Learning Outlines:

* Define the key attributes used to assess the quality of a light-weight encryption method.
* Idenity the operation of a simple Zero-knowledge Proof method.
* Understand how the Pedersen Commitment could be used in hidding the values of a transaction.

Sample questions:

* How do light-weight cryptography methods differ from traditional cryptography methods?
* What are key evaluators that are used to assess light-weight cryptography methods?
* Why would be stream encryption method be preferred to a block encryption method in light-weight cryptography?
* How is the Python yield keyword used in RC4 key stream generation [link]?
* Explain how the Fiat-Shamir method protects passwords.
* How does the Pedersen Commitment preserve privacy, and how are they used in cryptocurrency applications?
* How are Range Proofs used to preserve privacy, and how are they used in cryptocurrency applications?
* Bob the Chip Designer wants to use AES for the design of a new RFID tag, but Alice says he should use ChaCha20. Who is right?

## 10. Tokenization, Authorization and Docker

[10. Tokenization, Authorization and Docker]

Learning Outlines:

* Understand the strengths and weaknesses of using a range of tokens, including with OAuth 2.0, JWT and Fernet token.
* Understand how Docker could be used to setup a secure service (such as for SSH).

Sample questions:

* Define the basic security controls using within JWT.
* Bob the Developer says that JWT is the right way to create a Single Sign On (SSO) for the corportate infrastructure. Is this a good approach? Discuss possible strengths and weaknesses.
* Bob says that OAuth 2.0 is an excellent way to provide authentication into a corporate infrastructure. Is he correct? Justify your answer.
* Bob says that Docker is not a good approach for setting up an SSH server. In terms of configurability, what advantages would setting up an SSH server have with a Docker approach?
* What are the strengths of using Fernet tokens as apposed to JWT? [link]

Remember to look at the labs for the units defined above, as there may be a related question
