lists = []

while True:
    element = input('Введите элемент списка, для завершения ввода наберите "exit": ')
    if element == 'exit':
        break
    lists.append(element)

i = 1
while i < len(lists):
    lists[i-1], lists[i] = lists[i], lists[i-1]
    i += 2

print(lists)
