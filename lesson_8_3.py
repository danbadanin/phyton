class ValuesError(Exception):
    def __init__(self, txt):
        self.txt = txt


lists = []
check_list = list(map(str, range(10)))

while True:
    new_element = input('Введите элеменет списка, для выхода введите "stop": ')
    if new_element == 'stop':
        break
    try:
        for i in range(len(new_element)):
            if new_element[i] not in check_list:
                raise ValuesError('Необходимо вводить только числа!')
        lists.append(int(new_element))
    except ValuesError as err:
        print(err.txt)

print(f'{lists} - итоговый список')
