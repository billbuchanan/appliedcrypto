import sys

# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors

def prime_factors_gen(n):
    i = 2
    while i * i <= n:
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
        