timestamp = int(input('Введите время в секундах: '))

if timestamp < 0:
    print('Время не может быть отрицательным!')
    exit()
elif timestamp // 86400 > 0:
    timestamp -= (timestamp // 86400) * 86400
    print('Количество секунд больше, чем в сутках, преобразовано')

hours = timestamp // 3600
minutes = (timestamp - hours * 3600) // 60
seconds = timestamp - hours * 3600 - minutes * 60

print(f'{hours if hours > 9 else "0" + str(hours)}:{minutes if minutes > 9 else "0" + str(minutes)}:{seconds if seconds > 9 else "0" + str(seconds)}')
