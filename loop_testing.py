import time 
import sys
start = time.time()

a= [i for i in range(10000000)]
b= [i for i in range(10000000,20000000)]

c=[]


print(sys.getsizeof(a))
# for i in range(len(a)):
#     c.append(a[i]+b[i])


# print(c)
# print(time.time()- start)