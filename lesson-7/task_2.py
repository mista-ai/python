from abc import ABC, abstractmethod


class Cloth(ABC):
    @abstractmethod
    def __init__(self, title='None'):
        self.title = title

    @abstractmethod
    def consumption(self):
        pass


class Coat(Cloth):
    def __init__(self, size=None, title=None):
        self._size = size
        self.title = title

    @property
    def size(self):
        if self._size == 0:
            return 'no size no coat'
        return self._size

    @size.setter
    def size(self, value):
        assert value != 0, 'Size must be more than 0'
        self._size = value

    def consumption(self):
        return round(self.size/6.5 + 0.5, 2) if type(self.size) is not str else self.size


class Jacket(Cloth):
    def __init__(self, height=None, title=None):
        self._height = height
        self.title = title

    @property
    def height(self):
        if self._height == 0:
            return 'no height no jacket'
        return self._height

    @height.setter
    def height(self, value):
        assert value != 0, 'Height must be more than 0'
        self._height = value

    def consumption(self):
        return round(2 * self.height + 0.3, 2) if type(self.height) is not str else self.height


if __name__ == '__main__':
    coat = Coat(0, 'Dolce')
    jack = Jacket(0, 'Versaci')
    print(f'Fabric consumption for {coat.title} is {coat.consumption()} and size is {coat.size}')
    print(f'Fabric consumption for {jack.title} is {jack.consumption()} and height is {jack.height}')
    coat.size = 10
    jack.height = 5
    print('Now!')
    print(f'Fabric consumption for {coat.title} is {coat.consumption()} and size is {coat.size}')
    print(f'Fabric consumption for {jack.title} is {jack.consumption()} and height is {jack.height}')