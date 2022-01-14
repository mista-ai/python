from functools import reduce

def product(x, y):
    return x * y

result = [x for x in range(10, 1001) if x % 2 == 0]
print(reduce(product, result))