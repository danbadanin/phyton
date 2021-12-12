from sys import argv


def reward():
    try:
        time, rate, premium = map(float, argv[1:])
        print(f'Зарплата сотрудника: {time * rate + premium}')
    except ValueError:
        print('При запуске программы необходимо передать 3 параметра - отработанное время, ставку в час и премию')


reward()
