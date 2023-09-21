Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py", line 57, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py", line 18, in driver
    [xstar,ier] = fixedpt(f1,x0,tol,Nmax)
ValueError: too many values to unpack (expected 2)

====== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py =====
the approximate fixed point is: 1.3652300134164816
f1(xstar): 1.3652300134137934
Error message reads: 0
points
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    points
NameError: name 'points' is not defined. Did you mean: 'print'?

====== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py =====

points = [[1.34839972],
 [1.36737637],
 [1.36495702],
 [1.36526475],
 [1.36522559],
 [1.36523058],
 [1.36522994],
 [1.36523002],
 [1.36523001],
 [1.36523001],
 [1.36523001],
 [1.36523001]]
len(points)
12
# it took 12 iterations for this function

====== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py =====
the approximate fixed point is: 1.3652300134164816
f1(xstar): 1.3652300134137934
Error message reads: 0
Vector of Iterations 
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py", line 75, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py", line 25, in driver
    [alpha, constant] = orderconvergence(p, points)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py", line 64, in orderconvergence
    num = abs(vector[N] - point)
IndexError: index 100 is out of bounds for axis 0 with size 100
>>> 
====== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py =====
the approximate fixed point is: 1.3652300134164816
f1(xstar): 1.3652300134137934
Error message reads: 0
Vector of Iterations 
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py", line 76, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py", line 25, in driver
    [alpha, constant] = orderconvergence(p, points)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py", line 67, in orderconvergence
    if isinstance(num/denom, float) & num/denom < 1:
TypeError: ufunc 'bitwise_and' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
>>> 
====== RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 4\fixedpt_example.py =====
the approximate fixed point is: 1.3652300134164816
f1(xstar): 1.3652300134137934
Error message reads: 0
Vector of Iterations 
The order of convergence is:  1
The error constant is:  0.1271839945037372
