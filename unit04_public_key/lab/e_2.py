from factor import factors
from euclidian import inverse_of

# p=41
# q=19
# p=89
# q=83
p=61
q=103
# p=463
# q=499
N = p * q
PHI = (p-1)*(q-1)

for f in factors(PHI):
    print(f)

# e = 13
e = 107
# e = 353

# for d in range(1, 10000):
#     if (e*d) % PHI == 1:
#         break
# d=pow(e, -1, PHI)
d = inverse_of(e, PHI)

print(f'p: {p}, q: {q}, N: {N}, PHI:{PHI}, e: {e}, d: {d}, (e.d) (mod PHI): {(e*d) % PHI} ')



M = 777

C=pow(M, e, N)

print(f'M: {M}, C: {C}')

D=pow(C, d, N)
print(f'D: {D}')



