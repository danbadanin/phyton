with open('lesson_5_1.txt', 'w') as f:
    while True:
        new_line = input('Введите строку для сохранения в файл, для выхода отправьте пустую строку: ')
        if new_line == '':
            break
        f.write(new_line + '\n')

print('Запись окончена!')
