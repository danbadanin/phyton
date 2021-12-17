class Car:
    def __init__(self, speed: int, color, name, is_police: bool):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехал')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')


class TownCar(Car):
    def about_car(self):
        print(f'Обычный городской седан {self.name}')

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')
        if self.speed > 60:
            print(f'{self.name} превышает скорость')


class SportCar(Car):
    def about_car(self):
        print(f'Спортивный автомобиль {self.name}')


class WorkCar(Car):
    def about_car(self):
        print(f'Рабчоий грузовик {self.name}')
        if self.speed > 40:
            print(f'{self.name} превышает скорость')


class PoliceCar(Car):
    def about_car(self):
        print(f'Полицейский автомобиль {self.name}')


town_car = TownCar(70, 'grey', 'Ford', False)
sport_car = SportCar(300, 'red', 'Ferrari', False)
work_car = WorkCar(35, 'white', 'Renault', False)
police_car = PoliceCar(60, 'white&blue', 'Lada', True)

town_car.go()
town_car.turn('налево')
town_car.show_speed()
town_car.stop()

sport_car.about_car()
