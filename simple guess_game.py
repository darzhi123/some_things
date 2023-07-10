import random

print("Игра Угадай число")
number_from, number_to = map(
    int, input("Введите ограничения для числа: от и до: ").split()
)
number_from, number_to = min(number_from, number_to), max(number_from, number_to)

number = random.randrange(number_from, number_to + 1)
tries = 0

guess = int(input("Введите свою догадку насчет загаданного числа: "))
while guess != number:
    if guess > number:
        print("Введенное вами число больше загаданного числа")
    else:
        print('Введенное вами число меньше загаданного числа')
    guess = int(input("Введите свою догадку насчет загаданного числа: "))
    tries += 1
if guess == number:
    print('Поздравляем, вы угадали загаданное число!')
    print(f'Это у вас заняло {tries} попыток.')
exit()