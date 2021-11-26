start = int(input('Введите начальный километраж: '))
finish = int(input('Введите конечный километраж: '))

i = 1

while start < finish:
    start += start * 0.1
    i += 1

print(f'На {i}-ый день спортсмен достиг результата - не менее {finish} км в день')
