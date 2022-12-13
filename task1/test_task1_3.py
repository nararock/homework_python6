from timeit import timeit
from memory_profiler import profile

print(timeit("check_day1(my_day)", setup="from task1_3 import check_day1, "
                                         "my_day", number=1000000))
print(timeit("check_day2(my_day)", setup="from task1_3 import check_day2, "
                                         "my_day", number=1000000))
