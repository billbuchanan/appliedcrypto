import rsa
(bob_pub, bob_priv) = rsa.newkeys(512)

print (bob_pub)
print (bob_priv)

msg='Here is my message'
ciphertext = rsa.encrypt(msg.encode(), bob_pub)
message = rsa.decrypt(ciphertext, bob_priv)
print(message.decode('utf8'))
