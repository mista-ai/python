class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        # print('Запуск отрисовки')
        return 'Запуск отрисовки'


class Pen(Stationary):
    def __init__(self):
        super(self.__class__, self).__init__('ручка')

    def draw(self):
        # print('Рисуем ручкой')
        return 'Рисуем ручкой'


class Pencil(Stationary):
    def __init__(self):
        super(self.__class__, self).__init__('карандаш')

    def draw(self):
        # print('Рисуем карандашом')
        return 'Рисуем карандашом'


class Handle(Stationary):
    def __init__(self):
        super(self.__class__, self).__init__('маркер')

    def draw(self):
        # print('Рисуем маркером')
        return 'Рисуем маркером'


if __name__ == '__main__':
    stationary = Stationary('кисть')
    pen = Pen()
    pencil = Pencil()
    handle = Handle()
    for stat in (stationary, pen, pencil, handle):
        print(f'{stat.title}: {stat.draw()}')
