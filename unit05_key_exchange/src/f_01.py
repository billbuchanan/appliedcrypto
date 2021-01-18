g=2
A=32
B=41
p=97
a=0
b=0
for x in range(0,p):
	if (g**x)% p==A:
		print "Found a=",x
		a=x
        if (g**x)% p==B:
                print "Found b=",x
		b=x
secret = g**(a*b) % p
print "Secret is:",secret
