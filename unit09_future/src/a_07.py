import random

p=59
g=13
x=11
v=9

	
def string2numeric_hash(text):
    import hashlib
    return int(hashlib.md5(text).hexdigest()[:8], 16)

if (len(sys.argv)>1):
	g=int(sys.argv[1])

if (len(sys.argv)>2):
	x=int(sys.argv[2])

v= random.randint(3, 8)

print 'g=',g
print 'x=',x, ' (the secret)'
print 'v=',v, ' (random)'
print '=====Alice computes========='

import hashlib

y= g**x 
t= g**v  

print 't=',t

print 'y=',y

c = string2numeric_hash(str(g)+str(y)+str(t))
c =c % p

print 'c=',c

r= v -c*x

print '=============='

print 'Alice sends (t,r)=(',str(t),',',(r),')'

t1 = (g**r)
t2= (y**c)

val=int(t1*t2)
print 'My calc for g^r x y^c=',val

if (val==t):
	print "Alice has proven her ID"
else:
	print "You are a fraud"