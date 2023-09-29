Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py", line 129, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py", line 19, in driver
    [points, pstar, ier, count] = bisection_newton(f,fp,a,b,tol,Nmax)
ValueError: not enough values to unpack (expected 4, got 2)

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py", line 129, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py", line 19, in driver
    [points, pstar, ier, count] = bisection_newton(f,fp,a,b,tol,Nmax)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py", line 68, in bisection_newton
    [points,pstar,info, count] = newton(f, fp, d, tol, Nmax)
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py", line 118, in newton
    p[it+1] = p1
NameError: name 'p' is not defined. Did you mean: 'fp'?

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py
the approximate root is -1.2246467991473532e-16
the error message reads: 0
f(astar) = -1.2246467991473532e-16
The number of iterations is:  2

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py
the approximate root is -2.8225146347383807e-06
the error message reads: 0
f(astar) = -2.2485813655642863e-17
The number of iterations is:  11

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py
the approximate root is -2.8225146347383807e-06
the error message reads: 0
f(astar) = -2.2485813655642863e-17
The number of iterations is:  11
Iterations:  [array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), array([-5.00000000e-01, -1.66666667e-01, -5.55555556e-02, -1.85185185e-02,
       -6.17283951e-03, -2.05761317e-03, -6.85871056e-04, -2.28623685e-04,
       -7.62078951e-05, -2.54026317e-05, -8.46754390e-06, -2.82251463e-06,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,
        0.00000000e+00])]

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py", line 129, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py", line 19, in driver
    [points, pstar, ier, count] = bisection_newton(f,fp,a,b,tol,Nmax)
ValueError: not enough values to unpack (expected 4, got 2)

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py", line 129, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py", line 19, in driver
    [points, pstar, ier, count] = bisection_newton(f,fp,a,b,tol,Nmax)
ValueError: not enough values to unpack (expected 4, got 2)
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py
the approximate root is 0.5
the error message reads: 1
f(astar) = 39.0625
The number of iterations is:  0
Iterations:  [0.]
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Labs\Lab 5\bisection_newton example.py
the approximate root is 1.25
the error message reads: 0
f(astar) = 1.25
The number of iterations is:  1
Iterations:  [array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), array([1.25, 1.25, 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  ])]
