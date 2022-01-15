class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__mass_per_meter = 25
        self.__depth = 5
        self._mass = None

    def mass_calculate(self, mass_per_meter=25, depth=5):
        self.__mass_per_meter = mass_per_meter
        self.__depth = depth
        self.mass = self._length * self._width * self.__mass_per_meter * self.__depth / 1000
        return self.mass

    @property
    def mass(self):
        if self._mass is None:
            self.mass_calculate()
        return self._mass

    @mass.setter
    def mass(self, value):
        self._mass = value


if __name__ == '__main__':
    baker_street = Road(5000, 20)
    asphalt_mass = baker_street.mass_calculate()
    print(f'20 m * 5000 m * 25 kg * 5 sm = {asphalt_mass} t')
