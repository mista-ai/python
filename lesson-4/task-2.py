def more_than_previous(array):
    return [y for x, y in zip(array, array[1:]) if y > x]


# 300 2 12 44 1 1 4 10 7 1 78 123 55
while True:
    try:
        array = input().split()
        for i in range(len(array)):
            if array[i][0] != '-':
                if array[i].isnumeric():
                    array[i] = int(array[i])
                else:
                    array[i] = float(array[i])
            else:
                if array[i][1:].isnumeric():
                    array[i] = int(array[i])
                else:
                    array[i] = float(array[i])

        print(more_than_previous(array))
        break
    except ValueError:
        print("Input just numbers")
