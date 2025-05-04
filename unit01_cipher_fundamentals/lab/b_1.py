import sys

def gcd(a, b):
    
	while( b != 0 ):
		Remainder = a % b;
		a = b;
		b = Remainder;
	return a;

def main(args):
    print(f'gcd({args[0]}, {args[1]}) = {gcd(int(args[0]),int(args[1]))}')
    
if __name__ == "__main__":
    main(sys.argv[1:])



