p = 17
q = 97
N=p*q
print(f'N: {N}')

PHI = (p-1)*(q-1)
print(f'PHI: {PHI}')

e=5
d=pow(e, -1, PHI)
print(f'd: {d}')

M=1648
C=pow(M, e, N)

print(f'M: {M}, C: {C}')

D=pow(C, d, N)
print(f'D: {D}')


