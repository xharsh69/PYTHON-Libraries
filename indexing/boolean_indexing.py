import numpy as np 


# a= np.random.randint(1,100,24).reshape(6,4)


# print(a)

# print(a[(a%7==0) & (a>50)])

a= np.array([1,2,3,4,np.nan,5,6])

print(a[~np.isnan(a)])