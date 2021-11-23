import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


x = np.array([66, 49, 43, 34, 30, 27]) # x-values
y = np.array([[3.8, 3.69, 3.54, 3.48, 3.42, 3.41]]) # y-values

slope, intercept, r, p, std_err = stats.linregress(x, y) # important key values for linear regression

def myfunction(x):
    return slope * x + intercept

mymodel = list(map(myfunction, x))

plt.xlabel("Delta T [Celcius]")
plt.ylabel("Resistivity [Ohm]")
plt.text(0.7, 4, slope)

plt.scatter(x, y)
plt.plot(x, mymodel, color='r')
plt.show()
print(r) # coefficient of correlation
print(slope) # a
print(intercept) # b
