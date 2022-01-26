class NotNumberError(ValueError):
    def __init__(self, txt):
        self.txt = txt


def isfloat_or_int(num):
    try:
        float(num)
        return True
    except ValueError:
        try:
            int(num)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    numbers = []
    while True:
        try:
            print('Enter "stop" to stop')
            num = input()
            if num == 'stop':
                break
            if not isfloat_or_int(num):
                raise NotNumberError("Your input is not number!")
        except NotNumberError as err:
            print(err)
        else:
            numbers.append(num)

print("So all numbers we have are:")
print(*numbers)
