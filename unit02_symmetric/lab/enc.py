from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding
from Crypto.Cipher import DES
import Padding

import hashlib
import sys
import binascii

def aes_encrypt(plaintext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method, mode)
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext) + encryptor.finalize()
    return(ct)

def aes_decrypt(ciphertext,key, mode):
    method=algorithms.AES(key)
    cipher = Cipher(method, mode)
    decryptor = cipher.decryptor()
    pl = decryptor.update(ciphertext) + decryptor.finalize()
    return(pl)

def des_encrypt(plaintext, key, mode):
	encobj = DES.new(key, mode)
	return(encobj.encrypt(plaintext))

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

def unpad(data,size=128):
    padder = padding.PKCS7(size).unpadder()
    unpadded_data = padder.update(data)
    unpadded_data += padder.finalize()
    return(unpadded_data)

def generate_key(password):
    return hashlib.sha256(password.encode()).digest()

def pad_plaintext(plaintext):
    return pad(plaintext.encode())

def run_aes_enc(text, password):
    print("\nAES")

    padded_plaintext = pad_plaintext(text)
    print(f'padded_plaintext: {padded_plaintext}')
    
    encoded_padded_plaintext = binascii.hexlify(bytearray(padded_plaintext))
    print(f'encoded_padded_plaintext: {encoded_padded_plaintext}, type: {type(encoded_padded_plaintext)}')
    
    print("After padding (CMS): ",)

    key = generate_key(password)
    print(f'key: {key}')

    ciphertext = aes_encrypt(padded_plaintext, key, modes.ECB())
    print(f'ciphertext: {ciphertext}, type: {type(ciphertext)}')
    print(f'Cipher (ECB): {binascii.hexlify(bytearray(ciphertext))}, type: {type(binascii.hexlify(bytearray(ciphertext)))}')

    padded_plaintext = aes_decrypt(ciphertext, key, modes.ECB())
    # print(f'Padded Plaintext: {padded_plaintext}')

    plaintext = unpad(padded_plaintext)
    print("  decrypt: ",plaintext.decode())

def run_des_enc(text, password):
    print(f'\nDES: text: {text}')
    key = hashlib.sha256(password.encode()).digest()[:8]

    plaintext = Padding.appendPadding(text,blocksize=Padding.DES_blocksize,mode='CMS')
    print(f'plaintext: {plaintext}, type: {type(plaintext)}')

    encoded_plaintext = binascii.hexlify(bytearray(plaintext.encode()))
    print(f"After padding (CMS): {encoded_plaintext}, type: {type(encoded_plaintext)}")

    ciphertext = des_encrypt(plaintext.encode(),key,DES.MODE_ECB)
    print(f'ciphertext: {ciphertext}, type: {type(ciphertext)}')
    print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

    plaintext = des_decrypt(ciphertext,key,DES.MODE_ECB)
    print(f'plaintext: {plaintext}, type: {type(plaintext)}')

    plaintext = Padding.removePadding(plaintext.decode(),mode='CMS')
    print("  decrypt: ",plaintext)

def main(argv):
    if (argv[2] == "a"):
        run_aes_enc(argv[0], argv[1])
    elif (argv[2] == "d"):
        run_des_enc(argv[0], argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])
