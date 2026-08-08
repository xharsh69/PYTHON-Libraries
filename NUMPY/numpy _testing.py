import numpy as np 
import time
import sys

start = time.time()

a=np.arange(10000000, dtype=np.int16)
b=np.arange(10000000,20000000)

print(sys.getsizeof(a))

c= a+b
print(time.time()- start)