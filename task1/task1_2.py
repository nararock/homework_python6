# Задача:  Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

""" Первое решение задачи."""


def get_sum(var_1, var_2, var_3):
    my_list = [var_1, var_2, var_3]
    max_1 = max(my_list)
    my_list.remove(max_1)
    max_2 = max(my_list)
    return max_1 + max_2


"""Второе решение. Вместо двойного поиска максимума осуществляется
один поиск минимума. Исключена операция удаления элемента. Средняя величина 
времени работы при 1000000 повторений 0.043 с (второе решение) против 
0.057 сек (первое решение). Тест находится в файле test_task1_2.py"""


def get_sum_new(var_1, var_2, var_3):
    my_list = [var_1, var_2, var_3]
    min_elem = min(my_list)
    return sum(my_list) - min_elem


# print(get_sum(2, 7, 56))
# print(get_sum_new(2, 7, 56))
