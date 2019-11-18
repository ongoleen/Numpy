import numpy as np
x = np.random.random ((5,5))
print ('x = ')
print (x)
z = (x-np.mean(x))/np.std(x) 
print ('Normalized x = ')
print (z)
np.save('X_normalized', z)