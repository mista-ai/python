def int_func(*args):
    result = []
    for word in args:
        result.append(capitalization(word))
    return ' '.join(result)


def capitalization(x):
    x = x.split()
    result = ''
    for elem in x:
        if check_latin(elem):
            result += elem.capitalize() + ' '
    return result[:-1]


def check_latin(word):
    for letter in word:
        if ord(letter) < ord('A') or ord(letter) > ord('z'):
            return False
    return True


if __name__ == "__main__":
    print(int_func('text', 'hello world привет qew12 12qw 32привет qwыв manM'))
