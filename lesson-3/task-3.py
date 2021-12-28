def my_func(x, y, z):
    arr = sorted([x, y, z])
    return arr[1] + arr[2]


def my_func_two(x, y, z):
    if x >= y >= z:
        return x + y
    elif x >= z >= y:
        return x + z
    else:
        return y + z


if __name__ == "__main__":
    try:
        a = float(input("Input 1st number: "))
        b = float(input("Input 2nd number: "))
        c = float(input("Input 3rd number: "))
        print(f'my_func: {my_func(a, b, c)}')
        print(f'my_func_two: {my_func_two(a, b, c)}')
    except ValueError:
        print("It's not a number!")
