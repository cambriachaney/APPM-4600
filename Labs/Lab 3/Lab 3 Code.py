Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3
SyntaxError: unexpected character after line continuation character
python3 bisection_example.py
SyntaxError: invalid syntax
cd C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3
SyntaxError: invalid syntax
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\bisection_example.py
SyntaxError: invalid syntax


==== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\bisection_example.py ====
the approximate root is 0.9999999701976776
the error message reads: 0
f(astar) = -2.98023206113385e-08

==== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\bisection_example.py ====
the approximate root is -1
the error message reads: 1
f(astar) = -2

==== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\bisection_example.py ====
the approximate root is 0.9999999701976776
the error message reads: 0
f(astar) = -2.98023206113385e-08

==== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\bisection_example.py ====
the approximate root is 0.9999999701976776
the error message reads: 0
f(astar) = -2.98023206113385e-08
# The intervals of a and c were successful because f(astar) is approximately equal to 0, meaning the code found a zero. However, for b, it was unable to find the root x =0, and instead things the approximate root is -1, when that isn't true.
# Lab 3 Problem 2(a)

==== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\bisection_example.py ====
the approximate root is 1.0000030517578122
the error message reads: 0
f(astar) = 2.4414006618542327e-05
# Problem 2(b)

==== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\bisection_example.py ====
the approximate root is 0
the error message reads: 1
f(astar) = -3
# Problem 2(c)

==== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\bisection_example.py ====
the approximate root is 0
the error message reads: 0
f(astar) = 0.0

==== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\bisection_example.py ====
the approximate root is 0.5
the error message reads: 1
f(astar) = 0.479425538604203
# This behavior is not what I expected because for 2b and the second part of 2c, you didn't get a true root. However, it does behave to the 10^-5 tolerance level for part a and the first part of c.

===== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py =====
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 54, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 18, in driver
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 42, in fixedpt
    x1 = f(x0)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 7, in <lambda>
    f1 = lambda x: x*(1+ (7-x**5)/(x**2))**3
ZeroDivisionError: float division by zero

===== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py =====
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 54, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 18, in driver
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 42, in fixedpt
    x1 = f(x0)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 7, in <lambda>
    f1 = lambda x: x*(1+ (7-x**5)/(x**2))**3
ZeroDivisionError: float division by zero
>>> 
===== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py =====
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 54, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 18, in driver
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 42, in fixedpt
    x1 = f(x0)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py", line 7, in <lambda>
    f1 = lambda x: x*(1+ (7-x**5)/(x**2))**3
OverflowError: (34, 'Result too large')
>>> # the result for (a) and (b) is too large, meaning the fixed point code does not converge, meaning the functions go to infinity after x = 1.
>>> 
===== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 3\fixedpt_example.py =====
the approximate fixed point is: 1.475773161594552
f1(xstar): 1.4757731615945522
Error message reads: 0
the approximate fixed point is: 1.4735780454667078
f2(xstar): 1.4779035096682076
Error message reads: 1
>>> 7**(1/5)
1.4757731615945522
>>> # It is thus verified that 7**(1/5) is a fixed point for (c) and (d) but it could not be verified for (a) and (b) because the fixed point method doesn't converge for them.
