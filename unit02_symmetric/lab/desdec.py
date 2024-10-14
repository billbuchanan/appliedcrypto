from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from Crypto.Cipher import DES
import Padding

import hashlib
import sys
import binascii

def des_decrypt(ciphertext, key, mode):
    print('des decrypt')
    print(f'ciphertext: {ciphertext}, type: {type(ciphertext)}')
    print(f'key: {key}, type: {type(key)}')
    print(f'mode: {mode}, type: {type(mode)}')
    print('des decrypt')
    encobj = DES.new(key, mode)    
    return(encobj.decrypt(ciphertext))

def pad(data,size=128):
    padder = padding.PKCS7(size).padder()
    padded_data = padder.update(data)
    padded_data += padder.finalize()
    return(padded_data)

# def unpad(data,size=128):
def unpad(data,size=256):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)

def generate_key(password):
    return hashlib.sha256(password.encode()).digest()

def pad_plaintext(plaintext):
    return pad(plaintext.encode())

def run_des_enc(ciphertext, password):
    print(f'\nDES: ciphertext: {ciphertext}, type: {type(ciphertext)}')
    key = hashlib.sha256(password.encode()).digest()[:8]

    # plaintext = Padding.appendPadding(text,blocksize=Padding.DES_blocksize,mode='CMS')
    # print(f'plaintext: {plaintext}, type: {type(plaintext)}')

    # encoded_plaintext = binascii.hexlify(bytearray(plaintext.encode()))
    # print(f"After padding (CMS): {encoded_plaintext}, type: {type(encoded_plaintext)}")

    # ciphertext = binascii.a2b_base64(ciphertext)
    # ciphertext = binascii.a2b_hex(ciphertext)
    # ciphertext = binascii.b2a_hex(bytearray(ciphertext, 'utf8'))
    
    # ciphertext = binascii.unhexlify(ciphertext)
    
    # ciphertext = binascii.hexlify(bytearray(ciphertext, 'ascii'))
    # ciphertext = binascii.a2b_base64(bytearray(ciphertext, 'ascii'))
    ciphertext = binascii.a2b_hex(bytearray(ciphertext, 'ascii'))
    # ciphertext = binascii.b2a_hex(bytearray(ciphertext, 'ascii'))
    # ciphertext = binascii.unhexlify(bytearray(ciphertext, 'ascii'))
    
    print(f'ciphertext: {ciphertext}, type: {type(ciphertext)}')
    # print("Cipher (ECB): ", binascii.hexlify(bytearray(ciphertext)))

    plaintext = des_decrypt(ciphertext,key,DES.MODE_ECB)
    print(f'plaintext: {plaintext}, type: {type(plaintext)}')

    # plaintext = unpad(plaintext)

    # plaintext = Padding.removePadding(plaintext.decode(),mode='CMS')
    print("  decrypt: ",plaintext)

def main(argv):
    run_des_enc(str.strip(argv[0]), str.strip(argv[1]))

if __name__ == "__main__":
    main(sys.argv[1:])
