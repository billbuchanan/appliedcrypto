import rsa
(bob_pub, bob_priv) = rsa.newkeys(512)
ciphertext = rsa.encrypt('Here is my message', bob_pub)
message = rsa.decrypt(ciphertext, bob_priv)
print(message.decode('utf8'))
