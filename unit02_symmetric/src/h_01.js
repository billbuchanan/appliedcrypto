var crypto = require("crypto");


function encryptText(algor, key, iv, text, encoding) {

        var cipher = crypto.createCipheriv(algor, key, iv);

        encoding = encoding || "binary";

        var result = cipher.update(text, "utf8", encoding);
        result += cipher.final(encoding);

        return result;
    }

function decryptText(algor, key, iv, text, encoding) {

        var decipher = crypto.createDecipheriv(algor, key, iv);

        encoding = encoding || "binary";

        var result = decipher.update(text, encoding);
        result += decipher.final();

        return result;
    }


var data = "This is a test";
var password = "hello";
var algorithm = "aes256"

//const args = process.argv.slice(3);

//data = args[0];
//password = args[1];
//algorithm = args[2];

console.log("\nText:\t\t" + data);
console.log("Password:\t" + password);
console.log("Type:\t\t" + algorithm);

var hash,key;

if (algorithm.includes("256"))
{
	hash = crypto.createHash('sha256');
        hash.update(password);



	key = new Buffer.alloc(32,hash.digest('hex'),'hex');
}
else if (algorithm.includes("192"))
{
	hash = crypto.createHash('sha192');
        hash.update(password);

	key = new Buffer.alloc(24,hash.digest('hex'),'hex');
}

else if (algorithm.includes("128"))
{
	hash = crypto.createHash('md5');
        hash.update(password);

	key = new Buffer.alloc(16,hash.digest('hex'),'hex');
}


const iv=new Buffer.alloc(16,crypto.pseudoRandomBytes(16));

console.log("Key:\t\t"+key.toString('base64'));
console.log("Salt:\t\t"+iv.toString('base64'));

var encText = encryptText(algorithm, key, iv, data, "base64");

console.log("\n================");

console.log("\nEncrypted:\t" + encText);

var decText = decryptText(algorithm, key, iv, encText, "base64");

console.log("\nDecrypted:\t" + decText);
