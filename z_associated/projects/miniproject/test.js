var CryptoJS = require("crypto-js");
 
// Encrypt
var ciphertext = CryptoJS.AES.encrypt('my message', 'secret key 123');
 
// Decrypt
var bytes  = CryptoJS.AES.decrypt(ciphertext.toString(), 'secret key 123');
var plaintext = bytes.toString(CryptoJS.enc.Utf8);
 
console.log(plaintext);
