Pure javascript implementation of [ChaCha20](http://cr.yp.to/chacha.html) originally written by [@devi](https://github.com/devi/chacha20poly1305) supporting [draft-irtf-cfrg-chacha20-poly1305-01](https://tools.ietf.org/html/draft-irtf-cfrg-chacha20-poly1305-01).

Being packaged here as a simple node.js and browserify module.

## Usage

````
var chacha20 = require("chacha20");

var key = new Buffer(32);
key.fill(0);
var nonce = new Buffer(8);
nonce.fill(0);

var plaintext = "testing";
// pass in buffers, returns a buffer
var ciphertext = chacha20.encrypt(key, nonce, new Buffer(plaintext));
console.log(ciphertext.toString("hex")); // prints "02dd93d9c99f5a"
console.log(chacha20.decrypt(key, nonce, ciphertext).toString()); // prints "testing"
````

## Nonce Size

The handling of the nonce differs between the [reference](http://cr.yp.to/chacha.html) and [IETF Draft](https://tools.ietf.org/html/draft-irtf-cfrg-chacha20-poly1305-01#section-2.3), where the reference uses an 8-byte nonce and the draft uses a 12-byte one with the first 4 bytes being a `sender` unique identifier.  Passing a difference nonce buffer size will choose either mode.