from time import sleep


class TrafficLight:
    __color = None

    def running(self):
        timetable = {'red': 7, 'yellow': 2, 'green': 5}
        for _ in range(5):
            for key, value in timetable.items():
                self.__color = key
                print(self.__color)
                sleep(value)


my_light = TrafficLight()
my_light.running()
