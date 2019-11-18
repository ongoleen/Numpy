import numpy as np
a = np.zeros((10,10))
x = 1
for y in range (10):
    for z in range(10):
        a[y,z] = x**2
        x += 1
A = np.int64(a)
print ('A = ')
print (A)
aa = a[a%3 == 0]
aa.resize(3,11)
AA = np.int64(aa)
print ('Elements Divisible by 3 = ')
print (AA)
np.save('div_by_3', AA)