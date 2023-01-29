import array
import math
import sys
import numpy as np

def sieve(limit):
    max = math.floor(math.sqrt(limit))
    print(max)
    a = np.arange(max)
    # a = [True] * limit  
    # a = array.array('I', False) * limit
    # Initialize the primality list
    a[0] = a[1] = False
    print(a)

    # for (i, isprime) in enumerate(a):
    #     # print(i, isprime)
    #     if isprime:
    #         yield i
    #         for n in range(i*i, limit, i):     # Mark factors non-prime
    #             a[n] = False
    #         else:
    #             a[n] = n
    # print(a)

def main(argv):
    sieve(int(argv[0]))

if __name__ == "__main__":
    main(sys.argv[1:])
