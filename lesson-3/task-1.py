def division(a, b):
    """
    Division a by b
    division(number, number) -> float
    division(9, 3) -> 3.0
    division(9, 0) -> can't divide by zero
    """
    try:
        return a/b
    except ZeroDivisionError:
        return "can't divide by zero"
    except TypeError:
        return "unsupported operand type(s)"


if __name__ == '__main__':
    while True:
        try:
            x = float(input("Enter dividend: "))
            y = float(input("Enter divisor: "))
            print(division(x, y))
            break
        except TypeError:
            print("Wrong input.")
