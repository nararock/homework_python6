# Задача: Реализовать структуру «Рейтинг», представляющую собой не
# возрастающий набор натуральных чисел. У пользователя необходимо
# запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
# одинаковыми значениями, то новый элемент с тем же значением должен
# разместиться после них.
numb = 5
my_list1 = list(range(0, 100000))
my_list1.sort(reverse=True)
my_list2 = list(range(0, 100000))
my_list2.sort(reverse=True)

"""Первое решение задачи."""


def solution1(number, list_numb):
    counter = 0
    min_element = min(list_numb)
    if number <= min_element:
        list_numb.append(number)
    else:
        for el in list_numb:
            counter += 1
            if el < number:
                list_numb.insert(counter - 1, number)
                break
    return list_numb


"""Второе решение. Весь алгоритм заменяется на встроенную функцию sorted().
Средняя величина времени работы при 1000 повторений уменьшилась в разы: 
6.35 сек (первое решение) против 0.61 сек (второе решение). Тест находится 
в файле test_task1_1.py"""


def solution2(num, list_numb):
    list_numb.append(num)
    list_numb.sort(reverse=True)
    return list_numb


# solution1(5, my_list1)
# solution2(5, my_list2)
