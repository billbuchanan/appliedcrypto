import math
import sys

def calculate_entropy(password_length, no_of_chars):
    no_of_combinations = no_of_chars**password_length
    entropy = math.log10(no_of_combinations)/math.log10(2)
    return no_of_combinations, entropy

def main(argv):
    password_length = int(argv[0])
    no_of_chars = int(argv[1])
    no_of_combinations, entropy = calculate_entropy(password_length, no_of_chars)
    print(f'for a password of length {password_length} and {no_of_chars} of characters, there is {no_of_combinations} possible combinations and the key entropy is {entropy}.')

if "__main__" == __name__:
    main(sys.argv[1:])
