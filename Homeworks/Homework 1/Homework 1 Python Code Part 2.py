Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as no
(13/8)*no.cos(0.5) - (11/8)
0.05107166307185573
1/16
0.0625
def p2(x):
    return 1+x-0.5*x**2

pr(0.5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    pr(0.5)
NameError: name 'pr' is not defined. Did you mean: 'p2'?
p2(0.5)
1.375
11/8
1.375
import scipy
import scipy.integrate
scipy.integrate.quad((1+x+x**3)*no.cos(x), 0,1)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    scipy.integrate.quad((1+x+x**3)*no.cos(x), 0,1)
NameError: name 'x' is not defined
scipy.integrate.quad(lambda x: (1+x+x**3)*no.cos(x), 0,1)
(1.394982433840031, 1.5487416169968416e-14)
56**2 -4
3132
no.sqrt(3132)
55.96427431853289
56+55.964
111.964
(56 - 55.964)/2
0.018000000000000682
56-55.964
0.036000000000001364
no.sqrt(3132)
55.96427431853289
sq = no.sqrt(3132)
(56-sq)/2
0.017862840733556595
((56-sq)/2) - 0.018
-0.00013715926644340334
no.abs(((56-sq)/2) - 0.018)/((56-sq)/2)
0.007678468866698233
(56+sq)/2
55.98213715926644
0.017-0.018
-0.0009999999999999974
0.001/0.017
0.058823529411764705
x1 = 0.05
x2 = 9*10**5
x2-x1
899999.95
def difference(delta,x):
    denom = no.cos(x+delta) +no.cos(x)
    num = cos(x+delta)**2 + sin(x)**2 -1
    return no.cos(x+delta) - no.cos(x) - (num/denom)

x1 = no.pi
x2 = 10**6
delta = no.arange(10**(-16), 1, 10)
delta
array([1.e-16])
d = no.arange(-16, 0, 1)
d
array([-16, -15, -14, -13, -12, -11, -10,  -9,  -8,  -7,  -6,  -5,  -4,
        -3,  -2,  -1])
delta = 10**d
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    delta = 10**d
ValueError: Integers to negative integer powers are not allowed.
delta = []
for i in d:
    delta.append(10**(d))

    
Traceback (most recent call last):
  File "<pyshell#42>", line 2, in <module>
    delta.append(10**(d))
ValueError: Integers to negative integer powers are not allowed.
10**(-6)
1e-06
delta = [10**(-16), 10**(-15), 10**(-14), 10**(-13), 10**(-12), 10**(-11), 10**(-10), 10**(-9), 10**(-8), 10**(-7), 10**(-6), 10**(-5), 10**(-4), 10**(-3), 10**(-2), 10**(-1), 10**0)]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
delta = [10**(-16), 10**(-15), 10**(-14), 10**(-13), 10**(-12), 10**(-11), 10**(-10), 10**(-9), 10**(-8), 10**(-7), 10**(-6), 10**(-5), 10**(-4), 10**(-3), 10**(-2), 10**(-1), 10**0]
import matplotlib.pyplot as plt
plt.plot(delta, difference(delta, x1))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    plt.plot(delta, difference(delta, x1))
  File "<pyshell#31>", line 2, in difference
    denom = no.cos(x+delta) +no.cos(x)
TypeError: unsupported operand type(s) for +: 'float' and 'list'
delta = no.array(delta)
delta
array([1.e-16, 1.e-15, 1.e-14, 1.e-13, 1.e-12, 1.e-11, 1.e-10, 1.e-09,
       1.e-08, 1.e-07, 1.e-06, 1.e-05, 1.e-04, 1.e-03, 1.e-02, 1.e-01,
       1.e+00])
plt.plot(delta, difference(delta, x1))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    plt.plot(delta, difference(delta, x1))
  File "<pyshell#31>", line 3, in difference
    num = cos(x+delta)**2 + sin(x)**2 -1
NameError: name 'cos' is not defined
>>> def difference(delta,x):
...     denom = no.cos(x+delta) +no.cos(x)
...     num = no.cos(x+delta)**2 + no.sin(x)**2 -1
...     return no.cos(x+delta) - no.cos(x) - (num/denom)
... 
>>> plt.plot(delta, difference(delta, x1))
[<matplotlib.lines.Line2D object at 0x000001E8A5B57410>]
>>> plt.plot(delta, difference(delta, x2))
[<matplotlib.lines.Line2D object at 0x000001E8A5B1C4D0>]
>>> plt.show()
>>> plt.log(delta, difference(delta, x1))
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    plt.log(delta, difference(delta, x1))
AttributeError: module 'matplotlib.pyplot' has no attribute 'log'. Did you mean: '_log'?
>>> plt.logx(delta, difference(delta, x1))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    plt.logx(delta, difference(delta, x1))
AttributeError: module 'matplotlib.pyplot' has no attribute 'logx'
>>> plt.plot(delta, difference(delta, x1))
[<matplotlib.lines.Line2D object at 0x000001E8A75C61D0>]
>>> plt.xscale('log')
>>> plt.plot(delta, difference(delta, x2))
[<matplotlib.lines.Line2D object at 0x000001E8A7518DD0>]
>>> plt.xcale('log')
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    plt.xcale('log')
AttributeError: module 'matplotlib.pyplot' has no attribute 'xcale'. Did you mean: 'xscale'?
>>> plt.show()
>>> plt.plot(delta, difference(delta, x1))
[<matplotlib.lines.Line2D object at 0x000001E8AE8AE9D0>]
>>> plt.xscale('log')
>>> plt.plot(delta, difference(delta, x2))
[<matplotlib.lines.Line2D object at 0x000001E8AE8AD850>]
>>> plt.xscale('log')
>>> plt.show()
