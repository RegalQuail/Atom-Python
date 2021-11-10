import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


x = np.array([0.2, 0.4, 0.6, 0.8, 1]) # x-values
y = np.array([2.156626506, 4.369696970, 6.876832845, 8.673400673, 10.41015625]) # y-values

slope, intercept, r, p, std_err = stats.linregress(x, y) # important key values for linear regression

def myfunction(x):
    return slope * x + intercept

mymodel = list(map(myfunction, x))

plt.xlabel("Length [m]")
plt.ylabel("Resistivity [R]")
plt.text(0.7, 4, slope)

plt.scatter(x, y)
plt.plot(x, mymodel, color='r')
plt.show()
print(r) # coefficient of correlation
print(slope) # a
print(intercept) # b
