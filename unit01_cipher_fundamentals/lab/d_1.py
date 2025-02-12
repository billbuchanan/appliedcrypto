import math
import sys

def get_if_prime(val):
  limit = math.sqrt(val)

  if (val % 2 == 0):
    return (False) 
            
  if (val % 3 == 0):
    return (False)

  for k in range(1, 10000):

    testval = 6 * k + 1
    if (testval>limit):
      break

    if (val % testval == 0):
      return (False)

    testval = 6 * k - 1;
    
    if (testval>limit):
      break
 
    if (val % testval == 0):
      return (False)
  return (True)



def main(argv):
    primes = []
    for i in range(0, int(argv[0])):
        res = get_if_prime(i)
        if (res==True):
            print (str(i)+" is prime")
            primes.append(i)

    print(", ".join(str(x) for x in primes))

if __name__ == "__main__":
    main(sys.argv[1:])

