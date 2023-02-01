import math
import sys
import time
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
    start_time = time.time()
    sieve(int(argv[0]))
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main(sys.argv[1:])
