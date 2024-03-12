import sys

def dec_to_hex(dec):
    return hex(dec)

def hex_to_dec(hex):
    return int(hex, 16)

def main(argv):
    if (argv[0] == "d"):
        result = hex_to_dec(argv[1])
        print(f'hex {argv[1]} is dec {str(result)}')
    elif (argv[0] == "h"):
        result = dec_to_hex(int(argv[1]))
        print(f'dec {argv[1]} is hex {result}, type: {type(result)}')
    return result

if __name__ == "__main__":
    main(sys.argv[1:])