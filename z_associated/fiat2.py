import sys
import random
import hashlib

n=997

text="Hello"

g= 3

def extended_euclidean_algorithm(a, b):
    """
    Returns a three-tuple (gcd, x, y) such that
    a * x + b * y == gcd, where gcd is the greatest
    common divisor of a and b.

    This function implements the extended Euclidean
    algorithm and runs in O(log b) in the worst case.
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse_of(n, p):
    """
    Returns the multiplicative inverse of
    n modulo p.

    This function returns an integer m such that
    (n * m) % p == 1.
    """
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p

def pickg(p):
	for x in range (1,p):
		rand = x
		exp=1
		next = rand % p

		while (next <> 1 ):
			next = (next*rand) % p
			exp = exp+1
		
		if (exp==p-1):
			return rand

v = random.randint(1,n)
c = random.randint(1,n)


if (len(sys.argv)>1):
	text=str(sys.argv[1])

if (len(sys.argv)>2):
	v=int(sys.argv[2])

if (len(sys.argv)>3):
	c=int(sys.argv[3])

if (len(sys.argv)>4):
	n=int(sys.argv[4])



print "Password:\t",text
x = int(hashlib.md5(text).hexdigest()[:8], 16) % n

g=pickg(n)

y= pow(g,x,n)

t = pow(g,v,n)

r = (v - c * x) 

if (r<0):
	Result = ( inverse_of(pow(g,-r,n),n) * pow(y,c,n))  % n
else:
	Result = ( pow(g,r,n) * pow(y,c,n))  % n

print '\n======Agreed parameters============'
print 'P=',n,'\t(Prime number)'
print 'G=',g,'\t(Generator)'


print '\n======The secret=================='
print 'x=',x,'\t(Alice\'s secret)'

print '\n======Random values==============='
print 'c=',c,'\t(Bob\'s random value)'
print 'v=',v,'\t(Alice\'s random value)'

print '\n======Shared value==============='
print 'g^x mod P=\t',y
print 'r=\t\t',r

print '\n=========Results==================='
print 't=g**v % n =\t\t',t
print '( (g**r) * (y**c) )=\t',Result
if (t==Result):
	print 'Alice has proven she knows password'
else:
	print 'Alice has not proven she knows x'

