# Zero-knowledge proof (discrete logs).
# https://asecuritysite.com/encryption/z

import sys

p=71
g=13
x=7
r=8

print 'p=',p
print 'g=',g
print 'x=',x
print 'r=',r
print '========'

y= g**x % p

print 'Y=',y

C = g**r % p
print 'C=',C

print '========'
val1=g**((x+r)%(p-1))  % p
print 'g^(x+r)%(p-1) mod p=',val1

val2=C*y %p
print 'C.y mod P=',val2

if (val1==val2):
	print 'Well done ... have you proven that you know x'
else:
	print 'Not proven'