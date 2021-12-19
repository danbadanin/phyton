class Cell:
    def __init__(self, count: int):
        self.count = count

    def __str__(self):
        return str(self.count)

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count > other.count:
            return Cell(self.count - other.count)
        else:
            return f'Нельзя вычесть из меньшего большее!'

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, arg):
        counts = self.count
        strs = ''
        loop = True
        while loop:
            for i in range(arg):
                if i > counts or counts == 0:
                    loop = False
                    break
                strs += '*'
            strs += '\n'
            counts -= arg
        return strs


first_cell = Cell(10)
second_cell = Cell(5)

print(first_cell + second_cell)
print(first_cell - second_cell)
print(second_cell - first_cell)
print(first_cell * second_cell)
print(first_cell / second_cell)
print(first_cell.make_order(5))
