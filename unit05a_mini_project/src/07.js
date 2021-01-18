// Node.js example Run with:
// node crypto.js message password

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
if (args.length>2) message=args[2];
if (args.length>3) password=args[3];

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

console.log("\n--- AES");
var ciphertext = AES.encrypt(message, password);
 
var ciphertext = CryptoJS.AES.encrypt(message, password,mode=CryptoJS.mode.ECB);

var bytes  = CryptoJS.AES.decrypt(ciphertext.toString(), password,mode=CryptoJS.mode.ECB);

var plaintext = bytes.toString(CryptoJS.enc.Utf8);
 
console.log("Cipher: ",ciphertext.toString());
console.log("Plaintext: ",plaintext);

console.log("\n--- HMAC-SHA1");
console.log("HMAC: ",CryptoJS.HmacSHA1(message, password).toString());

