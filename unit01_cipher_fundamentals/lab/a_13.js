// Run as node a_13.js Hello zip
// If you want to "Deflate" (compress) using the argument of "zip"

var zlib = require('zlib');
var test="hello";

// var flag="zip"
var flag=""

var args = process.argv;
if (args.length>1) test=args[2];
if (args.length>2) flag=args[3];

console.log("Input: ",test);

// if (flag=="zip") {
	var input = new Buffer.from(test)
	zlib.deflate(input, function(err, buf) {
		var res=buf.toString('base64');
    	console.log("Compressed: " ,res );	
	});
// }
// else {
// 	var input = new Buffer.from(test,'base64')
// 	zlib.inflate(input, function(err, buf) {
// 		if (buf==undefined) console.log("Incorrect format in processing Base64!");
//     		else console.log("Uncompressed:", buf.toString("utf8") );
// 	});
// } 