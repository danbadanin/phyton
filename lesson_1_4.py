number = input('Введите целое положительное число: ')

max_number = 0
i = 0

while i < len(number):
    if int(number[i]) > max_number:
        max_number = int(number[i])
    i += 1

print(f'Наибольшая цифра в числе: {max_number}')
