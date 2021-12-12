def fact(n):
    num = 1
    if n < 0:
        yield 'Некорректное число'
    elif n == 0:
        yield f'{n}! = 1'
    for i in range(1, n+1):
        num *= i
        yield f'{i}! = {num}'


factorial = int(input('Введите число для получения факториала: '))

for el in fact(factorial):
    print(el)
