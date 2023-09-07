Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
>>> def difference(delta,x):
...     denom = np.cos(x+delta) +np.cos(x)
...     num = np.cos(x+delta)**2 + np.sin(x)**2 -1
...     return np.cos(x+delta) - np.cos(x) - (num/denom)
SyntaxError: invalid syntax
def difference(delta,x):
    denom = np.cos(x+delta) +np.cos(x)
    num = np.cos(x+delta)**2 + np.sin(x)**2 -1
    return np.cos(x+delta) - np.cos(x) - (num/denom)

delta = array([1.e-16, 1.e-15, 1.e-14, 1.e-13, 1.e-12, 1.e-11, 1.e-10, 1.e-09,
       1.e-08, 1.e-07, 1.e-06, 1.e-05, 1.e-04, 1.e-03, 1.e-02, 1.e-01,
       1.e+00])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    delta = array([1.e-16, 1.e-15, 1.e-14, 1.e-13, 1.e-12, 1.e-11, 1.e-10, 1.e-09,
NameError: name 'array' is not defined
delta = np.array([1.e-16, 1.e-15, 1.e-14, 1.e-13, 1.e-12, 1.e-11, 1.e-10, 1.e-09,1.e-08, 1.e-07, 1.e-06, 1.e-05, 1.e-04, 1.e-03, 1.e-02, 1.e-01,1.e+00])
                   
x1 = np.pi
                   
x2 = 10**6
                   
def taylor(x, delta, epsilon):
    return -delta*np.sin(x) - (delta**2)*0.5*np.cos(epsilon)

def algorithm(x, delta):
    epsilons = np.linspace(x, x+delta, 100)
    difference = []
    for i in epsilons:
        difference.append((abs(np.cos(x+delta) - np.cos(x) - taylor(x, delta, i)))
    minep = epsilons[difference.index(min(difference))]
                          
SyntaxError: '(' was never closed
def algorithm(x, delta):
    epsilons = np.linspace(x, x+delta, 100)
    difference = []
    for i in epsilons:
        difference.append((abs(np.cos(x+delta) - np.cos(x) - taylor(x, delta, i))))
    minep = epsilons[difference.index(min(difference))]
    return minep

def algorithm(x, delta):
    epsilons = np.linspace(x, x+delta, 100)
    difference = []
    for i in epsilons:
        difference.append((abs(np.cos(x+delta) - np.cos(x) - taylor(x, delta, i))))
    minep = epsilons[difference.index(min(difference))]
    return np.cos(x+delta) - np.cos(x) - taylor(x, delta, minep)

import matplotlib.pyplot as plt
plt.plot(delta, algorithm(x1, delta))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    plt.plot(delta, algorithm(x1, delta))
  File "<pyshell#22>", line 6, in algorithm
    minep = epsilons[difference.index(min(difference))]
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
algorithm(x1, delta)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    algorithm(x1, delta)
  File "<pyshell#22>", line 6, in algorithm
    minep = epsilons[difference.index(min(difference))]
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
def algorithm(x, delta):
    epsilons = np.linspace(x, x+delta, 100)
    difference = []
    for i in epsilons:
        difference.append((abs(np.cos(x+delta) - np.cos(x) - taylor(x, delta, i))))
    minep = difference.all(min(difference))
    print(minep)
    return np.cos(x+delta) - np.cos(x) - taylor(x, delta, minep)

algorithm(x1, delta)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    algorithm(x1, delta)
  File "<pyshell#27>", line 6, in algorithm
    minep = difference.all(min(difference))
AttributeError: 'list' object has no attribute 'all'
def algorithm(x, delta):
    epsilons = np.linspace(x, x+delta, 100)
    difference = []
    for i in epsilons:
        difference.append((abs(np.cos(x+delta) - np.cos(x) - taylor(x, delta, i))))
    mindiff = min(difference)
    indices = [i for i in range(len(difference)) if differences[i] == mindiff]
    minep = epsilons[indices[0]]
    print(minep)
    return np.cos(x+delta) - np.cos(x) - taylor(x, delta, minep)

algorithm(x1, delta)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    algorithm(x1, delta)
  File "<pyshell#30>", line 6, in algorithm
    mindiff = min(difference)
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
def algorithm(x, delta):
    epsilons = np.linspace(x, x+delta, 100)
    difference = []
    for i in epsilons:
        difference.append((abs(np.cos(x+delta) - np.cos(x) - taylor(x, delta, i))))
    print(difference)
    mindiff = min(difference)
    indices = [i for i in range(len(difference)) if differences[i] == mindiff]
    minep = epsilons[indices[0]]
    return np.cos(x+delta) - np.cos(x) - taylor(x, delta, minep)

algorithm(x1, delta)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    algorithm(x1, delta)
  File "<pyshell#33>", line 7, in algorithm
    mindiff = min(difference)
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
def algorithm(x, delta):
    eps = []
    for d in delta:
        epsilons = np.linspace(x, x+d, 100)
        difference = []
        for i in epsilons:
            difference.append((abs(np.cos(x+d) - np.cos(x) - taylor(x, d, i))))
        mindiff = min(difference)
        indices = [i for i in range(len(difference)) if differences[i] == mindiff]
        minep = epsilons[indices[0]]
        eps.append(minep)
    yvals = []
    for i in range(len(delta)):
        yvals.append(np.cos(x+delta[i]) - np.cos(x) - taylor(x, delta[i], eps[i]))
    plt.plot(delta, yvals)

    
algorithm(x1, delta)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    algorithm(x1, delta)
  File "<pyshell#38>", line 9, in algorithm
    indices = [i for i in range(len(difference)) if differences[i] == mindiff]
  File "<pyshell#38>", line 9, in <listcomp>
    indices = [i for i in range(len(difference)) if differences[i] == mindiff]
NameError: name 'differences' is not defined. Did you mean: 'difference'?
def algorithm(x, delta):
    eps = []
    for d in delta:
        epsilons = np.linspace(x, x+d, 100)
        difference = []
        for i in epsilons:
            difference.append((abs(np.cos(x+d) - np.cos(x) - taylor(x, d, i))))
        mindiff = min(difference)
        indices = [i for i in range(len(difference)) if difference[i] == mindiff]
        minep = epsilons[indices[0]]
        eps.append(minep)
    yvals = []
    for i in range(len(delta)):
        yvals.append(np.cos(x+delta[i]) - np.cos(x) - taylor(x, delta[i], eps[i]))
    plt.plot(delta, yvals)

    
algorithm(x1, delta)
def algorithm(x, delta):
    eps = []
    for d in delta:
        epsilons = np.linspace(x, x+d, 100)
        difference = []
        for i in epsilons:
            difference.append((abs(np.cos(x+d) - np.cos(x) - taylor(x, d, i))))
        mindiff = min(difference)
        indices = [i for i in range(len(difference)) if difference[i] == mindiff]
        minep = epsilons[indices[0]]
        eps.append(minep)
    yvals = []
    for i in range(len(delta)):
        yvals.append(np.cos(x+delta[i]) - np.cos(x) - taylor(x, delta[i], eps[i]))
    plt.plot(delta, yvals)
    plt.show()

    
algorithm(x1, delta)
algorithm(x2, delta)
xvals = np.linspace(0,2*np.pi,100)
yvals = cos(xvals + 1) - cos(xvals)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    yvals = cos(xvals + 1) - cos(xvals)
NameError: name 'cos' is not defined
yvals = np.cos(xvals + 1) - np.cos(xvals)
plt.plot(xvals, yvals)
[<matplotlib.lines.Line2D object at 0x00000197D2E7DB50>]
plt.show()
>>> def algorithm(x, delta):
...     eps = []
...     for d in delta:
...         epsilons = np.linspace(x, x+d, 100)
...         difference = []
...         for i in epsilons:
...             difference.append((abs(np.cos(x+d) - np.cos(x) - taylor(x, d, i))))
...         mindiff = min(difference)
...         indices = [i for i in range(len(difference)) if difference[i] == mindiff]
...         minep = epsilons[indices[0]]
...         eps.append(minep)
...     yvals = []
...     for i in range(len(delta)):
...         yvals.append(np.cos(x+delta[i]) - np.cos(x) - taylor(x, delta[i], eps[i]))
...     plt.plot(delta, yvals)
...     plt.xscale('log')
...     plt.show()'
...     
SyntaxError: incomplete input
>>> def algorithm(x, delta):
...     eps = []
...     for d in delta:
...         epsilons = np.linspace(x, x+d, 100)
...         difference = []
...         for i in epsilons:
...             difference.append((abs(np.cos(x+d) - np.cos(x) - taylor(x, d, i))))
...         mindiff = min(difference)
...         indices = [i for i in range(len(difference)) if difference[i] == mindiff]
...         minep = epsilons[indices[0]]
...         eps.append(minep)
...     yvals = []
...     for i in range(len(delta)):
...         yvals.append(np.cos(x+delta[i]) - np.cos(x) - taylor(x, delta[i], eps[i]))
...     plt.plot(delta, yvals)
...     plt.xscale('log')
...     plt.show()
... 
...     
>>> algorithm(x1, delta)
>>> algorithm(x2, delta)
