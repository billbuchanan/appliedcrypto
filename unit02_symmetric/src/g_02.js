// RC4

var crypto = require('crypto');

var keyname="test";
var plaintext = "testing";

var args = process.argv;
if (args.length>1) plaintext=args[2];
if (args.length>2) keyname=args[3];

var key = crypto.createHash('sha256').update(keyname).digest();

var cipher = crypto.createCipheriv('rc4', key,'' );
var ciphertext = cipher.update( plaintext, 'utf8', 'hex');
console.log("Ciphertext:\t",ciphertext);


var decipher = crypto.createDecipheriv('rc4', key,'' );
var text = decipher.update( ciphertext, 'hex','utf8');
console.log("Decipher:\t",text);
