from itertools import count, cycle
# Итератор целых чисел
start = int(input('Введите стартовую позицию: '))
print('Целые числа, начиная с указанного:')
for el in count(start):
    if el > start + 15:
        break
    print(el)

# Итератор значений списка
c = 0
my_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
print(f'\nПовторение элементов исходного списка {my_list}:')
for el in cycle(my_list):
    if c > 15:
        break
    print(el)
    c += 1
