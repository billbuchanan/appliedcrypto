![esecurity](https://raw.githubusercontent.com/billbuchanan/appliedcrypto/main/z_associated/esecurity_graphics.png)

# Unit 0: Introduction

## Units
The units involved in the module are:

* Ciphers and Fundamentals.  
* Symmetric (Secret) Key. AES, ChaCha20.
* Hashing and MAC. MD5, SHA-1, SHA-256.
* Asymmetric (Public) Key. RSA and Elliptic Curve.
* Key Exchange. Diffie-Hellman, ECDH.
* Digital Signatures and Digital Certificates. 
* Tunnelling. Tunnelling, including SSL/TLS.
* Cryptocurrencies and Blockchain. Outline of cryptocurrencies, Bitcoins, Ethereum and more.
* Future Cryptography. Outline of areas such as Homomorphic Encryption, Zero-knowledge proofs and Quantum-robust cryptography.
* Host security.

The module uses Teams as the main communication channel [here](https://teams.microsoft.com/l/team/19%3aoiGtiSHzHFM9tPVlc8590AS64_S7TvV3HCqVhVaLlvA1%40thread.tacv2/conversations?groupId=2eea5bc7-7986-4e4f-8b76-f53cc28894a6&tenantId=99e0dc58-9c4b-4820-8617-04c386c254c6). There is also a Teams session each Friday at 6pm.

## Module outline
An introduction video is here:

[![](http://img.youtube.com/vi/0RyBLmKtWG0/0.jpg)](http://www.youtube.com/watch?v=0RyBLmKtWG0 "")

and a Doodle:


[![](http://img.youtube.com/vi/wguYYvXA2T4/0.jpg)](http://www.youtube.com/watch?v=wguYYvXA2T4 "")

We will be using a Ubuntu machine for the practical elements of the module. The VM can either be sourced on vSoC or can be downloaded from [here](https://1drv.ms/u/s!AtLuQYeqHsJljfBbjVakRcSGIsQ3GA?e=DgvMbM). You can download VMWare Workstation or VMWare Fusion from [here](https://softcentre.soc.napier.ac.uk/users.cgi). A demo of using the VM is here:

[![](http://img.youtube.com/vi/tIQYpjaELcA/0.jpg)](http://www.youtube.com/watch?v=tIQYpjaELcA "")

## Draft Timetable
The following is the draft timetable:

| No | Date         | Subject                                            | Lab                            |
|----|--------------|----------------------------------------------------|--------------------------------|
| 2  | 26 Jan 2026  | Ciphers and Fundamentals [[Unit](https://github.com/billbuchanan/appliedcrypto/tree/main/unit01_cipher_fundamentals)]                      | [[Lab](https://github.com/billbuchanan/appliedcrypto/tree/main/unit01_cipher_fundamentals/lab)] [[Demo](https://www.youtube.com/watch?v=v6H7lHblKes)]         |
| 3  | 2 Feb 2026   | Symmetric Key [[Unit](https://github.com/billbuchanan/appliedcrypto/tree/main/unit02_symmetric)]                                 | [[Lab](https://github.com/billbuchanan/appliedcrypto/tree/main/unit02_symmetric/lab)]  [Vincent Rijmen](https://www.youtube.com/watch?v=u8kakBA7mkc)         |
| 4  | 9 Feb 2026  | Hashing and MAC [[Unit](https://github.com/billbuchanan/appliedcrypto/tree/main/unit03_hashing)]                               | [[Lab](https://github.com/billbuchanan/appliedcrypto/tree/main/unit03_hashing/lab)]   [Ivan Damgård](https://www.youtube.com/watch?v=crQVIqrJzds)    |
| 5  | 16 Feb 2026  | Asymmetric (Public) Key [[Unit](https://github.com/billbuchanan/appliedcrypto/tree/main/unit04_public_key)]                       | [[Lab](https://github.com/billbuchanan/appliedcrypto/tree/main/unit04_public_key/lab)]    [Len Adleman](https://youtu.be/sPcfQ2tPUb0)                 |
| 6  | 23 Feb 2026  | Key Exchange   [[Unit](https://github.com/billbuchanan/appliedcrypto/tree/main/unit05_key_exchange)]                                | [[Lab](https://github.com/billbuchanan/appliedcrypto/tree/main/unit05_key_exchange/lab)] [Whitfield Diffie](https://www.youtube.com/watch?v=KgkdwtYW-tE)                 |
| 7 | 2 Mar 2026  | Reading Week (Revision lecture)   | Mini-project  [[Here](https://github.com/billbuchanan/appliedcrypto/tree/main/unit06a_mini_project)] /Coursework |
| 8  | 9 Mar 2026   | Digital Signatures and Certificates   [[Unit](https://github.com/billbuchanan/appliedcrypto/tree/main/unit06_trust_dig_cert)]              | [[Lab](https://github.com/billbuchanan/appliedcrypto/tree/main/unit06_trust_dig_cert/lab) ]   
| 9  | 16 Mar 2026  | Test (Units 1-5) 40% of overall mark [[Here](https://github.com/billbuchanan/appliedcrypto/tree/main/z_assessments/test01)] |                                |
| 10 | 23 Mar 2026  | Tunnelling     [[Unit](https://github.com/billbuchanan/appliedcrypto/tree/main/unit07_tunnelling)]                                | [[Lab](https://github.com/billbuchanan/appliedcrypto/tree/main/unit07_tunnelling/lab) Marty Hellman                      |
| 11 | 13 Apr 2026   | Blockchain   [[Unit](https://github.com/billbuchanan/appliedcrypto/tree/main/unit08_blockchain)]                                             | [[Lab](https://github.com/billbuchanan/appliedcrypto/tree/main/unit08_blockchain/lab)] [Troy Hunt](https://us02web.zoom.us/j/87987679833?pwd=SVhMUHRVbXRRQjc0anFTS1UyaGVhQT09)     |
| 12 | 20 Apr 2026  | Future Cryptography  [[Unit](https://github.com/billbuchanan/appliedcrypto/tree/main/unit09_future)]                                  | [[Lab](https://github.com/billbuchanan/appliedcrypto/tree/main/unit09_future/lab)]                            |
| 13 | 27 Apr 2026  | Tokens, Authorization and Docker    [[Unit](https://github.com/billbuchanan/appliedcrypto/tree/main/unit10_services)]                      |    [[Lab](https://github.com/billbuchanan/appliedcrypto/tree/main/unit10_services/lab)]                          |                       |
| 14 | 4 May 2026  | Coursework Hand-in - 60% of overall mark (Sunday, 11 May 2026) [[Coursework](https://github.com/billbuchanan/appliedcrypto/tree/main/z_assessments/coursework)]    |         Daniel J Bernstein 
