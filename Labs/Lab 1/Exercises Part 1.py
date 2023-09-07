Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as  np
>>> import math
>>> x = [1,2,3]
>>> x*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> #it triples the vector
>>> y = np.array([1,2,3])
>>> y*3
array([3, 6, 9])
>>> #it multiplies each vector by 3
>>> 3*y
array([3, 6, 9])
>>> print('this is 3y', 3*y)
this is 3y [3 6 9]
>>> import matplotlib.pyplot as plt
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
>>> import matplotlib.pyplot as plt
Matplotlib is building the font cache; this may take a moment.
>>> x = np.linspace(0,2*np.pi, 100)
>>> Ya = np.sin(X)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    Ya = np.sin(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
>>> Ya = np.sin(x)
>>> Yb = np.cos(x)
>>> plt.plot(x, Ya)
[<matplotlib.lines.Line2D object at 0x0000013DDC963390>]
>>> plt.show()
>>> plt.plot(x, Ya)
[<matplotlib.lines.Line2D object at 0x0000013DDC9D6BD0>]
p
>>> plt.plot(X, Yb)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    plt.plot(X, Yb)
NameError: name 'X' is not defined. Did you mean: 'x'?
plt.plot(x, Yb)
[<matplotlib.lines.Line2D object at 0x0000013DDC9EC990>]
plt.show()
#x has 100 values between 0 and 2pi
plt.plot(X, Ya)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    plt.plot(X, Ya)
NameError: name 'X' is not defined. Did you mean: 'x'?
plt.plot(x, Ya)
[<matplotlib.lines.Line2D object at 0x0000013DE01830D0>]
plt.plot(x, Yb)
[<matplotlib.lines.Line2D object at 0x0000013DDC9F2C10>]
plt.xlabel('x')
Text(0.5, 0, 'x')
plt.ylabel('y')
Text(0, 0.5, 'y')
plt.show()
x = np.linspace(0,1,100)
x
array([0.        , 0.01010101, 0.02020202, 0.03030303, 0.04040404,
       0.05050505, 0.06060606, 0.07070707, 0.08080808, 0.09090909,
       0.1010101 , 0.11111111, 0.12121212, 0.13131313, 0.14141414,
       0.15151515, 0.16161616, 0.17171717, 0.18181818, 0.19191919,
       0.2020202 , 0.21212121, 0.22222222, 0.23232323, 0.24242424,
       0.25252525, 0.26262626, 0.27272727, 0.28282828, 0.29292929,
       0.3030303 , 0.31313131, 0.32323232, 0.33333333, 0.34343434,
       0.35353535, 0.36363636, 0.37373737, 0.38383838, 0.39393939,
       0.4040404 , 0.41414141, 0.42424242, 0.43434343, 0.44444444,
       0.45454545, 0.46464646, 0.47474747, 0.48484848, 0.49494949,
       0.50505051, 0.51515152, 0.52525253, 0.53535354, 0.54545455,
       0.55555556, 0.56565657, 0.57575758, 0.58585859, 0.5959596 ,
       0.60606061, 0.61616162, 0.62626263, 0.63636364, 0.64646465,
       0.65656566, 0.66666667, 0.67676768, 0.68686869, 0.6969697 ,
       0.70707071, 0.71717172, 0.72727273, 0.73737374, 0.74747475,
       0.75757576, 0.76767677, 0.77777778, 0.78787879, 0.7979798 ,
       0.80808081, 0.81818182, 0.82828283, 0.83838384, 0.84848485,
       0.85858586, 0.86868687, 0.87878788, 0.88888889, 0.8989899 ,
       0.90909091, 0.91919192, 0.92929293, 0.93939394, 0.94949495,
       0.95959596, 0.96969697, 0.97979798, 0.98989899, 1.        ])
y = np.arange(0, 1.00001, step = 1/100)
y
array([0.  , 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1 ,
       0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2 , 0.21,
       0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3 , 0.31, 0.32,
       0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4 , 0.41, 0.42, 0.43,
       0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5 , 0.51, 0.52, 0.53, 0.54,
       0.55, 0.56, 0.57, 0.58, 0.59, 0.6 , 0.61, 0.62, 0.63, 0.64, 0.65,
       0.66, 0.67, 0.68, 0.69, 0.7 , 0.71, 0.72, 0.73, 0.74, 0.75, 0.76,
       0.77, 0.78, 0.79, 0.8 , 0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87,
       0.88, 0.89, 0.9 , 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98,
       0.99, 1.  ])
x = np.linspace(0,1,4)
x
array([0.        , 0.33333333, 0.66666667, 1.        ])
y = np.arange(0,1.2, step = 1/3)
y
array([0.        , 0.33333333, 0.66666667, 1.        ])
x[0:2]
array([0.        , 0.33333333])
x[0:3]
array([0.        , 0.33333333, 0.66666667])
print('the first three entries of x are', x[0:3])
the first three entries of x are [0.         0.33333333 0.66666667]
w = 10**(-np.linspace(1,10,10))
w
array([1.e-01, 1.e-02, 1.e-03, 1.e-04, 1.e-05, 1.e-06, 1.e-07, 1.e-08,
       1.e-09, 1.e-10])
x = np.arange(1, length(w),1)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    x = np.arange(1, length(w),1)
NameError: name 'length' is not defined
x = np.arange(1, len(w), 1)
x
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.arange(1, len(w) +1, 1)
x
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
plt.smilogy(x, w)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    plt.smilogy(x, w)
AttributeError: module 'matplotlib.pyplot' has no attribute 'smilogy'. Did you mean: 'semilogy'?
plt.semilogy(x,w)
[<matplotlib.lines.Line2D object at 0x0000013DE01D56D0>]
plt.xlabel('x')
Text(0.5, 0, 'x')
plt.ylabel('w')
Text(0, 0.5, 'w')
plt.show()
s = 3*w
plt.plot(x, s)
[<matplotlib.lines.Line2D object at 0x0000013DE36DC390>]
plt.show()
plt.semilogy(x, w)
[<matplotlib.lines.Line2D object at 0x0000013DE37A6BD0>]
plt.xlabel('x')
Text(0.5, 0, 'x')
plt.ylabel('w')
Text(0, 0.5, 'w')
plt.plot(x, s)
[<matplotlib.lines.Line2D object at 0x0000013DE37ACB50>]
plt.show()
