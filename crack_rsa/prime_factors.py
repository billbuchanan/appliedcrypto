import sys

def prime_factors_gen(n):
    i = 2
    while i * i <= n:
        # print(f'n: {n} i: {i}')
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n

if __name__ == "__main__":
    for p in prime_factors_gen(int(sys.argv[1])):
        print(p)
        