import math
import sys
import decimal
import time

def sieve(limit):
    if limit % 2 == 0:
        return False

    squareroot = math.floor(decimal.Decimal(limit).sqrt())

    for k in range(1, squareroot):

        testval = 6 * k - 1
        # print(f'limit: {limit}, testval: {testval}, limit % testval: {limit % testval}, squareroot: {squareroot}')

        if limit % testval == 0:
            return False

        testval = 6 * k + 1
        # print(f'limit: {limit}, testval: {testval}, limit % testval: {limit % testval}')
        if testval > squareroot:
            break

        if limit % testval == 0:
            return False

    return True

def main(argv):
    start_time = time.time()
    if sieve(int(argv[0])):
        print(f'{int(argv[0])} is prime')
    else:
        print(f'{int(argv[0])} is not prime')
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main(sys.argv[1:])
