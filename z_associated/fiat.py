import sys
import random

n=101



g= 3

x = random.randint(5,10)
v = random.randint(100,150)
c = random.randint(5,10)

if (len(sys.argv)>1):
	g=int(sys.argv[1])

if (len(sys.argv)>2):
	x=int(sys.argv[2])

if (len(sys.argv)>3):
	v=int(sys.argv[3])


if (len(sys.argv)>4):
	c=int(sys.argv[4])

if (len(sys.argv)>5):
	n=int(sys.argv[5])

y= g**x % n

t = g**v % n

r = v - c * x

Result = ( (g**r) * (y**c) ) % n

print '======Agreed parameters============'
print 'P=',n,'\t(Prime number)'
print 'G=',g,'\t(Generator)'


print '======The secret=================='
print 'x=',x,'\t(Alice\'s secret)'

print '======Random values==============='
print 'c=',c,'\t(Bob\'s random value)'
print 'v=',v,'\t(Alice\'s random value)'

print '======Shared value==============='
print 'g^x mod P=\t',y
print 'r=\t\t',r

print '=========Resuts==================='
print 't=g**v % n =\t\t',t
print '( (g**r) * (y**c) )=\t',Result
if (t==Result):
	print 'Alice has proven she knows x'
else:
	print 'Alice has not proven she knows x'

