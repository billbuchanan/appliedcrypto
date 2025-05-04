
import sys

test=1000

if (len(sys.argv)>1):
	test=int(sys.argv[1])

def primes_to(n):
    size = (n + 1)//2
    # print(f'size: {size}')
    sieve = [1]*size
    # print(f'sieve: {sieve}')
    limit = int(n**0.5)
    # print(f'limit: {limit}')
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            # print(f'sieve: {sieve}, i: {i}, val: {val}, tmp: {tmp}')
            sieve[i+val::val] = [0]*tmp
            # print(f'sieve: {sieve}, sieve[{i+val}::{val}]: {sieve[i+val::val]}, [0]*{tmp}: {[0]*tmp}')
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]
 

print (primes_to(test))
