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

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\fixedpt_example - problem 1.py
the approximate fixed point is: -50.0
f1(xstar): -49.99999999999999
Error message reads: 0

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\fixedpt_example - problem 1.py
the approximate fixed point is: 20.0
f1(xstar): 20.000000000000007
Error message reads: 0
#Problem 1b
                     

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\bisection_example - problem 1.py
the approximate root is 0.6769550601503482
the error message reads: 0
f(astar) = 1.20614629395277e-12
the number of iterations is:  48
#Problem 5a
                     

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example.py", line 3, in <module>
    from tabulate import tabulate
ModuleNotFoundError: No module named 'tabulate'

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example.py
the approximate root is 1.1347241384015194e+00
the error message reads: 0
Number of iterations: 8
+-------------+--------------+
|   Iteration |        Error |
+=============+==============+
|           0 | -0.865276    |
+-------------+--------------+
|           1 | -0.545904    |
+-------------+--------------+
|           2 | -0.296015    |
+-------------+--------------+
|           3 | -0.120247    |
+-------------+--------------+
|           4 | -0.0268143   |
+-------------+--------------+
|           5 | -0.00162914  |
+-------------+--------------+
|           6 | -6.38994e-06 |
+-------------+--------------+
|           7 | -9.87017e-11 |
+-------------+--------------+
|           8 |  0           |
+-------------+--------------+
|           9 |  0           |
+-------------+--------------+

===================================== RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example.py =====================================
the approximate root is 1.1347241384015194e+00
the error message reads: 0
Number of iterations: 8
╒═════════════╤══════════════╕
│   Iteration │        Error │
╞═════════════╪══════════════╡
│           0 │ -0.865276    │
├─────────────┼──────────────┤
│           1 │ -0.545904    │
├─────────────┼──────────────┤
│           2 │ -0.296015    │
├─────────────┼──────────────┤
│           3 │ -0.120247    │
├─────────────┼──────────────┤
│           4 │ -0.0268143   │
├─────────────┼──────────────┤
│           5 │ -0.00162914  │
├─────────────┼──────────────┤
│           6 │ -6.38994e-06 │
├─────────────┼──────────────┤
│           7 │ -9.87017e-11 │
├─────────────┼──────────────┤
│           8 │  0           │
╘═════════════╧══════════════╛
# Secant method
                     

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py =
Traceback (most recent call last):
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 74, in <module>
    driver()
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 15, in driver
    (p, pstar, ier, count) = secant(p0, p1, f, tol, Nmax)
UnboundLocalError: cannot access local variable 'secant' where it is not associated with a value

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py =
the approximate root is 1.0161290322580645e+00
Traceback (most recent call last):
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 74, in <module>
    driver()
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 17, in driver
    print('the error message reads:', '%d' % info)
NameError: name 'info' is not defined

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py =
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
+-----------+----------------------+
| Iteration |        Error         |
+-----------+----------------------+
|     0     | 0.016129032258064502 |
|     1     |  1.0161290322580645  |
+-----------+----------------------+

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py =
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
+-----------+---------------------+
| Iteration |        Error        |
+-----------+---------------------+
|     0     | -0.9838709677419355 |
|     1     | 1.0161290322580645  |
+-----------+---------------------+

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py =
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
+-----------+---------------------+
| Iteration |        Error        |
+-----------+---------------------+
|     0     | -0.9838709677419355 |
|     1     |         0.0         |
+-----------+---------------------+

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py =
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
╒═════════════╤═══════════╕
│   Iteration │     Error │
╞═════════════╪═══════════╡
│           0 │ -0.983871 │
├─────────────┼───────────┤
│           1 │  0        │
╘═════════════╧═══════════╛
# Problem 5b
                     

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
╒═════════════╤═══════════╕
│   Iteration │     Error │
╞═════════════╪═══════════╡
│           0 │ -0.983871 │
├─────────────┼───────────┤
│           1 │  0        │
╘═════════════╧═══════════╛
Traceback (most recent call last):
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 96, in <module>
    driver()
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 40, in driver
    x1.append((i+1)[0])
TypeError: can only concatenate list (not "int") to list

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
╒═════════════╤═══════════╕
│   Iteration │     Error │
╞═════════════╪═══════════╡
│           0 │ -0.983871 │
├─────────────┼───────────┤
│           1 │  0        │
╘═════════════╧═══════════╛
Traceback (most recent call last):
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 96, in <module>
    driver()
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 40, in driver
    x1.append(mydata[(i+1)][0])
IndexError: list index out of range

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
╒═════════════╤═══════════╕
│   Iteration │     Error │
╞═════════════╪═══════════╡
│           0 │ -0.983871 │
├─────────────┼───────────┤
│           1 │  0        │
╘═════════════╧═══════════╛
Traceback (most recent call last):
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 99, in <module>
    driver()
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 45, in driver
    plt.plot.loglog(xn, yn)
AttributeError: 'function' object has no attribute 'loglog'

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
╒═════════════╤═══════════╕
│   Iteration │     Error │
╞═════════════╪═══════════╡
│           0 │ -0.983871 │
├─────────────┼───────────┤
│           1 │  0        │
╘═════════════╧═══════════╛

Warning (from warnings module):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1520.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 861
    func(*args)
UserWarning: Data has no positive values, and therefore cannot be log-scaled.

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
╒═════════════╤══════════╕
│   Iteration │    Error │
╞═════════════╪══════════╡
│           0 │ 0.983871 │
├─────────────┼──────────┤
│           1 │ 0        │
╘═════════════╧══════════╛

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example.py
the approximate root is 1.1347241384015194e+00
the error message reads: 0
Number of iterations: 8
╒═════════════╤═════════════╕
│   Iteration │       Error │
╞═════════════╪═════════════╡
│           0 │ 0.865276    │
├─────────────┼─────────────┤
│           1 │ 0.545904    │
├─────────────┼─────────────┤
│           2 │ 0.296015    │
├─────────────┼─────────────┤
│           3 │ 0.120247    │
├─────────────┼─────────────┤
│           4 │ 0.0268143   │
├─────────────┼─────────────┤
│           5 │ 0.00162914  │
├─────────────┼─────────────┤
│           6 │ 6.38994e-06 │
├─────────────┼─────────────┤
│           7 │ 9.87017e-11 │
├─────────────┼─────────────┤
│           8 │ 0           │
╘═════════════╧═════════════╛
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example.py", line 81, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example.py", line 44, in driver
    plt.loglog(xn, yn)
NameError: name 'plt' is not defined

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example.py
the approximate root is 1.1347241384015194e+00
the error message reads: 0
Number of iterations: 8
╒═════════════╤═════════════╕
│   Iteration │       Error │
╞═════════════╪═════════════╡
│           0 │ 0.865276    │
├─────────────┼─────────────┤
│           1 │ 0.545904    │
├─────────────┼─────────────┤
│           2 │ 0.296015    │
├─────────────┼─────────────┤
│           3 │ 0.120247    │
├─────────────┼─────────────┤
│           4 │ 0.0268143   │
├─────────────┼─────────────┤
│           5 │ 0.00162914  │
├─────────────┼─────────────┤
│           6 │ 6.38994e-06 │
├─────────────┼─────────────┤
│           7 │ 9.87017e-11 │
├─────────────┼─────────────┤
│           8 │ 0           │
╘═════════════╧═════════════╛

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
╒═════════════╤══════════╕
│   Iteration │    Error │
╞═════════════╪══════════╡
│           0 │ 0.983871 │
├─────────────┼──────────┤
│           1 │ 0        │
╘═════════════╧══════════╛
[0.9838709677419355, 0.0]
[0.0]

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
╒═════════════╤══════════╕
│   Iteration │    Error │
╞═════════════╪══════════╡
│           0 │ 0.983871 │
├─────────────┼──────────┤
│           1 │ 0        │
╘═════════════╧══════════╛
Traceback (most recent call last):
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 94, in <module>
    driver()
  File "C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py", line 41, in driver
    plt.loglog(y1, yn)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\pyplot.py", line 2722, in loglog
    return gca().loglog(*args, **kwargs)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_axes.py", line 1829, in loglog
    return self.plot(
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_axes.py", line 1688, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_base.py", line 311, in __call__
    yield from self._plot_args(
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_base.py", line 504, in _plot_args
    raise ValueError(f"x and y must have same first dimension, but "
ValueError: x and y must have same first dimension, but have shapes (1,) and (2,)

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Homeworks/Homework 4/secant method.py
the approximate root is 1.0161290322580645e+00
the error message reads: 1
Number of iterations: 2
╒═════════════╤══════════╕
│   Iteration │    Error │
╞═════════════╪══════════╡
│           0 │ 0.983871 │
├─────────────┼──────────┤
│           1 │ 0        │
╘═════════════╧══════════╛

Warning (from warnings module):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1520.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 861
    func(*args)
UserWarning: Data has no positive values, and therefore cannot be log-scaled.

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example.py
the approximate root is 1.1347241384015194e+00
the error message reads: 0
Number of iterations: 8
╒═════════════╤═════════════╕
│   Iteration │       Error │
╞═════════════╪═════════════╡
│           0 │ 0.865276    │
├─────────────┼─────────────┤
│           1 │ 0.545904    │
├─────────────┼─────────────┤
│           2 │ 0.296015    │
├─────────────┼─────────────┤
│           3 │ 0.120247    │
├─────────────┼─────────────┤
│           4 │ 0.0268143   │
├─────────────┼─────────────┤
│           5 │ 0.00162914  │
├─────────────┼─────────────┤
│           6 │ 6.38994e-06 │
├─────────────┼─────────────┤
│           7 │ 9.87017e-11 │
├─────────────┼─────────────┤
│           8 │ 0           │
╘═════════════╧═════════════╛
# Problem 4 - Newton
                     

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py
the approximate root is 3.7330877924904859e+00
the error message reads: 0
Number of iterations: 50
The order of convergence is:  2
# Newton Modified
                     

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py
the approximate root is -9.4688155953709674e-01
the error message reads: 1
Number of iterations: 99
The order of convergence is:  1

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py
the approximate root is 1.4109571153068636e+00
the error message reads: 1
Number of iterations: 99
The order of convergence is:  1

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py
the approximate root is 2.1838109873710398e-01
the error message reads: 1
Number of iterations: 999
The order of convergence is:  1

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py
the approximate root is 1.2117647738663757e+00
the error message reads: 1
Number of iterations: 999
The order of convergence is:  1
#Newton Modified with Multiplicity known
                     

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py", line 71, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py", line 18, in driver
    (p,pstar,info,it, count) = newton(f,fp,p0,tol, Nmax)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py", line 46, in newton
    p1 = x - 3* f(p0)/fp(p0)
NameError: name 'x' is not defined
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py
the approximate root is 3.7330838973302596e+00
the error message reads: 0
Number of iterations: 3
The order of convergence is:  2
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 4\newton_example - Copy.py
the approximate root is 1.2599616462966279e-01
the error message reads: 1
Number of iterations: 99
The order of convergence is:  1
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_example.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_example.py", line 127, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_example.py", line 19, in driver
    [points, pstar, ier, count] = bisection_newton(f,fp,a,b,tol,Nmax)
ValueError: not enough values to unpack (expected 4, got 2)
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_example.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_example.py", line 127, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_example.py", line 19, in driver
    [points, pstar, ier, count] = bisection_newton(f,fp,a,b,tol,Nmax)
ValueError: not enough values to unpack (expected 4, got 2)
