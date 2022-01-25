class Cell:
    def __init__(self, number):
        assert number > 0, "Number of cells can't be less than 1"
        self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        assert self.number - other.number > 0, "Number of cells can't be less than 1"
        return Cell(self.number - other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        assert self.number / other.number > 0, "Number of cells can't be less than 1"
        return Cell(self.number // other.number)

    def make_order(self, n):
        assert self.number > 0, "Number of cells can't be less than 1"
        return ('*' * n + '\n') * (self.number // n) + '*' * (self.number % n)


a = Cell(12)
b = Cell(4)
c = a * b
d = a - b
e = a + b
f = a / b
print(f'Cell a = {a.number}, Cell b = {b.number}')
print(f'Cell c = a * b = {c.number}, make_order(5)')
print(c.make_order(5))

print(f'Cell d = a - b = {d.number}, make_order(5)')
print(d.make_order(5))

print(f'Cell e = a + b = {e.number}, make_order(5)')
print(e.make_order(5))

print(f'Cell f = a / b = {f.number}, make_order(5)')
print(f.make_order(5))
