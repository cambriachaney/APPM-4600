Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#N = 2

========== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py =========
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py", line 139, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py", line 30, in driver
    plt.plot(xint, polynomial_eval, legend = "Approximation of Monomial")
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\pyplot.py", line 2812, in plot
    return gca().plot(
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_axes.py", line 1688, in plot
    lines = [*self._get_lines(*args, data=data, **kwargs)]
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_base.py", line 311, in __call__
    yield from self._plot_args(
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_base.py", line 544, in _plot_args
    return [l[0] for l in result]
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_base.py", line 544, in <listcomp>
    return [l[0] for l in result]
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_base.py", line 537, in <genexpr>
    result = (make_artist(x[:, j % ncx], y[:, j % ncy], kw,
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\axes\_base.py", line 351, in _makeline
    seg = mlines.Line2D(x, y, **kw)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\_api\deprecation.py", line 454, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\lines.py", line 395, in __init__
    self._internal_update(kwargs)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\artist.py", line 1223, in _internal_update
    return self._update_props(
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\matplotlib\artist.py", line 1197, in _update_props
    raise AttributeError(
AttributeError: Line2D.set() got an unexpected keyword argument 'legend'

========== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py =========
No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.

========== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py =========
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py", line 142, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py", line 31, in driver
    [a_vec,polynomial_eval] = monomials(f, xeval, N)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py", line 128, in monomials
    a = vander_inv * y
ValueError: operands could not be broadcast together with shapes (3,3) (1001,) 
>>> 
========== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py =========
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py", line 142, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py", line 33, in driver
    plt.plot(xeval, yeval_mono - polynomial_eval, label = "Error of Monomial")
ValueError: operands could not be broadcast together with shapes (1001,) (1001,3) 
>>> 
========== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py =========
[[ 0.         1.         0.       ]
 [-0.0049505  0.         0.0049505]
 [ 0.0049505 -1.         0.0049505]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py", line 144, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py", line 33, in driver
    plt.plot(xeval, yeval_mono - polynomial_eval, label = "Error of Monomial")
ValueError: operands could not be broadcast together with shapes (1001,) (1001,3) 
>>> 
========== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py =========
[ 1.          0.         -0.99009901]
No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
>>> 
========== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py =========
[ 1.          0.         -0.99009901]
>>> [ 1.          0.         -0.99009901]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> #N = 10
>>> 
========== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py =========
>>> 
========== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 7\interp.py =========
