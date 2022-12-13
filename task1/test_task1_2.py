from timeit import timeit

print(timeit("get_sum(1, 2, 5)", setup="from task1_2 import get_sum",
             number=100000))
print(timeit("get_sum_new(1, 2, 5)", setup="from task1_2 import get_sum_new",
             number=100000))
