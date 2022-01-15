with open('text_5.txt', 'w+') as f:
    while True:
        try:
            f.seek(0)
            user_input = input()
            map(float, user_input)
            f.write(user_input)
            f.seek(0)
            numbers = f.read()
            print(f'Sum of numbers in file is {sum(map(float, numbers.split()))}')
            break
        except ValueError:
            print("Input only numbers!")
