import sys
import random

n=101
g= 3

ans=7

x = 3
y = 4

E1= g**( (x+y) % (n-1)) % n

E2= (g**x * g**y) % n

E3 = g**(ans) % n

print '======Agreed parameters============'
print 'P=',n,'\t(Prime number)'
print 'G=',g,'\t(Generator)'
print 'x=',x,'\t(Value 1 - Alice first value)'
print 'y=',y,'\t(value 2 - Alice second value)'
print 'ans=',ans,'\t(Answer = x+y?)'

print '======Encrypted values============'
print 'g^x=',(g**x) % n
print 'g^y=',(g**y) % n

print '======zkSnark===================='
print 'E1=',E1
print 'E2=',E2
print 'E3=',E3
if (E2==E3):
	print 'Alice has proven she knows the sum is ',ans
else:
	print 'Alice has proven she does not know the sum is ',ans
    