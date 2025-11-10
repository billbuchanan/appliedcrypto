import hmac as hmc
import hashlib
import binascii
from cryptography.hazmat.primitives import hashes, hmac

pt = "Hello"
pt_hx = binascii.hexlify(bytearray(pt.encode()))
key = "qwerty123"
key_hx = binascii.hexlify(bytearray(key.encode()))


def show_hash(name,type,data,key):
    digest = hmac.HMAC(key, type,)
    digest.update(data)
    res=digest.finalize()
    res_hx=binascii.b2a_hex(res).decode()
    res_b64=binascii.b2a_base64(res).decode()
    print (f"HMAC-{name}: {res_hx} {res_b64}")

dg_hx = hmc.digest(key=key_hx, msg=pt_hx, digest=hashlib.md5)
nw_hx = hmc.new(key=key_hx, msg=pt_hx, digestmod=hashlib.md5)

dg = hashlib.md5(dg_hx).hexdigest()
nw = nw_hx.hexdigest()
 
print(f'pt: {pt}, pt_hx: {pt_hx}\nKey: {key}, key_hx: {key_hx}\ndg_hx: {dg_hx}\ndg: {dg}\nnw_hx: {nw_hx}\nnw: {nw}')

show_hash("MD5", hashes.MD5(), pt.encode(), key.encode())
show_hash("SHA1", hashes.SHA1(), pt.encode(), key.encode())
show_hash("SHA256", hashes.SHA256(), pt.encode(), key.encode())
show_hash("SHA512", hashes.SHA512(), pt.encode(), key.encode())
show_hash("BLAKE2b", hashes.BLAKE2b(digest_size=64), pt.encode(), key.encode())
show_hash("BLAKE2s", hashes.BLAKE2s(digest_size=32), pt.encode(), key.encode())
