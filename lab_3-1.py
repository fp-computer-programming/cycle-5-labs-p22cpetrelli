# author CJP 10/21/2021
import math
import time

t0 = time.perf_counter()
math.pow(2,2)
t1 = time.perf_counter()
process_time = t1 - t0
print(process_time)

t2 = time.perf_counter()
2 ** 2
t3 = time.perf_counter()
process_time2 = t3 - t2
print(process_time2)