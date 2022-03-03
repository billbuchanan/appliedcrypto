var crypto = require('crypto');

var key = 'qwerty';
var message = 'Hello';

var hash = crypto.createHmac('md5', key).update(message);

console.log(hash.digest('hex'));
console.log(hash.digest('base64'));

