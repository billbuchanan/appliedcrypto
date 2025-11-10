import sys

p=41

def getG(p):
    l = []
    for x in range (1, p):
        rand = x
        exp = 1
        next = rand % p

        while (next != 1 ):
            next = (next * rand) % p
            exp = exp + 1

        if (exp == p - 1): 
	        # print (rand)
            l.append(rand)
    return l

l = getG(p)
print (''.join(str(l)))
print(len(l))
