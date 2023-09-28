Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
x = np.linspace(0, 100, 1000)
import scipy
scipy.integrate.quad(e**(-s**2), 0, x/1.6916)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    scipy.integrate.quad(e**(-s**2), 0, x/1.6916)
NameError: name 'e' is not defined
y = scipy.integrate.quad(np.e**(-s**2), 0, x/1.6916)*(2/np.sqrt(pi))*35 - 15
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    y = scipy.integrate.quad(np.e**(-s**2), 0, x/1.6916)*(2/np.sqrt(pi))*35 - 15
NameError: name 's' is not defined
y = scipy.integrate.quad(np.e**(-x**2), 0, x/1.6916)*(2/np.sqrt(pi))*35 - 15
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    y = scipy.integrate.quad(np.e**(-x**2), 0, x/1.6916)*(2/np.sqrt(pi))*35 - 15
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\scipy\integrate\_quadpack_py.py", line 438, in quad
    flip, a, b = b < a, min(a, b), max(a, b)
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
y = []
for i in x:
    soln = scipy.integrate.quad(np.e**(-x**2), 0, i/1.6916)*(2/np.sqrt(pi))*35 - 15
    y.append(soln)

    
Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    soln = scipy.integrate.quad(np.e**(-x**2), 0, i/1.6916)*(2/np.sqrt(pi))*35 - 15
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\scipy\integrate\_quadpack_py.py", line 465, in quad
    retval = _quad(func, a, b, args, full_output, epsabs, epsrel, limit,
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\scipy\integrate\_quadpack_py.py", line 577, in _quad
    return _quadpack._qagse(func,a,b,args,full_output,epsabs,epsrel,limit)
ValueError: invalid callable given
for i in x:
    soln = scipy.integrate.quad(lambda x: np.e**(-x**2), 0, i/1.6916)*(2/np.sqrt(pi))*35 - 15
    y.append(soln)

    
Traceback (most recent call last):
  File "<pyshell#12>", line 2, in <module>
    soln = scipy.integrate.quad(lambda x: np.e**(-x**2), 0, i/1.6916)*(2/np.sqrt(pi))*35 - 15
NameError: name 'pi' is not defined. Did you mean: 'i'?
for i in x:
    soln = scipy.integrate.quad(lambda x: np.e**(-x**2), 0, i/1.6916)*(2/np.sqrt(np.pi))*35 - 15
    y.append(soln)

    
Traceback (most recent call last):
  File "<pyshell#14>", line 2, in <module>
    soln = scipy.integrate.quad(lambda x: np.e**(-x**2), 0, i/1.6916)*(2/np.sqrt(np.pi))*35 - 15
TypeError: can't multiply sequence by non-int of type 'numpy.float64'
for i in x:
    soln = scipy.integrate.quad(lambda x: np.e**(-x**2), 0, i/1.6916)
    a = soln*(2/np.sqrt(np.pi))*35 - 15
    y.append(soln)

    
Traceback (most recent call last):
  File "<pyshell#16>", line 3, in <module>
    a = soln*(2/np.sqrt(np.pi))*35 - 15
TypeError: can't multiply sequence by non-int of type 'numpy.float64'
for i in x:
    soln = scipy.integrate.quad(lambda x: np.e**(-x**2), 0, i/1.6916)
    print(soln)
    a = as.numeric(soln)*(2/np.sqrt(np.pi))*35 - 15
    y.append(soln)
    
SyntaxError: invalid syntax
for i in x:
    soln = scipy.integrate.quad(lambda x: np.e**(-x**2), 0, i/1.6916)
    print(soln)
    a = (soln)*(2/np.sqrt(np.pi))*35 - 15
    y.append(soln)

    
(0.0, 0.0)
Traceback (most recent call last):
  File "<pyshell#20>", line 4, in <module>
    a = (soln)*(2/np.sqrt(np.pi))*35 - 15
TypeError: can't multiply sequence by non-int of type 'numpy.float64'
for i in x:
    soln = scipy.integrate.quad(lambda x: np.e**(-x**2), 0, i/1.6916)
    a = (soln[0])*(2/np.sqrt(np.pi))*35 - 15
    y.append(a)

                   
y
                   

import matplotlib.pyplot as plt
plt.plot(x, y)
[<matplotlib.lines.Line2D object at 0x000001D9C206B790>]
plt.show()
x = np.linspace(0, 40, 1000)
for i in x:
    soln = scipy.integrate.quad(lambda x: np.e**(-x**2), 0, i/1.6916)
    a = (soln[0])*(2/np.sqrt(np.pi))*35 - 15
    y.append(a)

    
plt.plot(x, y)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    plt.plot(x, y)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\pyplot.py", line 2812, in plot
    return gca().plot(
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_axes.py", line 1688, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_base.py", line 311, in __call__
    yield from self._plot_args(
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_base.py", line 504, in _plot_args
    raise ValueError(f"x and y must have same first dimension, but "
ValueError: x and y must have same first dimension, but have shapes (1000,) and (2000,)
pl
# Problem 1a
                     
x = np.linspace(0, 40, 1000)
                     
y = []
                     
for i in x:
    soln = scipy.integrate.quad(lambda x: np.e**(-x**2), 0, i/1.6916)
    a = (soln[0])*(2/np.sqrt(np.pi))*35 - 15
    y.append(a)

                     
plt.plot(x, y)
                     
[<matplotlib.lines.Line2D object at 0x000001D9C4B1B290>]
plt.show()
                     
[<matplotlib.lines.Line2D object at 0x000001D9C4B1B290>]
                     
SyntaxError: invalid syntax
# Problem 1b
                     

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py", line 83, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py", line 17, in driver
    [astar,ier, numit] = bisection(f,a,b,tol)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py", line 41, in bisection
    fa = f(a)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py", line 7, in <lambda>
    f = lambda x: scipy.integrate.quad(lambda x: np.e**(-x**2), 0, x/1.6916)*(2/np.sqrt(np.pi))*35 - 15
NameError: name 'scipy' is not defined

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py", line 84, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py", line 18, in driver
    [astar,ier, numit] = bisection(f,a,b,tol)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py", line 42, in bisection
    fa = f(a)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py", line 8, in <lambda>
    f = lambda x: scipy.integrate.quad(lambda x: np.e**(-x**2), 0, x/1.6916)*(2/np.sqrt(np.pi))*35 - 15
TypeError: can't multiply sequence by non-int of type 'numpy.float64'

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py
the approximate root is 0.6769550684839487
the error message reads: 0
f(astar) = 1.6577132910811088e-07
the number of iterations is:  31
# Problem 1c
                     
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\fixedpt_example - problem 1.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\fixedpt_example - problem 1.py", line 54, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\fixedpt_example - problem 1.py", line 18, in driver
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\fixedpt_example - problem 1.py", line 42, in fixedpt
    x1 = f(x0)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\fixedpt_example - problem 1.py", line 7, in <lambda>
    f1 = lambda x: scipy.integrate.quad(lambda x: np.e**(-x**2), 0, x/1.6916)[0]*(2/np.sqrt(np.pi))*35 - 15
NameError: name 'scipy' is not defined
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\fixedpt_example - problem 1.py
the approximate fixed point is: -50.0
f1(xstar): -49.99999999999999
Error message reads: 0
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\fixedpt_example - problem 1.py
the approximate fixed point is: 20.0
f1(xstar): 20.000000000000007
Error message reads: 0
>>> #Problem 1b
...                      
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py
the approximate root is 0.6769550601503482
the error message reads: 0
f(astar) = 1.20614629395277e-12
the number of iterations is:  48
