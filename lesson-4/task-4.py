# 2 2 2 7 23 1 44 44 3 2 10 7 4 11
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

        print([x for x in array if array.count(x) == 1])
        break
    except ValueError:
        print("Input just numbers")
