import time
from itertools import cycle
from termcolor import colored


class TrafficLight:
    def __init__(self):
        self.__color = None
        self.__queue = {None: 'red', 'red': 'yellow', 'yellow': 'green', 'green': 'red'}
        self.__sleep = {'red': 7, 'yellow': 2, 'green': 10}
        # how many colors will be shown
        self.__power = 5
        self.__log = []

    def running(self):
        self.__log = []
        while self.__power > 0:
            self.switch()
            print(colored(self.__color, self.__color))
            for sec in range(self.__sleep[self.__color], 0, -1):
                print(colored(sec, self.__color))
                time.sleep(1)
            self.__power -= 1
        self.__power = 5

    def switch(self):
        self.__color = self.__queue[self.__color]
        self.__log.append(self.__color)

    @property
    def log(self):
        return self.__log


def test_colors(traffic_light_test):
    color_queue = cycle(['red', 'yellow', 'green'])
    for color in traffic_light_test.log:
        if color != next(color_queue):
            return False
    return True


if __name__ == '__main__':
    traffic_light_first = TrafficLight()
    traffic_light_first.running()
    if test_colors(traffic_light_first):
        print('Color queue is right.')
