Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Problem 1
# Initial guess x=1, y = 1

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py
[-1.81626407  0.8373678 ]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0006099462509155274
Netwon: number of iterations is: 7

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 46
    F[1] = np.e**(x[0]) + x[1] - 1
RuntimeWarning: overflow encountered in scalar power
[nan nan]
Lazy Newton: the error message reads: 1
Lazy Newton: took this many seconds: 0.0008180141448974609
Lazy Newton: number of iterations is: 99
[-1.81626407  0.8373678 ]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0007757425308227539
Broyden: number of iterations is: 12
# Initial Guess x = 1,  y = -1

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py
[ 1.00416874 -1.72963729]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0006673383712768555
Netwon: number of iterations is: 5
[ 1.00416874 -1.72963729]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0008430838584899903
Lazy Newton: number of iterations is: 36
[ 1.00416874 -1.72963729]
Broyden: the error message reads: 0
Broyden: took this many seconds: 2.5725364685058595e-05
Broyden: number of iterations is: 6
# Initial Guess x = 0, y = 0

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 162, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 16, in driver
    [xstar,ier,its] =  Newton(x0,tol,Nmax)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 65, in Newton
    Jinv = inv(J)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix
# Running the same things as above just with the order of convergence

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py
[-1.81626407  0.8373678 ]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0009642982482910156
Netwon: number of iterations is: 7
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 202, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 23, in driver
    [alpha, rate] = orderconvergence(xstar, iterations)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 79, in orderconvergence
    while num/(denom**alpha) == float("INF"):
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
# x= 1,y = -1

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py
[ 1.00416874 -1.72963729]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0011698675155639648
Netwon: number of iterations is: 5

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 74
    if (isinstance(num/denom, float)) and (num/denom < 1):
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 79
    while num/(denom**alpha) == float("INF"):
RuntimeWarning: invalid value encountered in divide
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 202, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 23, in driver
    [alpha, rate] = orderconvergence(xstar, iterations)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py", line 79, in orderconvergence
    while num/(denom**alpha) == float("INF"):
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2.py
[ 1.00416874 -1.72963729]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0017087078094482422
Netwon: number of iterations is: 5
[array([ 1.07576569, -1.92423431]), array([ 1.00947079, -1.73784486]), array([ 1.00418858, -1.72965323]), array([ 1.00416874, -1.72963729]), array([ 1.00416874, -1.72963729]), array([ 1.00416874, -1.72963729])]
[ 1.00416874 -1.72963729]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0010607361793518067
Lazy Newton: number of iterations is: 36
[array([ 1.07576569, -1.92423431]), array([ 0.95797535, -1.61204989]), array([ 1.02451819, -1.78729624]), array([ 0.99211361, -1.69766814]), array([ 1.01028226, -1.74631622]), array([ 1.00081413, -1.72063905]), array([ 1.00593194, -1.73440741]), array([ 1.00322072, -1.72708457]), array([ 1.00467229, -1.73099654]), array([ 1.00389953, -1.72891158]), array([ 1.00431216, -1.73002419]), array([ 1.00409219, -1.72943086]), array([ 1.00420956, -1.72974738]), array([ 1.00414696, -1.72957856]), array([ 1.00418035, -1.72966861]), array([ 1.00416254, -1.72962058]), array([ 1.00417204, -1.7296462 ]), array([ 1.00416698, -1.72963253]), array([ 1.00416968, -1.72963982]), array([ 1.00416824, -1.72963593]), array([ 1.00416901, -1.72963801]), array([ 1.0041686, -1.7296369]), array([ 1.00416881, -1.72963749]), array([ 1.0041687 , -1.72963718]), array([ 1.00416876, -1.72963735]), array([ 1.00416873, -1.72963726]), array([ 1.00416874, -1.7296373 ]), array([ 1.00416874, -1.72963728]), array([ 1.00416874, -1.72963729]), array([ 1.00416874, -1.72963728]), array([ 1.00416874, -1.72963729]), array([ 1.00416874, -1.72963729]), array([ 1.00416874, -1.72963729]), array([ 1.00416874, -1.72963729]), array([ 1.00416874, -1.72963729]), array([ 1.00416874, -1.72963729]), array([ 1.00416874, -1.72963729])]
[ 1.00416874 -1.72963729]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0005454301834106445
Broyden: number of iterations is: 6
[array([ 0.98824775, -1.69228204]), array([ 1.00301692, -1.7278811 ]), array([ 1.00417409, -1.72962989]), array([ 1.0041689 , -1.72963783]), array([ 1.00416874, -1.7296373 ]), array([ 1.00416874, -1.72963729]), array([ 1.00416874, -1.72963729])]
# realized I didn't need order of convergence
# Problem 2
# Steepest Descent - tolerance is 10^(-6)

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\steep_example.py
the steepest descent code found the solution  [-6.64330273e-05  9.99659465e-02  9.99983513e-01]
g evaluated at this point is  4.950473926375841e-09
ier is  0
>>> # Steepest Descent - tolerance 5 * 10^-2
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\steep_example.py
the steepest descent code found the solution  [-0.02218553  0.08874213  0.99556289]
g evaluated at this point is  0.0005462335865889256
ier is  0
>>> # Newton's Method - tolderance is 10^(-6)
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2 - problem 2.py
[0.  0.1 1. ]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0012643814086914062
Netwon: number of iterations is: 2
[0.  0.1 1. ]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0009544968605041503
Lazy Newton: number of iterations is: 3
[0.  0.1 1. ]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0008695483207702637
Broyden: number of iterations is: 1
>>> # Newton's method with x0 of Steepest Descent output with 5x10^-2 tolerance
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\newtonNONLinear2 - problem 2.py
[5.81496589e-17 1.00000000e-01 1.00000000e+00]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00037308692932128904
Netwon: number of iterations is: 2
[1.15383007e-11 1.00000000e-01 1.00000000e+00]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.00081787109375
Lazy Newton: number of iterations is: 2
[8.92021134e-15 1.00000000e-01 1.00000000e+00]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0009168267250061035
Broyden: number of iterations is: 2
# Steepest tol = 5*  10^-2

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\steep_example.py
the steepest descent code found the solution  [-0.02218553  0.08874213  0.99556289]
g evaluated at this point is  0.0005462335865889256
ier is  0
The number of iterations is: 0
# steepest tol = 10*(-6)

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 6\steep_example.py
the steepest descent code found the solution  [-6.64330273e-05  9.99659465e-02  9.99983513e-01]
g evaluated at this point is  4.950473926375841e-09
ier is  0
The number of iterations is: 4
