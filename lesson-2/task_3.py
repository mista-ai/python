months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
               'November', 'December']
months_dict = {}
for index, month in enumerate(months_list, 1):
    months_dict[index] = month

while True:
    n = input("Enter number of month (from 1 to 12): ")
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 12:
            break
        print("It's not a number from 1 to 12")
    else:
        print("It's not a number from 1 to 12")

print("\nSolution by list:")
print(f'Chosen month is {months_list[n-1]}')
print('\n***************************')
print("\nSolution by dict:")
print(f'Chosen month is {months_dict[n]}')
