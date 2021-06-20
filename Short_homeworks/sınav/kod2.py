"""
def zeta(number):
    N = 1000
    sum = 0
    for i in range(1, N+1):
        sum += pow(i, -number)
    return sum

for i in [1.5,2,4]:
    print("f({}) = ".format(i), zeta(i))
"""
"""
%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
x = np.linspace(0, 1, 100)
y = x**2 + 1
plt.figure(figsize(1000,1000), dpi=1)
plt.plot(x, y, 'r')
plt.show()
"""
"""
%matplotlib inline
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def f(x):
    return x**2+1

X = np.arange(101,1001,10001)
def F(x):
    res = np.zeros_like(x)
    for i,val in enumerate(x):
        y,err = integrate.quad(f,0,val)
        res[i]=y
    for i in res:
        print(i)
    return res

plt.plot(X,F(X))
"""
"""

%matplotlib inline
import numpy
import matplotlib.pyplot as plt

def derivative(f,a,h=0.001):
    return (f(a + h) - f(a - h))/(2*h)

f = lambda E :1/(numpy.exp((E-0)/ 8.61733034 * 10*(-5)*300)+1)

x = np.linspace(-0.25,0.25,100)
plt.plot(x, f(x))
plt.title('Fermi-Dirac function')
plt.xlabel('E')
plt.ylabel('Value')
plt.show()


plt.plot(x, derivative(f, x))
plt.title('Fermi-Dirac function\'s derivative' )
plt.xlabel('E')
plt.ylabel('Value')
plt.show()
"""
