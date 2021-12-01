user_string = input('Введите строку из нескольких слов: ')
user_list = user_string.split(' ')
for index, word in enumerate(user_string.split(' ')):
    print(index, word[:10])
