# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

print('Задача с монетками')

col = int(input('Введите кол-во монет: '))

order_coins = []

for _ in range(col):
    order_coins.append(int(input('Введите то, как лежат монеты (0-решка, 1-орел): ')))

i_0 = 0
i_1 = 0

for i in range(0, len(order_coins)):
    if order_coins[i] == 0:
        i_0 += 1
    if order_coins[i] == 1:
        i_1 += 1

if (i_0 >= i_1):
    print(f'Минимильное количество монет, которые нужно перевернуть: {col - i_0}')
else:
    print(f'Минимильное количество монет, которые нужно перевернуть: {col - i_1}')


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

print ('Задача про нахождение 2 чисел по их сумме и произведению')

s = int(input('Введите чему равна сумма чисел: '))
p = int(input('Введите чему равно произведение чисел: '))

if s == p == 0:
    print('Числа равны 0')
elif s < 0 and p < 0:
    print('Решений нет')
else:
    descr = s * s - 4 * p

    if descr >= 0:
        import math

        a1 = int((s - math.sqrt(descr)) / 2)
        a2 = int((s + math.sqrt(descr)) / 2)
        b1 = s - a1
        b2 = s - a2

        if a1 == a2:
            print('Ваши числа:')
            print(f'1 число = {a1}, 2 число = {b1}')
        else:
            print('Есть 2 варианта:')
            print(f'1 число = {a1}, 2 число = {b1}')
            print(f'1 число = {a2}, 2 число = {b2}')
    else:
        print('Решений нет')


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

print ('Задача со степенями двойки')

number = int(input('Введите число: '))

num = 1

print ('Все целые степени двойки:')

if number > 0:
    while num <= number:
        print (num)
        num *= 2
else:
    print ('Решений нет')