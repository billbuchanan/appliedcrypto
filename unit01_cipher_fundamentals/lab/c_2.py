import sys

def mod(m, e, p):
    return m ** e % p    

def main(args):
    print(f'mod(m{args[0]}, e{args[1]}, p{args[2]}) = {mod(int(args[0]),int(args[1]),int(args[2]))}')
    
if __name__ == "__main__":
    main(sys.argv[1:])



