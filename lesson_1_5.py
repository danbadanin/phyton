proceeds = int(input('Введите вашу выручку: '))
costs = int(input('Введите ваши издержки: '))

if proceeds > costs:
    print('Фирма отработала в плюс')
    profit = (proceeds - costs)
    profitability = profit / proceeds * 100
    print(f'Рентабельность выручки: {profitability}%')

    persons = int(input('Сколько человек работает в фирме? '))
    profit_per_person = profit / persons
    print(f'Прибыль на одного сотрудника: {profit_per_person}')
elif proceeds < costs:
    print('Фирма получила убыток')
else:
    print('Выручка фирмы равна издержкам')
