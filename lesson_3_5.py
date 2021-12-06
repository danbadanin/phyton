def sums(*nums, index):
    result = 0
    # Для выполнения условия, когда специальный символ в самом начале
    if type(index) == int:
        for i in range(index):
            result += float(nums[i])
    else:
        for i in range(len(nums)):
            result += float(nums[i])
    return result


total = 0

while True:
    string = input('Введите числа, разделенные пробелом. Для выхода введите "Q": ')
    list_of_nums = string.upper().split()
    try:
        exit_index = list_of_nums.index('Q')
    except ValueError:
        exit_index = None

    total += sums(*list_of_nums, index=exit_index)
    print(total)

    if type(exit_index) == int:
        break

print('Программа завершена!')
