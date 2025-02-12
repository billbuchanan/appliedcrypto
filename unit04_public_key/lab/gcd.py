import sys

def gcd(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

def main(argv):
    x, y = int(argv[0]), int(argv[1])
    g = gcd(x, y)
    print(f'gcd of {x} and {y} is {g}')

if __name__ == "__main__":
    main(sys.argv[1:])