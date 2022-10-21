
import numpy as np
m1 = np.random.randint(1,20,15)
print("Array")
print(m1)
#1. Reshape the array to 3 by 5
m2=np.reshape(m1,(3,5))
print("Reshaped Array")
print(m2)
#Print array shape.
print("Array Shape")
print(m2.shape)
#Replace the max in each row by 0
index = m2.argmax(axis=1)
print("indexes of max values in array")
print(index)
print("Array with replaced max value")
m2[0][index[0]] = 0
m2[1][index[1]] = 0
m2[2][index[2]] =0
print(m2)