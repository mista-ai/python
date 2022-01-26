class ZeroError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt


a = input("Input dividend: ")
b = input("Input divisor: ")

try:
    a = float(a)
    b = float(b)
    if b == 0:
        raise ZeroError("Divisor can't be equal to 0!")
except ValueError:
    print("It's not a float number")
except ZeroError as err:
    print(err)
else:
    print(f"Everything's ok: {a/b}")