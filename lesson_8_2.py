class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    user_var = int(input('Введите число в качестве делителя 15: '))
    if user_var == 0:
        raise ZeroError('Собственная ошибка деления на 0!')
    result = 15 / user_var
except ValueError:
    print('Вы ввели не число!')
except ZeroError as err:
    print(err.txt)
