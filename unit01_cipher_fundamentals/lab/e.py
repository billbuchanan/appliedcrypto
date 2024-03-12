import math

def gen_linear(a, seed,c, m):
    x = seed
    res = ""

    for i in range(0,200):
        val = (a * x + c) % m
        res += str(val) + " "
        x = val

    return(res)

a=2175143
X0=3553
c=10653
m=1000000
res=gen_linear(a,X0,c,m)
print (res)
