from abc import ABC, abstractmethod


class Equipment(ABC):
    @abstractmethod
    def __init__(self, title, kind='standard', speed=1, paper_format='A4', colour=True,):
        self.title = title
        self.kind = kind
        self.speed = speed
        self.paper_format = paper_format
        self.colour = colour


class Printer(Equipment):
    def __init__(self, title, capacity, kind='standard', speed=1, paper_format='A4', colour=True, ):
        super().__init__(title, kind, speed, paper_format, colour)
        self.capacity = capacity

    def __str__(self):
        return f'Printer {self.title}:\n capacity: {self.capacity}, type: {self.kind}'


class Scaner(Equipment):
    def __init__(self, title, resolution, kind='standard', speed=1, paper_format='A4', colour=True):
        super().__init__(title, kind, speed, paper_format, colour)
        self.resolution = resolution

    def __str__(self):
        return f'Printer {self.title}:\n resolution: {self.resolution}, type: {self.kind}'


class CopyMachine(Equipment):
    def __init__(self, title, copy_per_month, kind='standard', speed=1, paper_format='A4', colour=True):
        super().__init__(title, kind, speed, paper_format, colour)
        self.copy_per_month = copy_per_month

    def __str__(self):
        return f'Printer {self.title}:\n copies per month: {self.copy_per_month}, type: {self.kind}'


class CompanyObj:
    equip_map = {Printer.__name__: 'printer', Scaner.__name__: 'scaner',
                 CopyMachine.__name__: 'copy machine'}

    def __init__(self, name='Warehouse'):
        self.name = name
        self._stock = {'printer': [], 'scaner': [], 'copy machine': []}

    def load(self, equip):
        self._stock[CompanyObj.equip_map[equip.__class__.__name__]].append(equip)

    def unload(self, where, equip_name, **params):
        try:
            equip_index = self.find_equip(equip_name, **params) if len(params) != 0 else -1
            if equip_index != -2:
                where.load(self._stock[equip_name].pop(equip_index))
        except KeyError:
            print(f'{equip_name} is not found.')
        except IndexError:
            print(f'There is no {equip_name} in {self.name}')

    def find_equip(self, equip_name, **params):
        for index, equip in enumerate(self._stock[equip_name]):
            if params.items() <= equip.__dict__.items():
                return index
        return -2

    def __str__(self):
        return f'----------------------\n' \
               f'{self.name} contents:\nprinters: {len(self._stock["printer"])}' \
               f'\nscanners: {len(self._stock["scaner"])}' \
               f'\ncopy machines: {len(self._stock["copy machine"])}'


# Initialize warehouse and office
warehouse = CompanyObj()
office = CompanyObj('office')

# initialize our office equipment
printer1 = Printer('printer 2', 120)
scaner1 = Scaner('scaner 3', 640)
xerox = CopyMachine('xerox 4000', 4000)

# xerox is already in office
office.load(xerox)

# printer and scanner are in warehouse
warehouse.load(scaner1)
warehouse.load(printer1)

# before transfers
print("Before transfers")
print(warehouse)
print(office)

# transfer printer and scaner to office
warehouse.unload(office, 'printer')
warehouse.unload(office, 'scaner')

# xerox from office to warehouse
office.unload(warehouse, 'copy machine')
office.unload(warehouse, 'copy machine')

print('\n\nAfter transfers')
# print contents
print(warehouse)
print(office)
