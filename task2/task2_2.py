from memory_profiler import profile

# Задача: Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
"""Первое решение. Есть инкремент памяти."""


@profile
def func1(my_list):
    size = len(my_list)
    new_list = []
    for i in range(size - 1):
        if not i % 2:
            new_list.append(my_list[i + 1])
        else:
            new_list.append(my_list[i - 1])
    if size % 2:
        new_list.append(my_list[size - 1])
    return new_list


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     7     29.7 MiB     29.7 MiB           1   @profile
     8                                         def func1(my_list):
     9     29.7 MiB      0.0 MiB           1       size = len(my_list)
    10     29.7 MiB      0.0 MiB           1       new_list = []
    11     30.9 MiB      0.0 MiB       99999       for i in range(size - 1):
    12     30.9 MiB      0.0 MiB       99998           if not i % 2:
    13     30.9 MiB      1.1 MiB       49999               new_list.append(my_list[i + 1])
    14                                                 else:
    15     30.9 MiB      0.0 MiB       49999               new_list.append(my_list[i - 1])
    16     30.9 MiB      0.0 MiB           1       if size % 2:
    17     30.9 MiB      0.0 MiB           1           new_list.append(my_list[size - 1])
    18     30.9 MiB      0.0 MiB           1       return new_list
"""

"""Второе решение. Все обмены элементами происходят в одно списке, 
второй список не создается."""


@profile
def func2(my_list):
    size = len(my_list)
    for i in range(0, size - 1, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    return my_list


"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    25     29.7 MiB     29.7 MiB           1   @profile
    26                                         def func2(my_list):
    27     29.7 MiB      0.0 MiB           1       size = len(my_list)
    28     29.7 MiB      0.0 MiB       50000       for i in range(0, size - 1, 2):
    29     29.7 MiB      0.0 MiB       49999           my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    30     29.7 MiB      0.0 MiB           1       return my_list
"""

list1 = list(range(1, 100000))
list2 = list(range(1, 100000))

func1(list1)
func2(list2)
