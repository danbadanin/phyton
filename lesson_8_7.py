class Complexus:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return Complexus((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        result = self.a * other.a - self.b * other.b
        result_i = self.b * other.a + self.a * other.b
        return Complexus(result, result_i)


first = Complexus(2, 5)
second = Complexus(3, 4)

print(first + second)
print(first * second)
