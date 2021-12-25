while True:
    n = input("Enter amount of elements in array: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("It's not a number, please enter integer number: ")

array = []
for i in range(n):
    array.append(input(f"Enter element {i}: "))

for i in range(1, n, 2):
    array[i - 1], array[i] = array[i], array[i - 1]

print(array)
