from timeit import timeit

print(timeit("solution1(numb, my_list1)", setup="from task1_1 import "
                                                "solution1, "
                                                "numb, my_list1", number=1000))
print(timeit("solution2(numb, my_list2)", setup="from task1_1 import "
                                                "solution2, "
                                                "numb, my_list2", number=1000))
