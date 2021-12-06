def my_func_pow(x, y):
    result = x ** y
    return result


def my_func_loop(x: float, y: int):
    result = 1
    for i in range(abs(y)):
        result *= 1 / x
    return result


first_num = float(input('Введите действительное положительное число: '))
second_num = int(input('Введите целое отрицательное число: '))

print(my_func_pow(first_num, second_num))
print(my_func_loop(first_num, second_num))
