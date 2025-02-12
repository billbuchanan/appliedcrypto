g=2
p=97

def calculate(a):
    A = pow(g, a, p)

    # if A == 32 or A == 41:
    # if A == 41:
    print(f'g: {g}, p: {p}, a: {a}, A: {A}')

for i in range(0, 9999999):
    calculate(i)
