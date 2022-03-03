from Crypto.Cipher import AES

import hashlib
import sys
import binascii
import base64
import Padding

plaintext='Hello'
key='qwerty'
salt='241fa86763b85341'

if (len(sys.argv)>1):
        plaintext=str(sys.argv[1])
if (len(sys.argv)>2):
        key=str(sys.argv[2])
if (len(sys.argv)>3):
        salt=str(sys.argv[3])

def get_key_and_iv(password, salt, klen=32, ilen=16, msgdgst='md5'):

    mdf = getattr(__import__('hashlib', fromlist=[msgdgst]), msgdgst)
    password = password.encode('ascii', 'ignore')  # convert to ASCII

    try:
        maxlen = klen + ilen
        keyiv = mdf(password + salt).digest()
        tmp = [keyiv]
        while len(tmp) < maxlen:
            tmp.append( mdf(tmp[-1] + password + salt).digest() )
            keyiv += tmp[-1]  # append the last byte
        key = keyiv[:klen]
        iv = keyiv[klen:klen+ilen]
        return key, iv
    except UnicodeDecodeError:
         return None, None

def encrypt(plaintext,key, mode,salt):
	key,iv=get_key_and_iv(key,salt.decode('hex'))
	
	encobj = AES.new(key,mode,iv)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode,salt):
        key,iv=get_key_and_iv(key,salt.decode('hex'))
	encobj = AES.new(key,mode,iv)
	return(encobj.decrypt(ciphertext))

print "Plaintext:\t",plaintext
print "Passphrase:\t",key
print "Salt:\t\t",salt
plaintext = Padding.appendPadding(plaintext,mode='CMS')

ciphertext = encrypt(plaintext,key,AES.MODE_CBC,salt)

ctext = b'Salted__' + salt.decode('hex') + ciphertext


print "\nCipher (CBC): "+base64.b64encode(ctext)
print "Cipher in binary:",ctext

plaintext = decrypt(ciphertext,key,AES.MODE_CBC,salt)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print "\nDecrypted:\t"+plaintext
