
g = 2
p = 11
print('\tx\tg^x (mod p)')
for x in range(1,13):
    print(f'\t{x}\t{pow(g, x, p)}')