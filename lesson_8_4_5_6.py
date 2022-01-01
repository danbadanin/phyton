class Errors(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:
    def __init__(self, name, capacity, compound):
        self.name = name
        self.capacity = capacity
        self.compound = compound

    def take_to_storage(self, tech, count):
        free_space = self.capacity - sum(self.compound.values())
        if free_space < count:
            raise Errors(f'На скалде {self.name} недостаточно места для пополнения!')
        if tech.name in self.compound:
            self.compound[tech.name] += count
        else:
            self.compound[tech.name] = count
        print(f'На склад {self.name} поступила техника {tech.name} в количестве {count} шт.\nВсего на складе {self.compound[tech.name]} шт.')

    def transfer(self, other, tech, count):
        if self.compound[tech.name] < count:
            raise Errors(f'На складе {self.name} меньше, чем требуется для трансфера!')
            return
        else:
            self.compound[tech.name] -= count
        try:
            other.take_to_storage(tech, count)
            if self.compound[tech.name] == 0:
                del self.compound[tech.name]
        except Errors as e:
            self.compound[tech.name] += count
            print(e.txt)

        print(f'Склад-отправитель: \nНа складе {self.name} находится:\n{self.compound}')
        print(f'Склад-получатель: \nНа складе {other.name} находится:\n{other.compound}')


class Tech:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Printer(Tech):
    def __init__(self, name, price, colors, paper):
        self.colors = colors
        self.paper = paper
        Tech.__init__(self, name, price)


class Scan(Tech):
    def __init__(self, name, price, sides):
        self.sides = sides
        Tech.__init__(self, name, price)


class Copier(Tech):
    def __init__(self, name, price, resolution):
        self.resolution = resolution
        Tech.__init__(self, name, price)


printer = Printer('HP color', 10000, 'color', 'A4')
scanner = Scan('Kyocera 123', 30000, 'double')
xerox = Copier('Xerox', 15000, '1200х900')

moscow = Storage('Москва', 10, {})
spb = Storage('Санкт-Петербург', 15, {})

counts = input('Введите количество принтеров для перемещения между складами: ')
check_list = list(map(str, range(10)))
try:
    for i in range(len(counts)):
        if counts[i] not in check_list:
            raise Errors('Необходимо вводить только числа!')
    moscow.take_to_storage(printer, 5)
    moscow.transfer(spb, printer, int(counts))
except Errors as err:
    print(err.txt)
