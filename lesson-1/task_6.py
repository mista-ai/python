import math

a = int(input("Результат 1-го дня: "))
b = int(input("Интересующий результат: "))

# mathematically
# print(1 + math.ceil(math.log(b/a, 1.1)))


# with loop
day = 1
while a < b:
    day += 1
    a *= 1.1

print(day)
