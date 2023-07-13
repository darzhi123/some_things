from random import choice
import string

print("""Генератор паролей с английской клавиатурой и цифрами. \nВведите количество паролей и количество символов в пароле (более 4 символов):""")

dict1 = dict(numbers = [i for i in string.digits if i not in "01"],
lower_letters = [i for i in string.ascii_lowercase if i not in "lo"],
upper_letters = [i for i in string.ascii_uppercase if i not in "IO"])

def generate_password(length):
    result = [choice(dict1["numbers"]),choice(dict1["lower_letters"]),choice(dict1["upper_letters"])]
    for i in range(length - len(result)):
        dict_item = choice(list(dict1.keys()))
        result.append(choice(dict1[dict_item]))
    return "".join(result)

def generate_passwords(count, length):
    result_list = list()
    for i in range(count):
        result_list.append(generate_password(length))
    return result_list

n, m = map(int, input().split())

print(*generate_passwords(n, m), sep = "\n")

quit()