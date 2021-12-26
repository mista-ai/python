def int_func(*args):
    result = []
    for word in args:
        result.append(capitalization(word))
    return ' '.join(result)


def capitalization(x):
    x = x.split()
    result = ''
    for elem in x:
        result += elem.capitalize() + ' '
    return result[:-1]


if __name__ == "__main__":
    print(int_func('text', 'hello world'))
