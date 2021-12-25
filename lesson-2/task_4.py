user_string = input("Input your string: ")
user_string = user_string.split()
for index, elem in enumerate(user_string, 1):
    print(f'Word #{index}: {elem[:10]}')