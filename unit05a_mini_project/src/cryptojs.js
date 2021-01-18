// Node.js example Run with:
// node crypto.js

message ="Hello"
password="qwerty"

var SHA256 = require("crypto-js/sha256");
var MD5 = require("crypto-js/md5");
var SHA3 = require("crypto-js/sha3");
var SHA1 = require("crypto-js/sha1");
var SHA224 = require("crypto-js/sha224");
var SHA512 = require("crypto-js/sha512");
var SHA384 = require("crypto-js/sha384");
var RIP = require("crypto-js/ripemd160");
var AES = require("crypto-js/aes");

var CryptoJS = require("crypto-js");

var args = process.argv;
if (args.length>1) message=args[2];
if (args.length>2) password=args[3];

console.log("Message: ",message);
console.log("Password: ",password);

console.log("\n--- Hashes");
console.log("MD5: ",MD5(message).toString());
console.log("SHA-256: ",SHA256(message).toString());
console.log("SHA-1: ",SHA1(message).toString());
console.log("SHA-224: ",SHA224(message).toString());
console.log("SHA-512: ",SHA512(message).toString());
console.log("SHA-384: ",SHA384(message).toString());
console.log("ripemd160: ",RIP(message).toString());
//    To do:
//    crypto-js/sha1
//    crypto-js/sha256
//    crypto-js/sha224
//    crypto-js/sha512
//    crypto-js/sha384
//    crypto-js/ripemd160


console.log("\n--- AES");
var ciphertext = AES.encrypt(message, password);
 
var bytes  = AES.decrypt(ciphertext.toString(), password);
var plaintext = bytes.toString(CryptoJS.enc.Utf8);
 
console.log("Cipher: ",ciphertext.toString());
console.log("Plaintext: ",plaintext);

// To do:
//   crypto-js/tripledes
//   crypto-js/rc4
//   crypto-js/rabbit
//   crypto-js/evpkdf


console.log("\n--- HMAC-SHA1");
console.log("HMAC: ",CryptoJS.HmacSHA1(message, password).toString());

//  To do:
//    crypto-js/hmac-md5
//    crypto-js/hmac-sha256
//    crypto-js/hmac-sha224
//    crypto-js/hmac-sha512
//    crypto-js/hmac-sha384
//    crypto-js/hmac-sha3
//    crypto-js/hmac-ripemd160



// Padding to do:
//    crypto-js/pad-pkcs7
//    crypto-js/pad-ansix923
//    crypto-js/pad-iso10126
//    crypto-js/pad-iso97971
//    crypto-js/pad-zeropadding
//    crypto-js/pad-nopadding


// Formats to do:

//    crypto-js/enc-latin1
//    crypto-js/enc-utf8
//    crypto-js/enc-hex
//    crypto-js/enc-utf16
//    crypto-js/enc-base64


// Modes to do:

//     crypto-js/mode-cfb
//     crypto-js/mode-ctr
//     crypto-js/mode-ctr-gladman
//     crypto-js/mode-ofb
//     crypto-js/mode-ecb