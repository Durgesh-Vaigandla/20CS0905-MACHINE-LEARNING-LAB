import numpy as np
import matplotlib.pyplot as plt
x = np.array([0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10])
y = np.array([10 , 9 , 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 0])
m = (((np.mean(x)*np.mean(y)) - np.mean(x*y)) / ((np.mean(x)*np.mean(x)) - np.mean(x*x)))
b = np.mean(y) - m*np.mean(x)
plt.plot(x, y, 'ro')
plt.plot(x, m*x + b)
plt.show()