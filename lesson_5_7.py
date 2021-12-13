import json


def profits(firms):
    sums = 0
    counts = 0
    for i in firms.values():
        if i > 0:
            sums += i
            counts += 1
    return round(sums / counts)


firms = {}

with open('lesson_5_7.txt') as fr, open('lesson_5_7.json', 'w') as fw:
    firms = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in fr}
    result = [firms, {'average_profit': profits(firms)}]
    print(result)
    json.dump(result, fw)
