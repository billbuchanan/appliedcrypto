import sys
import random

n=101

g= 3

x = random.randint(5,10)
v = random.randint(100,150)
c = random.randint(5,10)

y= g**x % n

t = g**v % n

r = v - c * x

Result = ( (g**r) * (y**c) ) % n


print 'x=',x
print 'c=',c
print 'v=',v
print 'P=',n
print 'G=',g
print '======'
print 't=',t
print 'r=',Result
if (t==Result):
	print 'Alice has proven she knows x'
else:
	print 'Alice has not proven she knows x'