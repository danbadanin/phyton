products = []
features = ('Название', 'Цена', 'Количество', 'Ед.')

while True:
    print('-' * 20)
    print('МЕНЮ')
    print('-' * 20)
    print('1. Добавить товар\n2. Показать все товары\n3. Вывести аналитику\n4. Выход')
    print('-' * 20)
    choice = input('Выберите пункт меню (цифру): ')
    if choice == '1':
        product = {}
        for feature in features:
            product[feature] = input(f'Введите значение параметра {feature}: ')
        products.append((len(products) + 1, product))
    elif choice == '2':
        for product in products:
            print(product)
    elif choice == '3':
        analytics = {}
        for feature in features:
            analytics[feature] = []
        for product in products:
            for key, value in product[1].items():
                analytics[key].append(value)
        print(analytics)
    elif choice == '4':
        break
    else:
        print('Некорректный ввод, повторите!')

print('Программа завершена')
