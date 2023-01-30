import array
import math
import sys
import numpy as np
import decimal

def sieve(limit):
    divisors = []
    squareroot = math.floor(decimal.Decimal(limit).sqrt())
    
    divideby = squareroot
    if squareroot % 2 == 0:
        divideby = squareroot - 1
    
    while divideby > 1:
        if limit % divideby == 0:            
            divisors.append(divideby)

        divideby = divideby - 2

    if not divisors:
        print(f'{limit} is prime')
    else:
        print(f'{limit} is not prime, divisors: {divisors}')

def main(argv):
    sieve(int(argv[0]))

if __name__ == "__main__":
    main(sys.argv[1:])
