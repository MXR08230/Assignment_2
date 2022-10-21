import numpy as np
a=np.random.randint(1,20,15)
print("array")
print(a)
a=a.reshape(3,5)
print("reshapped array")
print(a)
print("array shape")
print(a.shape)
print("max of array")
print(a.max())
print("array with replaced max value")
a[a==a.max()]=0
print(a)