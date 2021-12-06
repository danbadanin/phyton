def division(number_1, number_2):
    if number_2 == 0:
        return 'Деление на 0!'
    else:
        result = number_1 / number_2
        return result


numbers = []
for i in range(2):
    numbers.append(float(input(f'Введите число {i+1}: ')))

print(f'Реузльтат операции: {division(numbers[0], numbers[1])}')
