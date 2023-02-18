from primes_to import primes_from


N = 879509040449463763008386484793372267
primes = primes_from(1000000000, 1000000000)
# print(f'primes: {primes}')

for i in range(len(primes)-1, 1000, -1):
    for j in range(len(primes)-1, 1000, -1):
        p = primes[i]
        q=primes[j]
        n=p*q
        print(f'p: {p}, q:{q}, n:{n}')
        if n == N:
            print(f'Cracked: p: {p}, q: {q}')
            break

