from abc import abstractmethod


class Clothes:
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):
    @property
    def consumption(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    @property
    def consumption(self):
        return self.param * 2 + 0.3


coat = Coat(52)
suit = Suit(185)

print(coat.consumption)
print(suit.consumption)
print(coat + suit)
