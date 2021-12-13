def sums(*args):
    result = 0
    for i in range(len(args)):
        count = args[i].split('(')
        if len(count) > 1:
            result += int(count[0])
    return result


lessons = {}

with open('lesson_5_6.txt', 'r') as f:
    for line in f:
        name, *args = line.split()
        lessons[name] = sums(*args)

print(lessons)
