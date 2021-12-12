from random import randint

main_list = [randint(0, 200) for _ in range(10)]
new_list = [main_list[i] for i in range(1, len(main_list)) if main_list[i] > main_list[i-1]]

print(f'Исходный список: {main_list}')
print(f'Норвый список: {new_list}')
