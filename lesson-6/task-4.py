class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car has gone')

    @staticmethod
    def stop():
        print('The car has stopped')

    @staticmethod
    def turn(direction):
        print(f'The car has turned to {direction}')

    def show_speed(self):
        print(f'Speed is {self.speed}')

    def __repr__(self):
        return f'{self.__class__.__name__}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Town car is speeding')
        else:
            print(f'Speed is {self.speed}')


class SportCar(Car):
    def go(self):
        print('Sport Car started the race')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Work car is speeding')
        else:
            print(f'Speed is {self.speed}')


class PoliceCar(Car):
    def go(self):
        print('Police car is pursuing a speeder')


if __name__ == '__main__':
    town_car = TownCar(120, 'grey', 'honda fit', False)
    town_car_two = TownCar(60, 'grey', 'volkswagen golf', False)
    sport_car = SportCar(240, 'red', 'mercedes amg-gt', False)
    work_car = WorkCar(120, 'white', 'volvo fl', False)
    work_car_two = WorkCar(40, 'white', 'mercedes actros', False)
    police_car = PoliceCar(220, 'blue', 'toyota camry', True)
    for x in (town_car, sport_car, work_car, police_car):
        print(f'{x}: speed - {x.speed}, color - {x.color}, model - {x.name},\
          police - {x.is_police}')
    print()
    for x in (town_car, town_car_two, sport_car, work_car, work_car_two, police_car):
        print(f'{x} - {x.name}')
        x.go()
        x.stop()
        x.turn('city')
        x.show_speed()
        print(f'\n---------')
