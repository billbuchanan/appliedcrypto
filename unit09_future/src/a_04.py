import sys
import random

n=101
g= 3

x=5

a = 3
b = 4

# eqn = ax + b x^2


E1= g**( a *x ) % n

E2= g**(b*x*x) % n

E3 = (E1 * E2) % n
E4 = g**(a*x + b*x*x) % n



print '======Agreed parameters============'
print 'P=',n,'\t(Prime number)'
print 'G=',g,'\t(Generator)'
print 'a=',a
print 'b=',b
print 'x=',x,'\t(Eqn= ax + bx^2)'


print '======zkSnark===================='

print 'E3=',E3
print 'E4=',E4

if (E3==E4):
	print 'Alice has computed the result'
else:
	print 'Alice has proven she does not know result'