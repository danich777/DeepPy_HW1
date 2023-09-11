# 2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник
# разносторонним, равнобедренным или равносторонним.

a = int(input("Введите сторону а: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует ")
    if a == b and b == c and a == c:
        print("треугольник - равносторонний")
    elif a == b or b == c or a == c:
        print("треугольник - равнобедренный")
    else:
        print("треугольник - разносторонний")
else:
    print("Треугольник не существует")




# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только
# на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

a = int(input("Введите число от 0 до 100000 включительно: "))
while not 0 < a < 100001:
    a = int(input("Введите число от 0 до до 100000 включительно: "))
if a == 1 or a == 0:
    print("Число не является ни простым, ни составным.")

k = 0
for i in range(2, a):
    if (a% i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число составное")


# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

lower_limit = 0
upper_limit = 1000
number_attempts = 10
counter = 0
num = randint(lower_limit, upper_limit)

while counter < number_attempts:
#    print (num)
    counter += 1
    entered_number = int(input("Введите число больше 0 и меньше 1000: "))

    if num == entered_number:
        print("Вы угадали!")
        break
    elif num > entered_number:
        print("Загаданное число больше")
        print(f"Осталось попыток {10 - counter}")
        upper_limit = num - 1
    else:
        print("Загаданное число меньше")
        print(f"Осталось попыток {10 - counter}")
        lower_limit = num + 1

else:
    print("Попытки исчерпаны")
    counter = -1