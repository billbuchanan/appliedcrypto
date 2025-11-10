# Python program to print all Primes Smaller
# than or equal to N using Sieve of Eratosthenes


import sys
import time


def sieve_of_eratosthenes(num):

    # boolean array
    prime = [True for i in range(num+1)]
        
    p = 2
    while (p * p <= num):

		# If prime[p] is not
		# changed, then it is a prime
        if(prime[p] == True):

			# Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

	# Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            print(p)

def main(argv):
    start_time = time.time()
    sieve_of_eratosthenes(int(argv[0]))
    print("--- %s seconds ---" % (time.time() - start_time))


# Driver code
if __name__ == '__main__':
    main(sys.argv[1:])