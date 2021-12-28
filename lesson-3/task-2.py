

def user_data(name, lastname, birthdate, city, email, tel):
    print(name, lastname, birthdate, city, email, tel)


def date_check(date):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not date.replace('.', '').isdigit():
        return False
    result = date.split('.')
    if len(result[0]) != 2 or len(result[1]) != 2:
        return False
    for i in range(3):
        result[i] = int(result[i])
    if len(result) == 3:
        if leap_year(result[2]):
            days_in_month[1] += 1
        if 0 < result[1] <= 12 and result[2] <= 2021 and 0 < result[0] <= days_in_month[result[1] - 1]:
            return True
    return False


def email_check(email):
    if '@' not in email:
        return False
    result = email.split('@')
    if len(result) == 2:
        if len(result[0]) > 0 and len(result[1]) > 2:
            if result[1].count('.') > 0:
                return True
    return False


def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def tel_check(tel):
    result = tel.replace(' ', '').replace('-', '').replace('-', '').replace('(', '').replace(')', '')
    if result[0] == '+':
        result = result[1:]
    if result.isdigit():
        return True
    return False


if __name__ == "__main__":
    name = input("Enter your name: ")
    lastname = input("Enter your last name: ")
    while True:
        birthdate = input("Enter your birthdate (dd.mm.yy): ")
        if date_check(birthdate):
            break
        else:
            print("Wrong input.")
    city = input("Enter your city of residence: ")
    while True:
        email = input("Enter your email: ")
        if email_check(email):
            break
        else:
            print("Wrong input.")
    while True:
        tel = input("Enter your telephone number: ")
        if tel_check(tel):
            break
        else:
            print("Wrong input.")
    user_data(name=name, lastname=lastname, city=city, birthdate=birthdate, email=email, tel=tel)
