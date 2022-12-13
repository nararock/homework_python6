import math

# Задача: Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
number = 30

"""Первое решение задачи."""


def multi1(num):
    m = range(1, num + 1)
    result = []
    ans = 1
    for el in m:
        for i in range(1, el + 1):
            ans *= i
        result.append(ans)
        ans = 1
    return result


"""Второе решение. Циклы заменены на встроеннную функцию factorial() и
конструкцию LC. Среднее время выполнения при 100000 повторений 2,8 сек 
(первая функция) против 0,5 сек (вторая функция). Тест находится в файле 
test_task1_4.py"""


def multi2(num):
    result = [math.factorial(elem) for elem in range(1, num + 1)]
    return result

# print(multi1(30))
# print(multi2(30))
