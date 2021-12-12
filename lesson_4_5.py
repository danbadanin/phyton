from functools import reduce


def multip(prev_el, el):
    return prev_el * el


main_list = [el for el in range(100, 1001, 2)]

print(f'Список: {main_list}')
print(f'Умножение элементов списка: {reduce(multip, main_list)}')
