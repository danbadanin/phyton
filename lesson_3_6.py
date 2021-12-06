def int_func(word: str):
    return word.capitalize()


def int_func_2(*words):
    result = ''
    for i in range(len(words)):
        result += int_func(words[i]) + ' '
    return result


string = input('Введите слово: ')
print(int_func(string))

string_2 = input('Введите слова через пробел: ')
print(int_func_2(*string_2.split()))
