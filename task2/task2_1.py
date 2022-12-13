from memory_profiler import profile

# Задача:Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.

list1 = list(range(1, 100000))
list2 = list(range(1, 100000))

"""Первое решение. Есть инкремент памяти."""


@profile
def get_sum1(my_list):
    new_list = []
    for j in range(1, len(my_list), 2):
        new_list.append(my_list[j])
    my_sum = sum(new_list)
    return my_sum


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    12     29.7 MiB     29.7 MiB           1   @profile
    13                                         def get_sum1(my_list):
    14     29.7 MiB      0.0 MiB           1       new_list = []
    15     30.7 MiB      0.0 MiB       50000       for j in range(1, len(my_list), 2):
    16     30.7 MiB      1.0 MiB       49999           new_list.append(my_list[j])
    17     30.7 MiB      0.0 MiB           1       my_sum = sum(new_list)
    18     30.7 MiB      0.0 MiB           1       return my_sum
"""

"""Второе решение. Использован генератор. Не происходит инкремента памяти."""


@profile
def get_sum2(my_list):
    generator = (my_list[i] for i in
                 range(1, len(my_list), 2))
    return sum(generator)


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    24     29.7 MiB     29.7 MiB           1   @profile
    25                                         def get_sum2(my_list):
    26     29.7 MiB      0.0 MiB      100002       generator = (my_list[i] for i in
    27     29.7 MiB      0.0 MiB           1                    range(1, len(my_list), 2))
    28     29.7 MiB      0.0 MiB           1       return sum(generator)

"""

print(get_sum1(list1))
print(get_sum2(list2))
