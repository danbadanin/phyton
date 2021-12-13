all_salary = 0
i = 0
with open('lesson_5_3.txt', 'r') as f:
    for line in f:
        surname, salary = line.split()
        if int(salary) < 20000:
            print(f'Получает меньше 20.000 руб.: {surname}')
        all_salary += int(salary)
        i += 1
    print(f'Средняя зарплата: {all_salary / i}')
