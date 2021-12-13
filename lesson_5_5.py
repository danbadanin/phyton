with open('lesson_5_5.txt', 'w+') as f:
    f.write('5 10 6 32 54 9')
    f.seek(0)
    content = sum(map(int, f.read().split()))
    print(content)

