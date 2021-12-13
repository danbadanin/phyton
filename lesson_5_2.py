with open('lesson_5_2.txt', 'r') as f:
    for i, line in enumerate(f):
        print(f'В строке {i+1} содержится {len(line.split())} слов')
