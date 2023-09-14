Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> def algo(x):
...     y = math.e^x
...     return y -1
... 
>>> x1 = 9.999999995000000 * 10**(-10)
>>> algo(x1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    algo(x1)
  File "<pyshell#4>", line 2, in algo
    y = math.e^x
TypeError: unsupported operand type(s) for ^: 'float' and 'float'
>>> def algo(x):
...     y = math.e**x
...     return y -1
... 
>>> algo(x1)
1.000000082740371e-09
>>> def taylor(x1)
SyntaxError: incomplete input
>>> def taylor(x):
...     term1 = x
...     term2 = 0.5*x**2
...     term3 = x**3 * (1/6)
...     term4 = x**4 * (1/24)
...     return term1 + term2 + term3 + term4
... 
>>> taylor(x1)
1e-09
>>> def taylor(x):
...     term1 = x
...     term2 = 0.5*x**2
...     term3 = x**3 * (1/6)
...     term4 = x**4 * (1/24)
...     return term1 + term2 + term3
... 
taylor(x1)
1e-09
def taylor(x):
    term1 = x
    term2 = 0.5*x**2
    term3 = x**3 * (1/6)
    term4 = x**4 * (1/24)
    return term1 + term2

taylor(x1)
1e-09
def taylor(x):
    term1 = x
    term2 = 0.5*x**2
    term3 = x**3 * (1/6)
    term4 = x**4 * (1/24)
    return term1

taylor(x1)
9.999999995e-10
def taylor(x):
    term1 = x
    term2 = 0.5*x**2
    term3 = x**3 * (1/6)
    term4 = x**4 * (1/24)
    return term1 + term2

import numpy as np
n
np.expm1
<ufunc 'expm1'>
np.expm1(0)
0.0
taylor(0)
0.0
# Problem 4 - Practicing Python
#(a)
t = np.arange(0, np.pi, np.pi/30)
y = np.cos(t)
N = len(y)
sum = 0
for i in range(N):
    sum = sum + t[i]*y[i]

    
sum
-17.545259710757044
print("the sum is: ", sum)
the sum is:  -17.545259710757044
# (b)
def parametricx(R, deltar, f, p, theta):
    return R*(1+deltar*np.sin(f*theta +p))*np.cos(theta)

def parametricy(R, deltar, f, p, theta):
    return R*(1+deltar*np.sin(f*theta +p))*np.sin(theta)

theta = np.linspace(0, 2*np.pi, num = 100)
y = []
x = []
for i in theta:
    y.append(parametricy(1.2, 0.1, 15, 0, i))
    x.append(parametricx(1.2, 0.1, 15, 0, i))

    
import matplotlib.pyplot as plt
plt.plot(theta, y)
[<matplotlib.lines.Line2D object at 0x0000025A4B1F4A10>]
plt.plot(theta, x)
[<matplotlib.lines.Line2D object at 0x0000025A4B4708D0>]
plt.show()
for i in range(10):
    R = i
    deltar = 0.05
    f = 2+i
    p = random.uniform(0,2)
    y = []
    x = []
    for v in theta:
        y.append(parametricy(R, deltar, f, p, v))
        x.append(parametricx(R, deltar, f, p, v))
    plt.plot(theta, y)
    plt.plot(theta, x)

    
Traceback (most recent call last):
  File "<pyshell#78>", line 5, in <module>
    p = random.uniform(0,2)
NameError: name 'random' is not defined
import random
for i in range(10):
    R = i
    deltar = 0.05
    f = 2+i
    p = random.uniform(0,2)
    y = []
    x = []
    for v in theta:
        y.append(parametricy(R, deltar, f, p, v))
        x.append(parametricx(R, deltar, f, p, v))
    plt.plot(theta, y)
    plt.plot(theta, x)

    
[<matplotlib.lines.Line2D object at 0x0000025A4B5DD1D0>]
[<matplotlib.lines.Line2D object at 0x0000025A52F35010>]
[<matplotlib.lines.Line2D object at 0x0000025A52F34E50>]
[<matplotlib.lines.Line2D object at 0x0000025A52F451D0>]
[<matplotlib.lines.Line2D object at 0x0000025A52F44DD0>]
[<matplotlib.lines.Line2D object at 0x0000025A52F46850>]
[<matplotlib.lines.Line2D object at 0x0000025A52F47310>]
[<matplotlib.lines.Line2D object at 0x0000025A52F47D50>]
[<matplotlib.lines.Line2D object at 0x0000025A52F44F90>]
[<matplotlib.lines.Line2D object at 0x0000025A4B5F75D0>]
[<matplotlib.lines.Line2D object at 0x0000025A52F50F50>]
[<matplotlib.lines.Line2D object at 0x0000025A52F519D0>]
[<matplotlib.lines.Line2D object at 0x0000025A52F524D0>]
[<matplotlib.lines.Line2D object at 0x0000025A52F53DD0>]
[<matplotlib.lines.Line2D object at 0x0000025A52F53C90>]
[<matplotlib.lines.Line2D object at 0x0000025A52F653D0>]
[<matplotlib.lines.Line2D object at 0x0000025A52F65010>]
[<matplotlib.lines.Line2D object at 0x0000025A52F66910>]
[<matplotlib.lines.Line2D object at 0x0000025A52F67410>]
[<matplotlib.lines.Line2D object at 0x0000025A52F67F10>]

plt.show()
y = []
x = []
for i in theta:
    y.append(parametricy(1.2, 0.1, 15, 0, i))
    x.append(parametricx(1.2, 0.1, 15, 0, i))
    
SyntaxError: multiple statements found while compiling a single statement
y = []
x = []
y = []
x = []
for i in theta:
    y.append(parametricy(1.2, 0.1, 15, 0, i))
    x.append(parametricx(1.2, 0.1, 15, 0, i))
    
SyntaxError: multiple statements found while compiling a single statement
for i in theta:
    y.append(parametricy(1.2, 0.1, 15, 0, i))
    x.append(parametricx(1.2, 0.1, 15, 0, i))

    
plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x0000025A52FE92D0>]
plt.show()
for i in range(10):
    R = i
    deltar = 0.05
    f = 2+i
    p = random.uniform(0,2)
    y = []
    x = []
    for v in theta:
        y.append(parametricy(R, deltar, f, p, v))
        x.append(parametricx(R, deltar, f, p, v))
    plt.plot(x, y)

    
[<matplotlib.lines.Line2D object at 0x0000025A542AF550>]
[<matplotlib.lines.Line2D object at 0x0000025A4B54BA50>]
[<matplotlib.lines.Line2D object at 0x0000025A4B5D3650>]
[<matplotlib.lines.Line2D object at 0x0000025A542BC3D0>]
[<matplotlib.lines.Line2D object at 0x0000025A542BCCD0>]
[<matplotlib.lines.Line2D object at 0x0000025A542BD910>]
[<matplotlib.lines.Line2D object at 0x0000025A542BE4D0>]
[<matplotlib.lines.Line2D object at 0x0000025A542BEFD0>]
[<matplotlib.lines.Line2D object at 0x0000025A542BCE90>]
[<matplotlib.lines.Line2D object at 0x0000025A542CC610>]
plt.show()

= RESTART: C:\Users\cambr\Downloads\bisection_example.py
the approximate root is 0.9999999701976776
the error message reads: 0
f(astar) = -2.98023206113385e-08
a = [[1,1],[1+10**(-10), 1-10**(-10)]]
cond(A)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    cond(A)
NameError: name 'cond' is not defined. Did you mean: 'round'?
cond(a)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    cond(a)
NameError: name 'cond' is not defined. Did you mean: 'round'?
np.cond(a)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    np.cond(a)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\__init__.py", line 328, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'cond'. Did you mean: 'conj'?
np.linalg.cond(a)
                         
19999973849.225224
