aes
===

A JavaScript component for the [Advanced Encryption Standard (AES)](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard). Fully compatible with Node.js and the browser (via Browserify).

(Note, more optimizations may need to be made)


Why?
----

AES is currently one of the most popular block ciper encyrption algorithms. It is relevant to the Bitcoin private key encryption scheme [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki).


Usage
-----

### Installation

    npm install --save aes


### Example

Note, that as version 0.1.x, you must be concerned with the endianess of your input data. It expects that the `key` is a regular JavaScript array of 4,6,8 or 32-bit unsigned values. The encrypt function is a regular JavaScript array of 4 32-bit big endian unsigned integers.

```js
var AES = require('aes')

var key = [0xffffffff,0xffffffff,0xffffffff,0xffffffff,0xffffffff,0xfffffff8];
var pt = [0x00000000,0x00000000,0x00000000,0x00000000];
var ct = [0xd241aab0,0x5a42d319,0xde81d874,0xf5c7b90d];

var aes = new AES(key);
console.dir(aes.encrypt(pt)); // => [0xd241aab0,0x5a42d319,0xde81d874,0xf5c7b90d]
console.dir(aes.decrypt(ct)); // => [0x00000000,0x00000000,0x00000000,0x00000000]
``` 

### Testing

1. Clone the git repo.
2. `npm install --development`

#### Node.js

    Make node-test

#### Browser

    npm install --production selenium-standalone -g start-selenium

(source your shell or open a new one), edit file `.min-wd`

    start-selenium
    Make browser-test


### Bundle for Browser

    npm install -g browserify
    browserify < lib/aes.js > lib/aes.bundle.js


References
----------
- https://code.google.com/p/crypto-js/source/browse/tags/3.1.2/src/aes.js
- https://github.com/bitwiseshiftleft/sjcl/blob/master/core/aes.js
- https://github.com/mdp/gibberish-aes
- http://en.wikipedia.org/wiki/Advanced_Encryption_Standard
- http://www.differencebetween.com/difference-between-stream-cipher-and-vs-block-cipher/
- http://en.wikipedia.org/wiki/Cipher_block_chaining
- http://opensource.apple.com/source/OpenSSL/OpenSSL-46/openssl/crypto/aes/aes_core.c



Credits
-------

Extracted from the [Stanford JavaScript Crypto Library](https://github.com/bitwiseshiftleft/sjcl).


License
-------

BSD License

