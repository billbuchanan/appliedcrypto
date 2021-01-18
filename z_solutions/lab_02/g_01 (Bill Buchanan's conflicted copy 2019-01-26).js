var chacha20 = require("chacha20");
var crypto = require("crypto")


var keyname = "test";
var ciphertext ="testing"

var args = process.argv;

if(args.length > 1) ciphertext=args[2]
if(args.length > 2) keyname=args[3]

console.log("Args", args[2], args[3])

console.log(keyname, ciphertext)
var key = crypto.createHash('sha256').update(keyname).digest();

var nonce = new Buffer.alloc(8)
nonce.fill(0)

console.log(key)
console.log("Decypher:", chacha20.decrypt(key, nonce, new Buffer.from(ciphertext, 'hex')).toString())