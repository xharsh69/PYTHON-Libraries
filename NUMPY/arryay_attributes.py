import numpy as np 

a= np.arange(10,dtype= np.int16)
b=np.arange(12, dtype=float).reshape(3,4)
c = np.arange(8).reshape(2,2,2)


# print(c.ndim)
# print(b.shape)
# print(a.size)

print(b.itemsize)

print(a.dtype)