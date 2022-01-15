def average_salary(db):
    return sum(db.values()) / len(db)


def poor_employee(db):
    return {l_name: salary for (l_name, salary) in db.items() if salary < 20000}


with open('text_3.txt', 'r', encoding='utf-8') as f:
    employee_db = dict()
    for line in f:
        last_name, salary = line.split()
        salary = float(salary)
        employee_db[last_name] = salary
    print("Employees with salary less than 20 000:\n")
    for last_name, salary in poor_employee(employee_db).items():
        print(last_name, salary)
    print(f'\nAverage salary is {average_salary(employee_db)}')
