import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from Crypto.Cipher import DES
import Padding

import hashlib
import sys
import binascii

# def aes_encrypt(plaintext,key, mode):
#     method=algorithms.AES(key)
#     cipher = Cipher(method, mode)
#     encryptor = cipher.encryptor()
#     ct = encryptor.update(plaintext) + encryptor.finalize()
#     return(ct)

def aes_decrypt(ciphertext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method, mode)
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)

# def des_encrypt(plaintext, key, mode):
# 	encobj = DES.new(key, mode)
# 	return(encobj.encrypt(plaintext))

# def des_decrypt(ciphertext, key, mode):
#     print('des decrypt')
#     print(f'ciphertext: {ciphertext}, type: {type(ciphertext)}')
#     # print(f'ciphertext: {binascii.unhexlify(ciphertext)}, type: {binascii.unhexlify(type(ciphertext))}')
#     # print(f'ciphertext.decode: {ciphertext.decode()}, type: {type(ciphertext.decode())}')
#     # print(f'binascii.a2b_base64(ciphertext): {binascii.a2b_base64(ciphertext)}, type: {type(binascii.a2b_base64(ciphertext))}')
#     print(f'key: {key}, type: {type(key)}')
#     print(f'mode: {mode}, type: {type(mode)}')
    
#     encobj = DES.new(key, mode)
#     # print(f'encobj: {encobj}, type: {type(encobj)}')
#     # b64_bin = binascii.a2b_base64(ciphertext)
#     # print(f'b64_bin: {b64_bin}, type: {type(b64_bin)}')
#     # decipherd = encobj.decrypt(b64_bin)
#     # print(f'decipherd: {decipherd}, type: {type(decipherd)}')
#     # print('des decrypt')
#     # return()
#     return(encobj.decrypt(ciphertext))

def des_decrypt(ciphertext, key, mode):
    print('des decrypt')
    print(f'ciphertext: {ciphertext}, type: {type(ciphertext)}')
    print(f'key: {key}, type: {type(key)}')
    print(f'mode: {mode}, type: {type(mode)}')
    print('des decrypt')
    encobj = DES.new(key, mode)    
    return(encobj.decrypt(ciphertext))

# def pad(data,size=128):
#     padder = padding.PKCS7(size).padder()
#     padded_data = padder.update(data)
#     padded_data += padder.finalize()
#     return(padded_data)

def unpad(data,size=128):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)

def generate_key(password):
    return hashlib.sha256(password.encode()).digest()

def run_aes_dec(ciphertext, password):
    print("\nAES")

    key = generate_key(password)
    print(f'key: {key}')

    padded_plaintext = aes_decrypt(ciphertext, key, modes.ECB())
    print(f'Padded Plaintext: {padded_plaintext}')

    plaintext = unpad(padded_plaintext)
    print("  decrypt: ",plaintext.decode())

def run_des_dec(ciphertext, password):
    print("\nDES")
    key = hashlib.sha256(password.encode()).digest()[:8]

    plaintext = des_decrypt(ciphertext,key,DES.MODE_ECB)
    print(f'plaintext: {plaintext}, type: {type(plaintext)}')

    plaintext = Padding.removePadding(plaintext.decode(),mode='CMS')
    print("  decrypt: ",plaintext)

    return plaintext

    # # print(f'ciphertext: {ciphertext}, type: {type(ciphertext)}')
    # # print(f'bytes(ciphertext): {bytes(ciphertext)}, type: {type(bytes(ciphertext))}')
    # # print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

    # plaintext = des_decrypt(bytes(ciphertext),key,DES.MODE_ECB)
    # # plaintext = des_decrypt(binascii.hexlify(bytearray(ciphertext)),key,DES.MODE_ECB)
    # print(f'plaintext: {plaintext}, type: {type(plaintext)}')
    # plaintext = unpad(plaintext, size=64)

    # # plaintext = Padding.removePadding(plaintext.decode(),mode='CMS')
    # print("  decrypt: ",plaintext)

def main(argv):
    print(f'argv[0]: {argv[0]}, type: {type(argv[0])}')
    input_ciphertext = bytearray.fromhex(argv[0])
    print(f'input_ciphertext: {input_ciphertext}: bytearray(input_ciphertext)')
    ba_input_ciphertext = bytearray(input_ciphertext)
    print(f'ba_input_ciphertext: {ba_input_ciphertext}, type: {type(ba_input_ciphertext)}')

    ba_input_ciphertext = binascii.unhexlify("0b8bd1e345e7bbf0")

    if (argv[2]== "a"):
        run_aes_dec(ba_input_ciphertext, argv[1])
    elif(argv[2] == "d"):
        run_des_dec(ba_input_ciphertext, argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])
