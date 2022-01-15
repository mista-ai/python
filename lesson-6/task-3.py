class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        assert name.isalpha(), 'Name must contain only letters'
        assert surname.isalpha(), 'Surname must contain only letters'
        assert type(wage) is float or type(wage) is int, 'Wage must be a number'
        assert type(bonus) is float or type(bonus) is int, 'Wage must be a number'
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


if __name__ == '__main__':
    bob = Position('Bob', 'Mcdonalds', 'dev', 10000, 5000.5)
    # bob = Position('Bob', 'Mcdonalds1', 'dev', 10000, 5000.5)
    susie = Position('Susie', 'Porier', 'manager', 15000.1, 2000)
    # susie = Position('Susie1', 'Porier', 'manager', 15000.1, 2000)
    print(f'''{bob.get_full_name()}, income: {bob.get_total_income()}
{susie.get_full_name()}, income: {susie.get_total_income()}''')
