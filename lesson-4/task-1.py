from sys import argv

def salary(work_hour, wage_per_hour, premium):
    return work_hour * wage_per_hour + premium


if __name__ == '__main__':
    work_hour, wage_per_hour, premium = (float(x) for x in argv[1:])
    print(f'Your salary is {salary(work_hour, wage_per_hour, premium)}')
