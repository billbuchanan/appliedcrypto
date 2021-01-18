
    var Chacha20KeySize = 32;
    var Chacha20NonceSize = 8;
    var Chacha20Ctx = function () {
        this.input = new Array(16);
    };
    function load32(x, i) {
        return x[i] | (x[i + 1] << 8) | (x[i + 2] << 16) | (x[i + 3] << 24);
    }
    function store32(x, i, u) {
        x[i] = u & 0xff; u >>>= 8;
        x[i + 1] = u & 0xff; u >>>= 8;
        x[i + 2] = u & 0xff; u >>>= 8;
        x[i + 3] = u & 0xff;
    }
    function rotl32(v, c) {
        return (v << c) | (v >>> (32 - c));
    }
    function chacha20_round(x, a, b, c, d) {
        x[a] += x[b]; x[d] = rotl32(x[d] ^ x[a], 16);
        x[c] += x[d]; x[b] = rotl32(x[b] ^ x[c], 12);
        x[a] += x[b]; x[d] = rotl32(x[d] ^ x[a], 8);
        x[c] += x[d]; x[b] = rotl32(x[b] ^ x[c], 7);
    }
    function chacha20_init(key, nonce) {
        var x = new Chacha20Ctx();
        x.input[0] = 1634760805;
        x.input[1] = 857760878;
        x.input[2] = 2036477234;
        x.input[3] = 1797285236;
        x.input[12] = 0;
        x.input[13] = 0;
        x.input[14] = load32(nonce, 0);
        x.input[15] = load32(nonce, 4);
        for (var i = 0; i < 8; i++) {
            x.input[i + 4] = load32(key, i * 4);
        }
        return x;
    }
    function chacha20_keystream(ctx, dst, src, len) {
        var x = new Array(16);
        var buf = new Array(64);
        var i = 0, dpos = 0, spos = 0;
        while (len > 0) {
            for (i = 16; i--;) x[i] = ctx.input[i];
            for (i = 20; i > 0; i -= 2) {
                chacha20_round(x, 0, 4, 8, 12);
                chacha20_round(x, 1, 5, 9, 13);
                chacha20_round(x, 2, 6, 10, 14);
                chacha20_round(x, 3, 7, 11, 15);
                chacha20_round(x, 0, 5, 10, 15);
                chacha20_round(x, 1, 6, 11, 12);
                chacha20_round(x, 2, 7, 8, 13);
                chacha20_round(x, 3, 4, 9, 14);
            }
            for (i = 16; i--;) x[i] += ctx.input[i];
            for (i = 16; i--;) store32(buf, 4 * i, x[i]);
            ctx.input[12] += 1;
            if (!ctx.input[12]) {
                ctx.input[13] += 1;
            }
            if (len <= 64) {
                for (i = len; i--;) {
                    dst[i + dpos] = src[i + spos] ^ buf[i];
                }
                return;
            }
            for (i = 64; i--;) {
                dst[i + dpos] = src[i + spos] ^ buf[i];
            }
            len -= 64;
            spos += 64;
            dpos += 64;
        }
    }
