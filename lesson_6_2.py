class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self, square, thickness):
        weight = self._length * self._width * square * thickness
        print(f'{weight} кг необходимо')


my_road = Road(100, 10)
my_road.asphalt(25, 5)
