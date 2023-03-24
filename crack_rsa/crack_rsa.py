# Find p & q for a given product p.q = N
import sys
from prime_factors import prime_factors_gen
from gcd import gcd

def select_g_with_no_common_factors_of(N):
    factors = []
    for p in prime_factors_gen(N):
        factors.append(p)

    factors.sort()
    print(factors)

    # c = len(factors) - 1
    # while c >= 0:
    for c in range(0, len(factors)):
        g = factors[c] + 1
        g2 = factors[c] - 1
        print(f'g: {g} g2: {g2}')
        if gcd(N, g) == 1:
            return g
        elif gcd(N, g2) == 1:
            return g2
    return 0

def calculate_gr_modN_eq_1(N, g):
    r = 1
    modN = 0
    while modN != 1:
        gr = g**r
        modN = (gr) % N
        print(f'g**r: {gr} modN: {modN}')
        if modN == 1:
            return r
        r += 1

def factor_out_p_and_q(N, g, r):
    gr = g**(r/2)
    p = -1
    q = -1
    value1 = gr+1
    modulo = N
    while int(p) != 0:
        r1 = value1 % modulo
        # print(f'r1: {value1} % {modulo} = {r1}')
        if r1 == 0:
            p = int(modulo)
            print(f'p: {p}')
            break
        else:
            value1 = modulo
            modulo = r1

    value2 = gr-1
    modulo = N
    while int(q) != 0:
        r2 = value2 % modulo
        # print(f'r2: {value2} % {modulo} = {r2}')
        if r2 == 0:
            q = int(modulo)
            print(f'q: {q}')
            break
        else:
            value2 = modulo
            modulo = r2
    
    return p, q

def crack(N):    
    # print(f'N: {N}')
    g = select_g_with_no_common_factors_of(N)
    r = calculate_gr_modN_eq_1(N, g)
    p, q = factor_out_p_and_q(N, g, r)
    print(f'N: {N} g: {g} r: {r} p: {p} q: {q}')

if __name__ == "__main__" and len(sys.argv) > 0:
    crack(int(sys.argv[1]))