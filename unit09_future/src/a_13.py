import sys
from random import randint

J = 4
I = 5

e=79
d=1019
N=3337

primes = [601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997]
val=randint(0,len(primes))
p=primes[val]

U=randint(0,2000)

C=(U**e) % N

print 'Bob has',I,'millions'
print 'Alice has',J,'millions'

print '\ne=',e,'d=',d,'N=',N,'p=',p
print '\nRandom Value U is:\t',U
print 'C value is (U^e %N):\t',C

val_for_alice = C - J + 1
print "Alice shares this value (C-J-1):",val_for_alice

Z=[]

for x in range(0,10):
	val = (((val_for_alice+x)**d) % N) % p
	if (x>(I-1)):
		Z.append(val+1)
	else:
		Z.append(val)

G = U % p


print "\nG value is",G
print "Z values are:",
for x in range(0,10):
	print Z[x],

print '\n\nAlice checks U(',U,') against the ',J,'th value (',Z[J-1],')'
if (G==Z[J-1]): print "\nSame. Bob has more money or the same"
else: print "\nDiffer. Alice has more money"