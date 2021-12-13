numbers = ('0', 'Один', 'Два', 'Три', 'Четрые')

with open('lesson_5_4.txt', 'r') as fr, open('lesson_5_4_w.txt', 'w') as fw:
    for line in fr:
        _, num = line.split(' - ')
        fw.write(numbers[int(num)] + ' - ' + num)
