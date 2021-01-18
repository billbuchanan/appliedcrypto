var expect = require('chai').expect;
var chacha20 = require('..');


describe('chacha20', function(){

  it('exports an object', function(){
    expect(chacha20).to.be.a('object');
  });

  it('reference tests', function(){
    var key = new Buffer(32);
    key.fill(0);
    var nonce = new Buffer(8);
    nonce.fill(0);
    var data = "\0\0\0\0\0\0\0\0\0"; // 9
    var out = chacha20.encrypt(key, nonce, new Buffer(data));
    expect(out.toString('hex')).to.be.equal("76b8e0ada0f13d9040");
    expect(chacha20.decrypt(key, nonce, out).toString()).to.be.equal(data);

    key.fill(0xff);
    nonce.fill(0xff);
    var ff = new Buffer(9);
    ff.fill(0xff);
    var out = chacha20.encrypt(key, nonce, ff);
    expect(out.toString('hex')).to.be.equal("2640c09431912f4abd");
    expect(chacha20.decrypt(key, nonce, out).toString("hex")).to.be.equal(ff.toString("hex"));
  });

  it('draft tests', function(){
    var key = new Buffer(32);
    key.fill(0);
    var nonce = new Buffer(12);
    nonce.fill(0);
    var data = "\0\0\0\0\0\0\0\0\0"; // 9
    var out = chacha20.encrypt(key, nonce, new Buffer(data));
    expect(out.toString('hex')).to.be.equal("76b8e0ada0f13d9040");
    expect(chacha20.decrypt(key, nonce, out).toString()).to.be.equal(data);

    key.fill(0xff);
    nonce.fill(0xff);
    var ff = new Buffer(9);
    ff.fill(0xff);
    var out = chacha20.encrypt(key, nonce, ff);
    expect(out.toString('hex')).to.be.equal("2919cb6a15012803c4");
    expect(chacha20.decrypt(key, nonce, out).toString("hex")).to.be.equal(ff.toString("hex"));
  });

  it('original tests', function(){
    var Chacha20 = chacha20.Cipher;

    //--------------------------- test -----------------------------//
    function fromHex(h) {
      h = h.replace(/([^0-9a-f])/g, '');
      var out = [], len = h.length, w = '';
      for (var i = 0; i < len; i += 2) {
        w = h[i];
        if (((i+1) >= len) || typeof h[i+1] === 'undefined') {
            w += '0';
        } else {
            w += h[i+1];
        }
        out.push(parseInt(w, 16));
      }
      return out;
    }

    function bytesEqual(a, b) {
      var dif = 0;
      if (a.length !== b.length) return 0;
      for (var i = 0; i < a.length; i++) {
        dif |= (a[i] ^ b[i]);
      }
      dif = (dif - 1) >>> 31;
      return (dif & 1);
    }

    function printHex(num, len, padlen, block) {
      var ret = '', pad = '', i;
      for (i=0; i<padlen;i++) pad += '0';
      i = 0;
      while (i < len) {
        var h = num[i].toString(16);
        ret += (pad + h).slice(-padlen);
        ret += ((i%block) === block-1) ? '\n' : ' ';
        i++;
      }
      console.log(ret);
    }

    function decodeUTF8(s) {
      var i, d = unescape(encodeURIComponent(s)), b = new Uint8Array(d.length);
      for (i = 0; i < d.length; i++) b[i] = d.charCodeAt(i);
      return b;
    }

    function chacha20_block_test() {
      console.log('chacha20 block test');
      var testVectors = [
        {
          key:      '00:01:02:03:04:05:06:07:08:09:0a:0b:0c:0d:0e:0f:10:11:12:13:14:15:16:17:18:19:1a:1b:1c:1d:1e:1f',
          nonce:    '00:00:00:09:00:00:00:4a:00:00:00:00',
          counter:  1,
          expected: '10 f1 e7 e4 d1 3b 59 15 50 0f dd 1f a3 20 71 c4'+
                    'c7 d1 f4 c7 33 c0 68 03 04 22 aa 9a c3 d4 6c 4e'+
                    'd2 82 64 46 07 9f aa 09 14 c2 d7 05 d9 8b 02 a2'+
                    'b5 12 9c d1 de 16 4e b9 cb d0 83 e8 a2 50 3c 4e'
        },
        {
          key:      '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'+
                    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00',
          nonce:    '00 00 00 00 00 00 00 00 00 00 00 00',
          counter:  1,
          expected: '9f 07 e7 be 55 51 38 7a 98 ba 97 7c 73 2d 08 0d'+
                    'cb 0f 29 a0 48 e3 65 69 12 c6 53 3e 32 ee 7a ed'+
                    '29 b7 21 76 9c e6 4e 43 d5 71 33 b0 74 d8 39 d5'+
                    '31 ed 1f 28 51 0a fb 45 ac e1 0a 1f 4b 79 4d 6f'
        },
        {
          key:      '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'+
                    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01',
          nonce:    '00 00 00 00 00 00 00 00 00 00 00 00',
          counter:  1,
          expected: '3a eb 52 24 ec f8 49 92 9b 9d 82 8d b1 ce d4 dd'+
                    '83 20 25 e8 01 8b 81 60 b8 22 84 f3 c9 49 aa 5a'+
                    '8e ca 00 bb b4 a7 3b da d1 92 b5 c4 2f 73 f2 fd'+
                    '4e 27 36 44 c8 b3 61 25 a6 4a dd eb 00 6c 13 a0'
        },
        {
          key:      '00 ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00'+
                    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00',
          nonce:    '00 00 00 00 00 00 00 00 00 00 00 00',
          counter:  2,
          expected: '72 d5 4d fb f1 2e c4 4b 36 26 92 df 94 13 7f 32'+
                    '8f ea 8d a7 39 90 26 5e c1 bb be a1 ae 9a f0 ca'+
                    '13 b2 5a a2 6c b4 a6 48 cb 9b 9d 1b e6 5b 2c 09'+
                    '24 a6 6c 54 d5 45 ec 1b 73 74 f4 87 2e 99 f0 96'
        },
        {
          key:      '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'+
                    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00',
          nonce:    '00 00 00 00 00 00 00 00 00 00 00 02',
          counter:  0,
          expected: 'c2 c6 4d 37 8c d5 36 37 4a e2 04 b9 ef 93 3f cd'+
                    '1a 8b 22 88 b3 df a4 96 72 ab 76 5b 54 ee 27 c7'+
                    '8a 97 0e 0e 95 5c 14 f3 a8 8e 74 1b 97 c2 86 f7'+
                    '5f 8f c2 99 e8 14 83 62 fa 19 8a 39 53 1b ed 6d'
        }
      ];

      for (var i = 0; i < testVectors.length; i++) {
        var key = fromHex(testVectors[i].key),
            nonce = fromHex(testVectors[i].nonce),
            counter = testVectors[i].counter,
            expected = fromHex(testVectors[i].expected),
            len = expected.length,
            output = new Uint8Array(len);

        var ctx = new Chacha20(key, nonce, counter);

        ctx.keystream(output, len);

        if (bytesEqual(output, expected) !== 1) {
          console.log(i, 'ERROR');
        } else {
          console.log(i, 'OK');
        }
      }
    }

    function chacha20_encryption_test() {
      console.log('chacha20 encryption test');
      var testVectors = [
        {
          key:       '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'+
                     '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00',
          nonce:     '00 00 00 00 00 00 00 00 00 00 00 00',
          counter:   0,
          plaintext: '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'+
                     '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'+
                     '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'+
                     '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00',
          expected:  '76 b8 e0 ad a0 f1 3d 90 40 5d 6a e5 53 86 bd 28'+
                     'bd d2 19 b8 a0 8d ed 1a a8 36 ef cc 8b 77 0d c7'+
                     'da 41 59 7c 51 57 48 8d 77 24 e0 3f b8 d8 4a 37'+
                     '6a 43 b8 f4 15 18 a1 1c c3 87 b6 69 b2 ee 65 86'
        },
        {
          key:       '00:01:02:03:04:05:06:07:08:09:0a:0b:0c:0d:0e:0f:10:11:12:13:14:15:16:17:18:19:1a:1b:1c:1d:1e:1f',
          nonce:     '00:00:00:00:00:00:00:4a:00:00:00:00',
          counter:   1,
          plaintext: '4c 61 64 69 65 73 20 61 6e 64 20 47 65 6e 74 6c'+
                     '65 6d 65 6e 20 6f 66 20 74 68 65 20 63 6c 61 73'+
                     '73 20 6f 66 20 27 39 39 3a 20 49 66 20 49 20 63'+
                     '6f 75 6c 64 20 6f 66 66 65 72 20 79 6f 75 20 6f'+
                     '6e 6c 79 20 6f 6e 65 20 74 69 70 20 66 6f 72 20'+
                     '74 68 65 20 66 75 74 75 72 65 2c 20 73 75 6e 73'+
                     '63 72 65 65 6e 20 77 6f 75 6c 64 20 62 65 20 69'+
                     '74 2e',
          expected:  '6e 2e 35 9a 25 68 f9 80 41 ba 07 28 dd 0d 69 81'+
                     'e9 7e 7a ec 1d 43 60 c2 0a 27 af cc fd 9f ae 0b'+
                     'f9 1b 65 c5 52 47 33 ab 8f 59 3d ab cd 62 b3 57'+
                     '16 39 d6 24 e6 51 52 ab 8f 53 0c 35 9f 08 61 d8'+
                     '07 ca 0d bf 50 0d 6a 61 56 a3 8e 08 8a 22 b6 5e'+
                     '52 bc 51 4d 16 cc f8 06 81 8c e9 1a b7 79 37 36'+
                     '5a f9 0b bf 74 a3 5b e6 b4 0b 8e ed f2 78 5e 42'+
                     '87 4d'
        },
        {
          key:       '1c 92 40 a5 eb 55 d3 8a f3 33 88 86 04 f6 b5 f0'+
                     '47 39 17 c1 40 2b 80 09 9d ca 5c bc 20 70 75 c0',
          nonce:     '00 00 00 00 00 00 00 00 00 00 00 02',
          counter:   42,
          plaintext: '27 54 77 61 73 20 62 72 69 6c 6c 69 67 2c 20 61'+
                     '6e 64 20 74 68 65 20 73 6c 69 74 68 79 20 74 6f'+
                     '76 65 73 0a 44 69 64 20 67 79 72 65 20 61 6e 64'+
                     '20 67 69 6d 62 6c 65 20 69 6e 20 74 68 65 20 77'+
                     '61 62 65 3a 0a 41 6c 6c 20 6d 69 6d 73 79 20 77'+
                     '65 72 65 20 74 68 65 20 62 6f 72 6f 67 6f 76 65'+
                     '73 2c 0a 41 6e 64 20 74 68 65 20 6d 6f 6d 65 20'+
                     '72 61 74 68 73 20 6f 75 74 67 72 61 62 65 2e',
          expected:  '62 e6 34 7f 95 ed 87 a4 5f fa e7 42 6f 27 a1 df'+
                     '5f b6 91 10 04 4c 0d 73 11 8e ff a9 5b 01 e5 cf'+
                     '16 6d 3d f2 d7 21 ca f9 b2 1e 5f b1 4c 61 68 71'+
                     'fd 84 c5 4f 9d 65 b2 83 19 6c 7f e4 f6 05 53 eb'+
                     'f3 9c 64 02 c4 22 34 e3 2a 35 6b 3e 76 43 12 a6'+
                     '1a 55 32 05 57 16 ea d6 96 25 68 f8 7d 3f 3f 77'+
                     '04 c6 a8 d1 bc d1 bf 4d 50 d6 15 4b 6d a7 31 b1'+
                     '87 b5 8d fd 72 8a fa 36 75 7a 79 7a c1 88 d1'
        },
      ];

      for (var i = 0; i < testVectors.length; i++) {
        var key = fromHex(testVectors[i].key),
            nonce = fromHex(testVectors[i].nonce),
            counter = testVectors[i].counter,
            plaintext = fromHex(testVectors[i].plaintext),
            expected = fromHex(testVectors[i].expected),
            len = plaintext.length,
            buf = new Uint8Array(len),
            output = new Uint8Array(len);

        var ctx = new Chacha20(key, nonce, counter);

        ctx.keystream(buf, len);

        for (var j = 0; j < len; j++) {
          output[j] = buf[j] ^ plaintext[j];
        }

        if (bytesEqual(output, expected) !== 1) {
          console.log(i, 'ERROR');
        } else {
          console.log(i, 'OK');
        }
      }
    }

    chacha20_block_test();
    chacha20_encryption_test();
  });

});