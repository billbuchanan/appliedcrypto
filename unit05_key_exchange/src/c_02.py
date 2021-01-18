import sys
import random

p=11

def getG(p):

  for x in range (1,p):
	rand = x
	exp=1
	next = rand % p

	while (next <> 1 ):
		next = (next*rand) % p
		exp = exp+1
		

	if (exp==p-1):
		print rand

print getG(p)

