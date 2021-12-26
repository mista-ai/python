def my_func(x, y):
    assert x > 0, "X is negative"
    assert (y < 0 and type(y) is int), "Y is not negative int"
    return x ** y


def my_func_two(x, y):
    assert x > 0, "X is negative"
    assert (y < 0 and type(y) is int), "Y is not negative int"
    result = 1
    for i in range(-y):
        result /= x
    return result


if __name__ == "__main__":
    try:
        a = float(input("Enter positive number: "))
        b = int(input("Enter negative integer: "))
        print(f'my_func: {my_func(a, b)}')
        print(f'my_func_two: {my_func_two(a, b)}')
    except AssertionError:
        print("Wrong input!")
    except ValueError:
        print("Wrong input!")
