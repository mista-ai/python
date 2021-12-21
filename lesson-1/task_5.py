# task 1.5
proceeds = int(input("Какая выручка в вашей компании? "))
costs = int(input("Какие издержки в вашей компании? "))
result = proceeds - costs

if result < 0:
    print("Вы работаете в убыток")
if result > 0:
    print("Вы работаете в прибыль")
    print(f'Рентабельность вашего бизнеса: {result / proceeds:.2f}')
    amount_of_employees = int(input("Введите количество сотрудников: "))
    print(f'Прибыль на сотрудника: {result / amount_of_employees:.2f}')
else:
    print("Вы работаете в ноль")
