# https://asecuritysite.com/encryption/rsa12_2
from Crypto.Util.number import long_to_bytes
import libnum
import sys

p=954354002755510667
q=801297755486859913
# c=607778777406675887172756406181993732
c=850431005415590313843011081245086829
#N=764721720347891218098402268606191971
N=879509040449463763008386484793372267

if (len(sys.argv)>1):
        c=int(sys.argv[1])
if (len(sys.argv)>2):
        p=int(sys.argv[2])
if (len(sys.argv)>3):
        q=int(sys.argv[3])

n = p*q
PHI=(p-1)*(q-1)

e=65537
d=(libnum.invmod(e, PHI))


res=pow(c,d, n)

print ("Cipher: ",c)
print ("p: ",p)
print ("q: ",q)

print ("\n=== Calc ===")
print ("d=",d)
print ("n=",n)
print(f'res: {res}')
print ("Decrypt: %s" % ((long_to_bytes(res))))


