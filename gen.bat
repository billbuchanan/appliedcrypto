openssl ecparam -name secp256k1 -genkey -out alice_private.pem
openssl ec -in alice_private.pem -pubout -out alice_public.pem

openssl ecparam -name secp256k1 -genkey -out bob_private.pem 
openssl ec -in bob_private.pem -pubout -out bob_public.pem

openssl pkeyutl -derive -inkey alice_private.pem -peerkey bob_public.pem -out shared_secret.bin
openssl pkeyutl -derive -inkey bob_private.pem -peerkey alice_public.pem -out shared_secret2.bin
xxd shared_secret.bin
xxd shared_secret2.bin
