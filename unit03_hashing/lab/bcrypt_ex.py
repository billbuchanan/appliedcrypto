
import bcrypt
from time import time

salt="ZDzPE45C"
string="the boy stood on the burning deck"
pt="hello"

def bcrypt_ex(salt, pt, rounds):
    return bcrypt.kdf(pt.encode(),
                    salt=salt.encode(),
                    desired_key_bytes=32,
                    rounds=rounds).hex()

for i in range(49, 1000):
    start_time = time()
    key = bcrypt_ex(salt, pt, i)
    print(f'rounds: {i}, key: {key}, time: {time() - start_time} secs')
