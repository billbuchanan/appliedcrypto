from math import sqrt
def factors(n):    # (cf. https://stackoverflow.com/questions/16007204/factorizing-a-number-in-python)
    j = 2
    while n > 1:
        for i in range(j, int(sqrt(n+0.05)) + 1):
            if n % i == 0:
                n //= i ; j = i
                yield i
                break
        else:
            if n > 1:
                yield n; break

for f in factors(879509040449463763008386484793372267):
    print(f)