![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Unit 5: Key Exchange
The key concepts are: Basics of Key Exchange; Diffie-Hellman, Diffie-Hellman Weaknesses, ECDH, and Passing Key Using Public Key.
What you should know at the end of unit?

* Understand how the Diffie-Hellman process works, with a simple example
* Understands how the private key is used to check the identity of the sender, and how public key is used to preserve the privacy of the message.
* Understand the basics of how Bob and Alice generate a shared key with ECC.

## Presentations

* Week 5 Presentation (lecture - Part 1) - Key Exchange: [here](https://youtu.be/l_osjo8r13Q)
* Week 5 Presentation (lecture - Part 2) - Key Exchange: [here](https://youtu.be/95AuvZNm0Yg)
* Week 5 Presentation (PDF) - Key Exchange: [here](https://asecuritysite.com/public/unit05_key_exchange.pdf)
* Week 5 Presentation (class lecture) - Key Exchange (Recorded 14 Feb 2020): [here](https://youtu.be/WIkDh_5198M)

## Lab

* Week 5 Lab (PDF): [here](https://github.com/billbuchanan/esecurity/blob/master/unit05_key_exchange/lab/new_lab05.pdf)
* Week 5 Lab (Demo): [here](https://www.youtube.com/watch?v=Lnw4FhiOwiU&feature=youtu.be)

## Sample Exam Questions

The following are sample questions for key exchange:

* Eve listens to Bob and Alice's communcication for their Diffie-Hellman handshaking. In order to generate the same key as Bob and Alice, which values will Eve try to determine, and how is it likely to be difficult to gain these?
* For the following key exchanges, Bob generates x, and Alice generates y. Prove the shared key. [Examples](https://asecuritysite.com/public/diffie_examples.pdf)
  * x=3, y=4, G=4 and N=7. Share=1.
  * x=6, y=15, G=5 and N=23. Share=2.
  * x=5, y=7, G=10 and N=541. Share=193.
  * x=6, y=15, G=5 and N=23. Share=2.
  * x=7, y=7, G=5 and N=11. Share=9.
  * x=7, y=9, G=8 and N=13. Share=5.
  * x=5, y=4, G=2969 and N=9929. Share=8106.
  * x=6, y=5, G=3881 and N=125. Share=792.
  * x=3, y=4, G=3623 and N=1153. Share=939.
* Why are Forward Security and Ephemeral so important for the security of your keys?

## Examples

* Diffie-Hellman Examples: [here](https://asecuritysite.com/public/diffie_examples.pdf)
* ECDH Step-by-step: [here](https://asecuritysite.com/encryption/js08)

## Quick demos

* Introduction to Diffie-Hellman: [here](https://www.youtube.com/watch?v=wyNPhNAsmJ0)
* ECDH [here](https://youtu.be/uQQz3MX-d8I)
* Picking the Generator Value (G): [here](https://www.youtube.com/watch?v=-TjSuch3VGU)

## Any questions?

Slackspace: esecurity2020.slack.com
