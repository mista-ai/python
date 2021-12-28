def sum_array(arr):
    result = 0
    for x in arr:
        result += x
    return result


def user_input():
    print("Enter numbers separated by spaces. Enter q to stop.")
    args = input()
    state = False
    if 'q' in args:
        state = True
        args = args[:args.index('q')]
    args = args.split()
    array = [float(x) for x in args if is_number(x)]
    return array, state


def is_number(x):
    if x.count('.') > 1:
        return False
    if x[0] == '-':
        x = x[1:]
    x = x.replace('.', '')
    if x.isdigit():
        return True
    return False


if __name__ == "__main__":
    print("Program will ignore non-numbers. q - to quit")
    result = 0
    while True:
        array, state = user_input()
        result += sum_array(array)
        print(f'Sum: {result}')
        if state:
            break
