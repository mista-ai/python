def fact(n):
    factor = 1
    for i in range(1, n + 1):
        factor = factor * i
        yield factor

for x, el in zip(range(1, 11), fact(10)):
    print(f'{x}! = {el}')