def users_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} - {value}', end='; ')


params = ('name', 'surname', 'birth', 'city', 'email', 'phone')
person = {}
for param in params:
    person[param] = (input(f'Введите параметр {param}: '))

users_info(**person)
