p = 11
q = 13
N=p*q
print(f'N: {N}')

PHI = (p-1)*(q-1)
print(f'PHI: {PHI}')

e=65537
# e=11
d=pow(e, -1, PHI)
print(f'd: {d}')

M=4

C=pow(M, e, N)

print(f'M: {M}, C: {C}')

D=pow(C, d, N)
print(f'D: {D}')


