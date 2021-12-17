class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника - {self.name} {self.surname}')

    def get_full_income(self):
        print(f'Полный оклад сотрудника с учетом премии - {self._income["wage"] + self._income["bonus"]}')


my_worker = Position('Иван', 'Иванов', 'Менеджер', {"wage": 10000, "bonus": 2000})
my_worker.get_full_name()
my_worker.get_full_income()
