my_list = [7, 5, 3, 3, 2]

while True:
    new_element = input('Введите число для добавления в рейтинг, для выхода введите "exit": ')

    if new_element == 'exit' or new_element == '':
        break

    my_list.append(int(new_element))
    my_list.sort(reverse=True)
    print(my_list)
