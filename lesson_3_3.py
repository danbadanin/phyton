def my_func(*args):
    args = list(args)
    args.sort(reverse=True)
    sums = args[0] + args[1]
    return sums


numbers = []
for i in range(3):
    numbers.append(float(input(f'Введите {i+1} число: ')))

print(my_func(*numbers))
