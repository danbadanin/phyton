months_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
months_dic = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}

while True:
    month = int(input('Введите номер месяца (от 1 до 12): '))
    if month <= 12 and month >= 1:
        break

# Вывод из списка
print(f'Месяц относится к вреемни года {months_list[month - 1]}')

# Вывод из словаря
for key, season in months_dic.items():
    if month in season:
        print(f'Месяц относится к вреемни года {key}')
        break
