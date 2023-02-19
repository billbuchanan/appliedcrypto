import sys
from sieve import sieve
from euclidian import inverse_of

def calculate_N(p, q):
    return p * q

def calculate_PHI(p, q):
    return (p-1) * (q-1)

def determine_eNdN(p, q, e):
    N = calculate_N(p, q)
    PHI = calculate_PHI(p, q)
    d = inverse_of(e, PHI)
    eN = e * N
    dN = d * N
    return d, eN, dN

def encrypt(M, e, N):
    return pow(M, e) % N

def decrypt(C, d, N):
    return pow(C, d) % N

if __name__ == "__main__":
    p = int(sys.argv[1])
    q = int(sys.argv[2])
    e = int(sys.argv[3])
    M = int(sys.argv[4])

    if sieve(p) and sieve(q):
        N = calculate_N(p, q)
        PHI = calculate_PHI(p, q)
        d, en, dn = determine_eNdN(p, q, e)
        print(f'p:{p}, q: {q}, N: {N}, PHI: {PHI}, d: {d}, e.N: {en}, d.N: {dn}')

        if M:
            C = encrypt(M, e, N)
            P = decrypt(C, d, N)
            print(f'M: {M}, C: {C}, Pt: {P}')
    else:
        print(f'p:{p} and q: {q} must both be prime.')
