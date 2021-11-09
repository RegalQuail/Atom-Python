import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # x-values
y = np.array([0.0098, 0.0197, 0.0296, 0.0404, 0.0504, 0.0604, 0.0702, 0.0804,
             0.0903, 0.1007]) # y-values

slope, intercept, r, p, std_err = stats.linregress(x, y) # important key values for linear regression

def myfunction(x):
    return slope * x + intercept # 

mymodel = list(map(myfunction, x))

plt.xlabel("Volt [U]")
plt.ylabel("Amper [I]")

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
print(r)
print(slope)
print(intercept)
