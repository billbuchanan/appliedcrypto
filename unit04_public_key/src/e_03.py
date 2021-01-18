from Crypto.PublicKey import RSA

key = RSA.generate(2048)

binPrivKey = key.exportKey('PEM')
binPubKey =  key.publickey().exportKey('PEM')

print binPrivKey
print binPubKey
