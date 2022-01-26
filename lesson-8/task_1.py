class Data:
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    @classmethod
    def normalize(cls, data):
        dd, mm, yy = tuple(map(int, data.split('-')))
        assert Data.validation(dd, mm, yy), 'Data is wrong.'
        return cls(dd, mm, yy)

    @staticmethod
    def leap_year(yy):
        if (yy % 400 == 0) and (yy % 100 == 0):
            return True
        elif (yy % 4 == 0) and (yy % 100 != 0):
            return True
        else:
            return False

    @staticmethod
    def validation(dd, mm, yy):
        if not 1 <= mm <= 12:
            return False
        if mm == 2 and Data.leap_year(yy):
            if not 1 <= dd <= 29:
                return False
        elif not 1 <= dd <= Data.months[mm]:
            return False
        return True

    def __str__(self):
        return f'{self.dd:02d}-{self.mm:02d}-{self.yy}'


if __name__ == "__main__":
    d1 = Data.normalize('28-02-2021')
    print(d1)