class Date:
    @classmethod
    def extracts(cls, param):
        cls.dates = param
        lists = list(map(int, cls.dates.split('-')))
        print(lists)
        cls.dates = lists

    @staticmethod
    def validator():
        valid = {'День': 32, 'Месяц': 13, 'Год': 2100}
        for i in range(len(valid)):
            if Date.dates[i] in range(1, list(valid.values())[i]):
                print(f'{list(valid)[i]} указан правильно')
            else:
                print(f'{list(valid)[i]} указан неправильно!')


Date.extracts('10-12-2021')
Date.validator()
