var args = process.argv;
var sec='fff';

var pay="{ foo: \'bar\'}";

if (args.length>1) pay=args[2];
if (args.length>2) sec=args[3];

console.log("Message:\t",pay)
console.log("Passphrase:\t",sec)

var jwt = require('jwt-simple');
var payload = pay  ;
var secret = sec;


// encode
var token = jwt.encode(payload, secret);
console.log("Token: ",token);
// decode
var decoded = jwt.decode(token, secret);
console.log("Decoded: ",decoded); 

