const openpgp = require('openpgp') 
var name1='bill';
var email1='bill@home.com';

var args = process.argv;
if (args.length>1) name=args[2];
if (args.length>2) email=args[3];

openpgp.initWorker({ path:'openpgp.worker.js' }) // set the relative web worker path
 
var options = {
    userIds: [{ name:name1, email:email1 }], // multiple user IDs
    numBits: 512,                                            // RSA key size
    passphrase: 'password'         // protects the private key
};

openpgp.generateKey(options).then(function(key) {
    var privkey = key.privateKeyArmored; // '-----BEGIN PGP PRIVATE KEY BLOCK ... '
    var pubkey = key.publicKeyArmored;   // '-----BEGIN PGP PUBLIC KEY BLOCK ... '
    var revocationCertificate = key.revocationCertificate; // '-----BEGIN PGP PUBLIC KEY BLOCK ... '

    console.log(pubkey);
    console.log(privkey);

});
