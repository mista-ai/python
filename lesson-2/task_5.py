my_list = [7, 5, 3, 3, 2]
my_list.sort(reverse=True)
while True:
    element = input('Enter number (enter "end" to end input): ')
    if element.isdigit() or (element[0] == '-' and element[1:].isdigit()):
        my_list.append(int(element))
        for i in range(len(my_list) - 1, 0, -1):
            if my_list[i] > my_list[i - 1]:
                my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
            else:
                break
        print(f'user entered {element}. Result is ', end='')
        for x in my_list:
            print(x, end=' ')
        print()
    elif element == 'end':
        break
    else:
        print("Enter a number!")

print(my_list)
