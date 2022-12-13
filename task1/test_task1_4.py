from timeit import timeit


print(timeit("multi1(number)", setup="from task1_4 import multi1, number",
             number=100000))
print(timeit("multi2(number)", setup="from task1_4 import multi2, number",
             number=100000))
