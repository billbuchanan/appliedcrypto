import math

def gen_linear(a, seed,c, m):
	x=seed
	res=""

	for i in range(0,200):
                val = (a * x + c) % m
                res += str(val) + " "
                x = val;
	return (res)
a=21
X0=35
c=31
m=100  
res=gen_linear(a,X0,c,m)
print (res)
