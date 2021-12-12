from random import randint

main_list = [randint(0, 20) for _ in range(10)]
new_list = [el for el in main_list if main_list.count(el) == 1]

print(main_list)
print(new_list)
