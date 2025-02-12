import sys 

# shared values
g = 2879
N = 9929

# secret value
b = 6
a = 9

def DH(g, secret, N):
    return pow(g, secret, N)

def DHKE(bob_swap_value, alice_secret, alice_swap_value, bob_secret, N):
    alice_key = DH(bob_swap_value, alice_secret, N)
    bob_key = DH(alice_swap_value, bob_secret, N)

    # independently generated keys
    print(f'Independently Generated Keys')
    print(f'Bob\'s Key: {bob_key}, Alice\'s Key: {alice_key}')

if __name__ == "__main__":
    g = int(sys.argv[1])
    N = int(sys.argv[2])
    alices_secret = int(sys.argv[3])
    bobs_secret = int(sys.argv[4])

    print(f'Shared Values\ng: {g}, N: {N}\n')
    print(f'Secret Values\nalices_secret: {alices_secret}, bobs_secret: {bobs_secret}\n')

    # exchangeable values
    alices_swappable_value = DH(g, alices_secret, N)
    bobs_swappable_value = DH(g, bobs_secret, N)    
    print(f'Independently calculated and exchanged values\nAlice\'s to send to Bob: {alices_swappable_value}, Bob\'s to send to Alice: {bobs_swappable_value}\n')

    DHKE(bobs_swappable_value, alices_secret, alices_swappable_value, bobs_secret, N)
