var crypto = require("crypto");


function showhash(password, type)
{
	hash = crypto.createHash(type);
	hash.update(password);
	console.log(type,"\t",hash.digest('hex'));
}


var data = "hello";

const args = process.argv.slice(3);
console.log("Data:\t",data);

data = args[0];
console.log("Data:\t",data+"\n");

showhash(data,'DSA');
showhash(data,'DSA-SHA');
showhash(data,'DSA-SHA1');
showhash(data,'DSA-SHA1-old');
showhash(data,'RSA-MD4');
showhash(data,'RSA-MD5');
showhash(data,'RSA-MDC2');
showhash(data,'RSA-RIPEMD160');
showhash(data,'RSA-SHA');
showhash(data,'RSA-SHA1');
showhash(data,'RSA-SHA1-2');
showhash(data,'RSA-SHA224');
showhash(data,'RSA-SHA256');
showhash(data,'RSA-SHA384');
showhash(data,'RSA-SHA512');
showhash(data,'dsaEncryption');
showhash(data,'dsaWithSHA');
showhash(data,'dsaWithSHA1');
showhash(data,'dss1');
showhash(data,'ecdsa-with-SHA1');
showhash(data,'md4');
showhash(data,'md4WithRSAEncryption');
showhash(data,'md5');
showhash(data,'md5WithRSAEncryption');
showhash(data,'mdc2');
showhash(data,'mdc2WithRSA');
showhash(data,'ripemd');
showhash(data,'ripemd160');
showhash(data,'ripemd160WithRSA');
showhash(data,'rmd160');
showhash(data,'sha');
showhash(data,'sha1');
showhash(data,'sha1WithRSAEncryption');
showhash(data,'sha224');
showhash(data,'sha224WithRSAEncryption');
showhash(data,'sha256');
showhash(data,'sha256WithRSAEncryption');
showhash(data,'sha384');
showhash(data,'sha384WithRSAEncryption');
showhash(data,'sha512');
showhash(data,'sha512WithRSAEncryption');
showhash(data,'shaWithRSAEncryption');
showhash(data,'ssl2-md5');
showhash(data,'ssl3-md5');
showhash(data,'ssl3-sha1');
showhash(data,'whirlpool');