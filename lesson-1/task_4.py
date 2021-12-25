# task 1.4
user_number = int(input("Введите натуральное число: "))
biggest_natural = 1

while user_number > 0:
    biggest_natural = user_number % 10 if biggest_natural < user_number % 10 \
        else biggest_natural
    if biggest_natural == 9:
        break
    user_number //= 10

print(f'Biggest digit is {biggest_natural}')
