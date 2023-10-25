Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 84
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 121, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 25, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 85, in create_natural_spline
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
IndexError: index 1 is out of bounds for axis 0 with size 1

============ RESTART: C:\Users\cambr\Downloads\cubic_spline_demo.py ============
4
M = [0.         1.46739813 2.58190378 0.        ]
nerr =  0.06988468205767485

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
4
M = [ 0.         -1.45923627 -1.02019776  0.        ]
nerr =  3.957087934407497

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
4
M = [ 0.         -1.45923627 -1.02019776  0.        ]
yeval =  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0.]
nerr =  3.957087934407497

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
4
M = [ 0.         -1.45923627 -1.02019776  0.        ]
yloc =  []
yloc =  []
yloc =  []
yeval =  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0.]
nerr =  3.957087934407497

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
4
M = [ 0.         -1.45923627 -1.02019776  0.        ]
xip 6.123233995736766e-17
xeval []
xi 0.8660254037844387
Mip -1.4592362732259472
yloc =  []
xip -0.8660254037844387
xeval []
xi 6.123233995736766e-17
Mip -1.0201977642390665
yloc =  []
xip -0.8660254037844388
xeval []
xi -0.8660254037844387
Mip 0.0
yloc =  []
yeval =  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0.]
nerr =  3.957087934407497

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
4
M = [ 0.         -1.45923627 -1.02019776  0.        ]
ind (array([], dtype=int64),)
ind (array([], dtype=int64),)
ind (array([], dtype=int64),)
yeval =  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0.]
nerr =  3.957087934407497

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
4
M = [ 0.         -1.45923627 -1.02019776  0.        ]
atmp 0.8660254037844387
btmp 6.123233995736766e-17
ind (array([], dtype=int64),)
atmp 6.123233995736766e-17
btmp -0.8660254037844387
ind (array([], dtype=int64),)
atmp -0.8660254037844387
btmp -0.8660254037844388
ind (array([], dtype=int64),)
yeval =  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0.]
nerr =  3.957087934407497

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
xeval [-5.  -4.9 -4.8 -4.7 -4.6 -4.5 -4.4 -4.3 -4.2 -4.1 -4.  -3.9 -3.8 -3.7
 -3.6 -3.5 -3.4 -3.3 -3.2 -3.1 -3.  -2.9 -2.8 -2.7 -2.6 -2.5 -2.4 -2.3
 -2.2 -2.1 -2.  -1.9 -1.8 -1.7 -1.6 -1.5 -1.4 -1.3 -1.2 -1.1 -1.  -0.9
 -0.8 -0.7 -0.6 -0.5 -0.4 -0.3 -0.2 -0.1  0.   0.1  0.2  0.3  0.4  0.5
  0.6  0.7  0.8  0.9  1.   1.1  1.2  1.3  1.4  1.5  1.6  1.7  1.8  1.9
  2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8  2.9  3.   3.1  3.2  3.3
  3.4  3.5  3.6  3.7  3.8  3.9  4.   4.1  4.2  4.3  4.4  4.5  4.6  4.7
  4.8  4.9  5. ]
4
M = [ 0.         -1.45923627 -1.02019776  0.        ]
atmp 0.8660254037844387
btmp 6.123233995736766e-17
ind (array([], dtype=int64),)
atmp 6.123233995736766e-17
btmp -0.8660254037844387
ind (array([], dtype=int64),)
atmp -0.8660254037844387
btmp -0.8660254037844388
ind (array([], dtype=int64),)
yeval =  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0.]
nerr =  3.957087934407497

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
4
M = [ 0.         -1.45923627 -1.02019776  0.        ]
atmp 0.8660254037844387
btmp 6.123233995736766e-17
ind []
atmp 6.123233995736766e-17
btmp -0.8660254037844387
ind []
atmp -0.8660254037844387
btmp -0.8660254037844388
ind []
yeval =  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0. 0. 0. 0. 0.]
nerr =  3.957087934407497

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
4
M = [ 0.         -1.45923627 -1.02019776  0.        ]
atmp 0.8660254037844387
btmp 6.123233995736766e-17
ind []
atmp 6.123233995736766e-17
btmp -0.8660254037844387
ind []
atmp -0.8660254037844387
btmp -0.8660254037844388
ind []
yeval =  [0. 0. 0. ... 0. 0. 0.]
nerr =  12.51288629048828

================= RESTART: C:\Users\cambr\Downloads\lab8-3-3.py ================

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
[ 8.66025404e-01  6.12323400e-17 -8.66025404e-01 -8.66025404e-01]
4
M = [ 0.         -1.45923627 -1.02019776  0.        ]
atmp 0.8660254037844387
btmp 6.123233995736766e-17
ind []
atmp 6.123233995736766e-17
btmp -0.8660254037844387
ind []
atmp -0.8660254037844387
btmp -0.8660254037844388
ind []
yeval =  [0. 0. 0. ... 0. 0. 0.]
nerr =  12.51288629048828

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
[ 8.66025404e-01  6.12323400e-17 -8.66025404e-01]
3
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 129, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 27, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 76, in create_natural_spline
    A[N][N] = 1
IndexError: index 3 is out of bounds for axis 0 with size 3

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
[ 8.66025404e-01  6.12323400e-17 -8.66025404e-01]
3
M = [ 0.         -1.71428571  0.        ]
atmp 0.8660254037844387
btmp 6.123233995736766e-17
ind []
atmp 6.123233995736766e-17
btmp -0.8660254037844387
ind []
yeval =  
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 129, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 40, in driver
    nerr = norm(fex-yeval)
ValueError: operands could not be broadcast together with shapes (1001,) (1000,) 

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py
[ 8.66025404e-01  8.66025404e-01  6.12323400e-17 -8.66025404e-01
  8.66025404e-01  8.66025404e-01  6.12323400e-17 -8.66025404e-01
  8.66025404e-01  8.66025404e-01  6.12323400e-17 -8.66025404e-01
  8.66025404e-01  8.66025404e-01  6.12323400e-17 -8.66025404e-01
  8.66025404e-01  8.66025404e-01  6.12323400e-17 -8.66025404e-01]
20

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 64
    b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
RuntimeWarning: invalid value encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 86
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 87
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [nan nan nan]
atmp 0.8660254037844387
btmp 0.8660254037844387
ind []
atmp 0.8660254037844387
btmp 6.123233995736766e-17
ind []
yeval =  
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 129, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic_spline_demo.py", line 40, in driver
    nerr = norm(fex-yeval)
ValueError: operands could not be broadcast together with shapes (1001,) (1000,) 

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 65
    b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
RuntimeWarning: invalid value encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 87
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 88
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [nan nan nan nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 124, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 24, in driver
    xeval =  np.linspace(xint[0],xint[Nint],Neval+1)
IndexError: index 3 is out of bounds for axis 0 with size 3

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 124, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 24, in driver
    xeval =  np.linspace(xint[0],xint[Nint],Neval+1)
IndexError: index 3 is out of bounds for axis 0 with size 3

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 65
    b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
RuntimeWarning: invalid value encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 87
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 88
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 65
    b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
RuntimeWarning: invalid value encountered in scalar divide
[[1.         0.         0.         0.        ]
 [0.72168784 2.88675135 0.72168784 0.        ]
 [0.         0.72168784 1.44337567 0.        ]
 [0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 87
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 88
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 65
    b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
RuntimeWarning: invalid value encountered in scalar divide
A matrix:  [[1.         0.         0.         0.        ]
 [0.72168784 2.88675135 0.72168784 0.        ]
 [0.         0.72168784 1.44337567 0.        ]
 [0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 87
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 88
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 65
    b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.         -0.43849388         nan  0.        ]
A matrix:  [[1.         0.         0.         0.        ]
 [0.72168784 2.88675135 0.72168784 0.        ]
 [0.         0.72168784 1.44337567 0.        ]
 [0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 65
    b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.          0.27114227 -0.60990735  0.27114227         nan  0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [nan nan nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan]
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 65
    b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.          0.27114227 -0.60990735  0.27114227         nan  0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [nan nan nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan nan nan nan nan nan nan nan nan nan nan]
yloc =  [nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan nan
 nan nan]
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.27114227 -0.60990735  0.27114227  0.          0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.31916917 -0.47929939  0.35286475 -0.17643238  0.        ]
yloc =  [0.04235007 0.03640173 0.03060456 0.0251097  0.02006833 0.0156316
 0.01195067 0.00917671 0.00746087 0.00695432 0.00780822 0.01017372
 0.01420199 0.02004418 0.02785147 0.037775   0.04996595 0.06457547
 0.08175471 0.10165486]
yloc =  [0.12438002 0.1497813  0.17762503 0.2076775  0.23970499 0.27347379
 0.30875018 0.34530045 0.38289088 0.42128775 0.46025736 0.49956597
 0.53897988 0.57826537 0.61718873 0.65551624 0.69301417 0.72944883
 0.76458649 0.79819344 0.83003595 0.85988032 0.88749283 0.91263977
 0.9350874  0.95460203 0.97094994 0.98389741 0.99321071 0.99865615
 1.        ]
yloc =  [0.99708809 0.99008446 0.97923269 0.96477634 0.94695901 0.92602427
 0.90221569 0.87577686 0.84695136 0.81598276 0.78311465 0.74859059
 0.71265418 0.67554899 0.63751859 0.59880657 0.55965651 0.52031198
 0.48101657 0.44201384 0.40354738 0.36586078 0.3291976  0.29380143
 0.25991584 0.22778441 0.19765073 0.16975837 0.14435091 0.12167192]
yloc =  [0.10196492 0.08536457 0.07168059 0.06066231 0.05205903 0.0456201
 0.04109482 0.03823251 0.03678251 0.03649412 0.03711668 0.0383995
 0.04009191 0.04194321 0.04370275 0.04511983 0.04594379 0.04592393
 0.04480958 0.04235007]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 99
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.27114227 -0.60990735  0.27114227  0.          0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.31916917 -0.47929939  0.35286475 -0.17643238  0.        ]
yloc =  [0.04235007 0.03640173 0.03060456 0.0251097  0.02006833 0.0156316
 0.01195067 0.00917671 0.00746087 0.00695432 0.00780822 0.01017372
 0.01420199 0.02004418 0.02785147 0.037775   0.04996595 0.06457547
 0.08175471 0.10165486]
yloc =  [0.12438002 0.1497813  0.17762503 0.2076775  0.23970499 0.27347379
 0.30875018 0.34530045 0.38289088 0.42128775 0.46025736 0.49956597
 0.53897988 0.57826537 0.61718873 0.65551624 0.69301417 0.72944883
 0.76458649 0.79819344 0.83003595 0.85988032 0.88749283 0.91263977
 0.9350874  0.95460203 0.97094994 0.98389741 0.99321071 0.99865615
 1.        ]
yloc =  [0.99708809 0.99008446 0.97923269 0.96477634 0.94695901 0.92602427
 0.90221569 0.87577686 0.84695136 0.81598276 0.78311465 0.74859059
 0.71265418 0.67554899 0.63751859 0.59880657 0.55965651 0.52031198
 0.48101657 0.44201384 0.40354738 0.36586078 0.3291976  0.29380143
 0.25991584 0.22778441 0.19765073 0.16975837 0.14435091 0.12167192]
yloc =  [0.10196492 0.08536457 0.07168059 0.06066231 0.05205903 0.0456201
 0.04109482 0.03823251 0.03678251 0.03649412 0.03711668 0.0383995
 0.04009191 0.04194321 0.04370275 0.04511983 0.04594379 0.04592393
 0.04480958 0.04235007]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 99
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.01064407  0.0415022   0.23787734 -0.30777139 -0.30777139
  0.23787734  0.0415022   0.01064407  0.          0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.08056818 0.46763593 0.15324979 0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.15324979 0.72836004 0.21093023 0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.21093023 0.91778719 0.24796336 0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.24796336 1.01737494 0.26072411
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.26072411 1.01737494
  0.24796336 0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.24796336
  0.91778719 0.21093023 0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.21093023 0.72836004 0.15324979 0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.15324979 0.46763593 0.08056818 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.08056818 0.16113636 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.04061699 -0.05448554  0.35539121 -0.30973734 -0.30981552
  0.35562975 -0.05543159  0.04478498 -0.02239249  0.        ]
yloc =  [0.03938837 0.04083157 0.04235574 0.04404181 0.04597076]
yloc =  [0.04822349 0.0508404  0.05374335 0.05683269 0.06000877 0.06317193
 0.06622251 0.06906086 0.07158732 0.07370225]
yloc =  [0.07534059 0.07669639 0.07808113 0.07980685 0.08218561 0.08552944
 0.09015041 0.09636055 0.10447192 0.11479657 0.12764654 0.14333389
 0.16217067]
yloc =  [0.18435151 0.20957609 0.23741366 0.26743346 0.29920475 0.33229677
 0.36627877 0.40072001 0.43518972 0.46925716 0.50249157 0.53446221
 0.56473833 0.59288917 0.61848397]
yloc =  [0.64114776 0.66078996 0.67741049 0.69100931 0.70158637 0.70914161
 0.71367499 0.71518647 0.71367598 0.70914349 0.70158895 0.69101231
 0.67741352 0.66079253 0.6411493 ]
yloc =  [0.61848381 0.59288659 0.5647328  0.53445339 0.50247933 0.46924157
 0.43517106 0.40069877 0.36625565 0.33227265 0.29918073 0.26741085
 0.23739396 0.20956103 0.184343  ]
yloc =  [0.16217084 0.14334488 0.12766976 0.11483251 0.1045202  0.09641988
 0.09021858 0.08560336 0.08226127 0.07987935 0.07814466 0.07674425
 0.07536516]
yloc =  [0.07369504 0.07154072 0.06897208 0.06609414 0.06301191 0.0598304
 0.05665464 0.05358962 0.05074037 0.0482119 ]
yloc =  [0.04608075 0.04426668 0.04263586 0.04105439 0.03938837]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 99
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.01064407  0.0415022   0.23787734 -0.30777139 -0.30777139
  0.23787734  0.0415022   0.01064407  0.          0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.08056818 0.46763593 0.15324979 0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.15324979 0.72836004 0.21093023 0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.21093023 0.91778719 0.24796336 0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.24796336 1.01737494 0.26072411
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.26072411 1.01737494
  0.24796336 0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.24796336
  0.91778719 0.21093023 0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.21093023 0.72836004 0.15324979 0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.15324979 0.46763593 0.08056818 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.08056818 0.16113636 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.04061699 -0.05448554  0.35539121 -0.30973734 -0.30981552
  0.35562975 -0.05543159  0.04478498 -0.02239249  0.        ]
yloc =  [0.03938837 0.04083157 0.04235574 0.04404181 0.04597076]
yloc =  [0.04822349 0.0508404  0.05374335 0.05683269 0.06000877 0.06317193
 0.06622251 0.06906086 0.07158732 0.07370225]
yloc =  [0.07534059 0.07669639 0.07808113 0.07980685 0.08218561 0.08552944
 0.09015041 0.09636055 0.10447192 0.11479657 0.12764654 0.14333389
 0.16217067]
yloc =  [0.18435151 0.20957609 0.23741366 0.26743346 0.29920475 0.33229677
 0.36627877 0.40072001 0.43518972 0.46925716 0.50249157 0.53446221
 0.56473833 0.59288917 0.61848397]
yloc =  [0.64114776 0.66078996 0.67741049 0.69100931 0.70158637 0.70914161
 0.71367499 0.71518647 0.71367598 0.70914349 0.70158895 0.69101231
 0.67741352 0.66079253 0.6411493 ]
yloc =  [0.61848381 0.59288659 0.5647328  0.53445339 0.50247933 0.46924157
 0.43517106 0.40069877 0.36625565 0.33227265 0.29918073 0.26741085
 0.23739396 0.20956103 0.184343  ]
yloc =  [0.16217084 0.14334488 0.12766976 0.11483251 0.1045202  0.09641988
 0.09021858 0.08560336 0.08226127 0.07987935 0.07814466 0.07674425
 0.07536516]
yloc =  [0.07369504 0.07154072 0.06897208 0.06609414 0.06301191 0.0598304
 0.05665464 0.05358962 0.05074037 0.0482119 ]
yloc =  [0.04608075 0.04426668 0.04263586 0.04105439 0.03938837]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 99
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.01064407  0.0415022   0.23787734 -0.30777139 -0.30777139
  0.23787734  0.0415022   0.01064407  0.          0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.08056818 0.46763593 0.15324979 0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.15324979 0.72836004 0.21093023 0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.21093023 0.91778719 0.24796336 0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.24796336 1.01737494 0.26072411
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.26072411 1.01737494
  0.24796336 0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.24796336
  0.91778719 0.21093023 0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.21093023 0.72836004 0.15324979 0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.15324979 0.46763593 0.08056818 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.08056818 0.16113636 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.04061699 -0.05448554  0.35539121 -0.30973734 -0.30981552
  0.35562975 -0.05543159  0.04478498 -0.02239249  0.        ]
yloc =  [0.03938837 0.04083157 0.04235574 0.04404181 0.04597076]
yloc =  [0.04822349 0.0508404  0.05374335 0.05683269 0.06000877 0.06317193
 0.06622251 0.06906086 0.07158732 0.07370225]
yloc =  [0.07534059 0.07669639 0.07808113 0.07980685 0.08218561 0.08552944
 0.09015041 0.09636055 0.10447192 0.11479657 0.12764654 0.14333389
 0.16217067]
yloc =  [0.18435151 0.20957609 0.23741366 0.26743346 0.29920475 0.33229677
 0.36627877 0.40072001 0.43518972 0.46925716 0.50249157 0.53446221
 0.56473833 0.59288917 0.61848397]
yloc =  [0.64114776 0.66078996 0.67741049 0.69100931 0.70158637 0.70914161
 0.71367499 0.71518647 0.71367598 0.70914349 0.70158895 0.69101231
 0.67741352 0.66079253 0.6411493 ]
yloc =  [0.61848381 0.59288659 0.5647328  0.53445339 0.50247933 0.46924157
 0.43517106 0.40069877 0.36625565 0.33227265 0.29918073 0.26741085
 0.23739396 0.20956103 0.184343  ]
yloc =  [0.16217084 0.14334488 0.12766976 0.11483251 0.1045202  0.09641988
 0.09021858 0.08560336 0.08226127 0.07987935 0.07814466 0.07674425
 0.07536516]
yloc =  [0.07369504 0.07154072 0.06897208 0.06609414 0.06301191 0.0598304
 0.05665464 0.05358962 0.05074037 0.0482119 ]
yloc =  [0.04608075 0.04426668 0.04263586 0.04105439 0.03938837]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 99
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.27114227 -0.60990735  0.27114227  0.          0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.31916917 -0.47929939  0.35286475 -0.17643238  0.        ]
yloc =  [0.04235007 0.03640173 0.03060456 0.0251097  0.02006833 0.0156316
 0.01195067 0.00917671 0.00746087 0.00695432 0.00780822 0.01017372
 0.01420199 0.02004418 0.02785147 0.037775   0.04996595 0.06457547
 0.08175471 0.10165486]
yloc =  [0.12438002 0.1497813  0.17762503 0.2076775  0.23970499 0.27347379
 0.30875018 0.34530045 0.38289088 0.42128775 0.46025736 0.49956597
 0.53897988 0.57826537 0.61718873 0.65551624 0.69301417 0.72944883
 0.76458649 0.79819344 0.83003595 0.85988032 0.88749283 0.91263977
 0.9350874  0.95460203 0.97094994 0.98389741 0.99321071 0.99865615
 1.        ]
yloc =  [0.99708809 0.99008446 0.97923269 0.96477634 0.94695901 0.92602427
 0.90221569 0.87577686 0.84695136 0.81598276 0.78311465 0.74859059
 0.71265418 0.67554899 0.63751859 0.59880657 0.55965651 0.52031198
 0.48101657 0.44201384 0.40354738 0.36586078 0.3291976  0.29380143
 0.25991584 0.22778441 0.19765073 0.16975837 0.14435091 0.12167192]
yloc =  [0.10196492 0.08536457 0.07168059 0.06066231 0.05205903 0.0456201
 0.04109482 0.03823251 0.03678251 0.03649412 0.03711668 0.0383995
 0.04009191 0.04194321 0.04370275 0.04511983 0.04594379 0.04592393
 0.04480958 0.04235007]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 99
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.00176417  0.00351015  0.00647762  0.01229336  0.02535679
  0.05922053  0.1556776   0.29233211 -0.57209505 -0.57209505  0.29233211
  0.1556776   0.05922053  0.02535679  0.01229336  0.00647762  0.00351015
  0.00176417  0.          0.        ]
A matrix:  

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.01080065  0.01112161  0.01439204  0.02466994  0.0306343
  0.10330541  0.08625083  0.82088511 -1.04228478 -1.04228476  0.82088505
  0.08625105  0.10330455  0.03063764  0.02465659  0.01444682  0.01088751
  0.01187624 -0.00593812  0.        ]
yloc =  [0.03869055 0.04022456]
yloc =  [0.04183925 0.04356212]
yloc =  [0.0453947  0.04734125 0.04941049 0.05161153]
yloc =  [0.05395441 0.05645722 0.05914202 0.06203088]
yloc =  [0.06514587 0.0685063  0.07212402 0.0760097  0.08017398 0.08462752]
yloc =  [0.08938419 0.09451162 0.10012192 0.10632851 0.11324484 0.12098433]
yloc =  [0.12966022 0.13934634 0.15003001 0.16168706 0.17429332 0.18782462
 0.20225678]
yloc =  [0.21756685 0.23401015 0.25247468 0.27393587 0.29936916 0.32974998
 0.36605377 0.40925597]
yloc =  [0.46013311 0.51746727 0.57889021 0.64201978 0.70447384 0.76387026
 0.8178269  0.86396163]
yloc =  [0.90021693 0.92611364 0.94165167 0.94683102 0.94165167 0.92611364
 0.90021693]
yloc =  [0.86396163 0.8178269  0.76387026 0.70447384 0.64201978 0.57889021
 0.51746728 0.46013311]
yloc =  [0.40925597 0.36605377 0.32974998 0.29936915 0.27393587 0.25247468
 0.23401015 0.21756685]
yloc =  [0.20225679 0.18782463 0.17429334 0.16168708 0.15003003 0.13934635
 0.12966022]
yloc =  [0.12098432 0.1132448  0.10632846 0.10012185 0.09451156 0.08938416]
yloc =  [0.08462755 0.08017409 0.07600988 0.07212423 0.06850646 0.0651459 ]
yloc =  [0.06203066 0.05914155 0.05645664 0.053954  ]
yloc =  [0.05161171 0.04941157 0.04734276 0.0453954 ]
yloc =  [0.04356025 0.04183607]
yloc =  [0.04022652 0.03869055]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 99
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.00346841  0.00803181  0.01912159  0.0538299   0.18712708
  0.21203166 -0.9992479   0.21203166  0.18712708  0.0538299   0.01912159
  0.00803181  0.00346841  0.          0.        ]
A matrix:  

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.0110543   0.01553798  0.01820598  0.07019408  0.08030818
  0.75860721 -1.82113847  0.75860632  0.08031183  0.07017973  0.01826385
  0.01529403  0.01216363 -0.00608182  0.        ]
yloc =  [0.0388699  0.040431   0.04204213]
yloc =  [0.04374975 0.04557512 0.04752865 0.04962071]
yloc =  [0.05186152 0.05425822 0.05681517 0.05953666 0.06242695 0.06549032]
yloc =  [0.06873151 0.07217927 0.07589676 0.0799498  0.08440424 0.08932591
 0.09478063 0.10083424]
yloc =  [0.10755105 0.11496736 0.12309498 0.13194491 0.14152815 0.15185567
 0.16293847 0.17478754 0.18741387]
yloc =  [0.20083841 0.21537691 0.23168214 0.25042523 0.27227734 0.29790964
 0.32799328 0.3631994  0.40419918 0.45166375]
yloc =  [0.50621612 0.56708131 0.63190325 0.69824094 0.76365335 0.82569946
 0.88193827 0.92992874 0.96722987 0.99140063 1.        ]
yloc =  [0.99140064 0.9672299  0.92992879 0.88193832 0.82569952 0.76365341
 0.698241   0.6319033  0.56708134 0.50621614]
yloc =  [0.45166374 0.40419912 0.36319931 0.32799314 0.29790948 0.27227717
 0.25042505 0.23168198 0.2153768  0.20083836]
yloc =  [0.18741394 0.17478774 0.1629388  0.15185613 0.1415287  0.1319455
 0.12309553 0.11496778 0.10755123]
yloc =  [0.10083406 0.09477998 0.08932479 0.08440273 0.07994807 0.07589507
 0.07217799 0.06873108]
yloc =  [0.06549125 0.06242951 0.05954062 0.05681983 0.05426239 0.05186354]
yloc =  [0.04961849 0.0475213  0.04556481 0.04374177]
yloc =  [0.04204486 0.04044617 0.0388699 ]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 99
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.00985307  0.01815039  0.03660477  0.08154158  0.18864097
  0.24705882 -0.6        -0.6         0.24705882  0.18864097  0.08154158
  0.03660477  0.01815039  0.          0.        ]
A matrix:  

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.01573065  0.025755    0.04460285  0.12527658  0.18816507
  0.81983191 -1.24396328 -1.24397878  0.81987841  0.18799455  0.12591215
  0.04223111  0.0346064  -0.0173032   0.        ]
yloc =  [0.03846154 0.04010572 0.04177351 0.04348848 0.04527424 0.04715439
 0.04915252]
yloc =  [0.05129217 0.05359371 0.05607261 0.0587439  0.06162262 0.06472381
 0.0680625 ]
yloc =  [0.07165437 0.07552273 0.07969576 0.08420173 0.08906891 0.09432558
 0.1       ]
yloc =  [0.1        0.10613591 0.11283886 0.12022985 0.12842991 0.13756004
 0.14774125]
yloc =  [0.15909439 0.17173042 0.18574499 0.20123244 0.21828709 0.23700329
 0.25747536]
yloc =  [0.27983977 0.30472276 0.33306657 0.3658187  0.40392665 0.44833792
 0.5       ]
yloc =  [0.5        0.55918654 0.6234757  0.6897718  0.75497914 0.81600203
 0.86974477]
yloc =  [0.91313078 0.94423003 0.96288961 0.9691095  0.96288969 0.94423014
 0.91313083]
yloc =  [0.86974462 0.8160016  0.75497842 0.68977089 0.62347479 0.55918589
 0.5       ]
yloc =  [0.5        0.44833895 0.40392887 0.36582191 0.33307027 0.3047261
 0.27984159]
yloc =  [0.25747418 0.23699789 0.21827737 0.20121952 0.18573119 0.17171928
 0.15909065]
yloc =  [0.14775059 0.13758577 0.12847086 0.12028035 0.11288872 0.10617044
 0.1       ]
yloc =  [0.1        0.09427088 0.08895263 0.08403383 0.07950302 0.07534877
 0.07155965]
yloc =  [0.06812381 0.0650048  0.06212803 0.05941564 0.05678977 0.05417255
 0.05148611]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [inf inf inf inf inf inf nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.00633484  0.00976693  0.01576027  0.02680547  0.04827586
  0.09124668  0.16923077  0.21538462 -0.2        -0.8        -0.2
  0.21538462  0.16923077  0.09124668  0.04827586  0.02680547  0.01576027
  0.00976693  0.          0.        ]
A matrix:  

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.01446173  0.01817117  0.03005669  0.05072525  0.08870789
  0.17375355  0.31123814  0.61206312 -0.17487522 -2.31256222 -0.17487589
  0.6120658   0.31122808  0.1737911   0.08856773  0.05124833  0.02810453
  0.02545674 -0.01272837  0.        ]
yloc =  [0.03846154 0.0400653  0.04169799 0.04338852 0.04516583 0.04705882]
yloc =  [0.04705882 0.04909285 0.05127892 0.05362444 0.05613684 0.05882353]
yloc =  [0.05882353 0.06169466 0.06477126 0.06807713 0.07163601 0.0754717 ]
yloc =  [0.0754717  0.07961088 0.08409196 0.08895628 0.09424518 0.1       ]
yloc =  [0.1        0.10626784 0.1131189  0.12062914 0.12887453 0.13793103]
yloc =  [0.13793103 0.1478903  0.15890674 0.17115045 0.1847915  0.2       ]
yloc =  [0.2        0.21696351 0.23593953 0.25720302 0.28102896 0.30769231]
yloc =  [0.30769231 0.33752248 0.37106669 0.40892658 0.4517038  0.5       ]
yloc =  [0.5        0.55405424 0.61265524 0.67422912 0.737202   0.8       ]
yloc =  [0.8        0.860599   0.91517387 0.95944925 0.98914975 1.        ]
yloc =  [1.         0.98914975 0.95944926 0.91517389 0.86059901 0.8       ]
yloc =  [0.8        0.73720198 0.67422909 0.61265521 0.55405422 0.5       ]
yloc =  [0.5        0.45170385 0.40892668 0.37106681 0.33752258 0.30769231]
yloc =  [0.30769231 0.28102878 0.25720266 0.23593907 0.21696314 0.2       ]
yloc =  [0.2        0.18479217 0.17115181 0.15890846 0.14789169 0.13793103]
yloc =  [0.13793103 0.12887203 0.12062406 0.11311249 0.10626269 0.1       ]
yloc =  [0.1        0.09425452 0.08897524 0.08411587 0.07963012 0.0754717 ]
yloc =  [0.0754717  0.07160116 0.06800636 0.06468203 0.06162285 0.05882353]
yloc =  [0.05882353 0.05626693 0.05388854 0.05161197 0.04936085 0.04705882]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan inf inf inf inf nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 133, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 28, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 71, in create_natural_spline
    b[end] = -1 + (yint[end] - yint[end-1])/h[end - 1]
IndexError: index 6 is out of bounds for axis 0 with size 6

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 71
    b[end] = -1 + (yint[end] - yint[end-1])/h[end - 1]
RuntimeWarning: divide by zero encountered in scalar divide
B vector [-0.96923077  0.16923077 -0.2        -0.2         0.                -inf]
A matrix:  [[0.66666667 0.33333333 0.         0.         0.         0.        ]
 [0.33333333 1.33333333 0.33333333 0.         0.         0.        ]
 [0.         0.33333333 1.33333333 0.33333333 0.         0.        ]
 [0.         0.         0.33333333 1.33333333 0.33333333 0.        ]
 [0.         0.         0.         0.33333333 0.66666667 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 133, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 28, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 88, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
last term 0.0
h[end] 0.0

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 75
    b[end] = -1 + (yint[end] - yint[end-1])/h[end - 1]
RuntimeWarning: divide by zero encountered in scalar divide
B vector [-0.96923077  0.16923077 -0.2        -0.2         0.                -inf]
A matrix:  [[0.66666667 0.33333333 0.         0.         0.         0.        ]
 [0.33333333 1.33333333 0.33333333 0.         0.         0.        ]
 [0.         0.33333333 1.33333333 0.33333333 0.         0.        ]
 [0.         0.         0.33333333 1.33333333 0.33333333 0.        ]
 [0.         0.         0.         0.33333333 0.66666667 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 137, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 28, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 92, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
last term 0.0
h[end] 0.0

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 75
    b[end] = -1 + (yint[end] - yint[end-1])/h[end - 1]
RuntimeWarning: divide by zero encountered in scalar divide
B vector [-0.96923077  0.16923077 -0.2        -0.2         0.                -inf]
A matrix:  [[0.66666667 0.33333333 0.         0.         0.         0.        ]
 [0.33333333 1.33333333 0.33333333 0.         0.         0.        ]
 [0.         0.33333333 1.33333333 0.33333333 0.         0.        ]
 [0.         0.         0.33333333 1.33333333 0.33333333 0.        ]
 [0.         0.         0.         0.33333333 0.66666667 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 137, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 28, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 92, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
last term 0.0
h vec [2. 2. 2. 2. 0. 0.]
h[end] 0.0

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 75
    b[end] = -1 + (yint[end] - yint[end-1])/h[end - 1]
RuntimeWarning: divide by zero encountered in scalar divide
B vector [-0.96923077  0.16923077 -0.2        -0.2         0.                -inf]
A matrix:  [[0.66666667 0.33333333 0.         0.         0.         0.        ]
 [0.33333333 1.33333333 0.33333333 0.         0.         0.        ]
 [0.         0.33333333 1.33333333 0.33333333 0.         0.        ]
 [0.         0.         0.33333333 1.33333333 0.33333333 0.        ]
 [0.         0.         0.         0.33333333 0.66666667 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 137, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 28, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 92, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
last term 0.0
h vec [2. 2. 2. 2. 0. 0.]
xint [-5. -3. -1.  1.  3.  5.]
h[end] 0.0

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 76
    b[end] = -1 + (yint[end] - yint[end-1])/h[end - 1]
RuntimeWarning: divide by zero encountered in scalar divide
B vector [-0.96923077  0.16923077 -0.2        -0.2         0.                -inf]
A matrix:  [[0.66666667 0.33333333 0.         0.         0.         0.        ]
 [0.33333333 1.33333333 0.33333333 0.         0.         0.        ]
 [0.         0.33333333 1.33333333 0.33333333 0.         0.        ]
 [0.         0.         0.33333333 1.33333333 0.33333333 0.        ]
 [0.         0.         0.         0.33333333 0.66666667 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 138, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 28, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 93, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix
y = [0,1,2]
y[-1]
2
y[-2]
1

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
h vec [2. 2. 2. 2. 2.]
xint [-5. -3. -1.  1.  3.  5.]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 141, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 28, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 79, in create_natural_spline
    b[end] = -1 + (yint[-1] - yint[-2])/h[N-1]
NameError: name 'end' is not defined. Did you mean: 'endh'?

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
h vec [2. 2. 2. 2. 2.]
xint [-5. -3. -1.  1.  3.  5.]
B vector [-0.96923077  0.16923077 -0.2        -0.2         0.         -1.03076923]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 141, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 28, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 93, in create_natural_spline
    A[N][N] = h[end-1]/3
NameError: name 'end' is not defined. Did you mean: 'endh'?
y[-1] = 3
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    y[-1] = 3
NameError: name 'y' is not defined
y = [0,1,2]
y[-1] = 3
y
[0, 1, 3]

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
h vec [2. 2. 2. 2. 2.]
xint [-5. -3. -1.  1.  3.  5.]
B vector [-0.96923077  0.16923077 -0.2        -0.2         0.         -1.03076923]
A matrix:  [[0.66666667 0.33333333 0.         0.         0.         0.        ]
 [0.33333333 1.33333333 0.33333333 0.         0.         0.        ]
 [0.         0.33333333 1.33333333 0.33333333 0.         0.        ]
 [0.         0.         0.33333333 1.33333333 0.33333333 0.        ]
 [0.         0.         0.         0.33333333 1.33333333 0.33333333]
 [0.         0.         0.         0.         0.33333333 0.66666667]]
M = [-1.77055576  0.63341921 -0.25542878 -0.21170409  0.50224512 -1.79727641]
yloc =  [0.03846154 0.12980909 0.20465307 0.26419547 0.30963828 0.34218347
 0.36303305 0.373389   0.37445329 0.36742794 0.35351491 0.33391619
 0.30983379 0.28246967 0.25302584 0.22270427 0.19270696 0.16423589
 0.13849304 0.11668042 0.1       ]
yloc =  [0.1        0.08937937 0.08464851 0.08536299 0.0910784  0.10135029
 0.11573427 0.13378589 0.15506073 0.17911437 0.20550239 0.23378036
 0.26350386 0.29422847 0.32550975 0.35690329 0.38796467 0.41824945
 0.44731321 0.47471154 0.5       ]
yloc =  [0.5        0.52281189 0.54309135 0.56086025 0.57614045 0.58895381
 0.59932219 0.60726746 0.61281148 0.61597611 0.61678322 0.61525466
 0.61141229 0.60527799 0.59687361 0.58622102 0.57334207 0.55825863
 0.54099257 0.52156573 0.5       ]
yloc =  [0.5        0.47637308 0.45098609 0.42419601 0.39635981 0.36783447
 0.33897696 0.31014426 0.28169334 0.25398117 0.22736474 0.20220101
 0.17884696 0.15765957 0.1389958  0.12321264 0.11066706 0.10171603
 0.09671653 0.09602552 0.1       ]
yloc =  [0.1        0.12566888 0.15521045 0.18747495 0.22131262 0.2555737
 0.28910843 0.32076704 0.34939978 0.37385688 0.39298859 0.40564514
 0.41067678 0.40693373 0.39326625 0.36852457 0.33155893 0.28121956
 0.21635672 0.13582063 0.03846154]
nerr =  1.8599387701109849

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 142, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 30, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 79, in create_natural_spline
    b[0] = ypint[0] + (yint[1] - yint[0])/h[0]
NameError: name 'ypint' is not defined. Did you mean: 'yint'?

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
M = [-0.0175901   0.17186659 -0.16218397 -0.12313072  0.05470683 -0.09569661]
yloc =  [0.03846154 0.03691009 0.03527746 0.03365839 0.03214761 0.03083983
 0.0298298  0.02921224 0.02908187 0.02953343 0.03066165 0.03256124
 0.03532695 0.0390535  0.04383561 0.04976802 0.05694545 0.06546264
 0.07541431 0.08689519 0.1       ]
yloc =  [0.1        0.11477985 0.13111135 0.14882746 0.16776116 0.18774543
 0.20861323 0.23019755 0.25233136 0.27484763 0.29757934 0.32035947
 0.34302098 0.36539685 0.38732006 0.40862359 0.4291404  0.44870347
 0.46714578 0.4843003  0.5       ]
yloc =  [0.5        0.51410896 0.5266156  0.53753946 0.54690005 0.55471692
 0.56100958 0.56579755 0.56910038 0.57093757 0.57132867 0.5702932
 0.56785067 0.56402063 0.55882259 0.55227609 0.54440065 0.53521579
 0.52474104 0.51299594 0.5       ]
yloc =  [0.5        0.48578432 0.47042625 0.45401471 0.43663862 0.4183869
 0.39934847 0.37961224 0.35926713 0.33840207 0.31710597 0.29546775
 0.27357633 0.25152063 0.22938956 0.20727205 0.18525702 0.16343338
 0.14189005 0.12071595 0.1       ]
yloc =  [0.1        0.09672684 0.09392555 0.09152093 0.08943776 0.08760086
 0.08593502 0.08436503 0.08281571 0.08121183 0.07947821 0.07753964
 0.07532093 0.07274685 0.06974223 0.06623185 0.06214051 0.05739301
 0.05191415 0.04562873 0.03846154]
nerr =  1.342895288230576

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
M = [ 0.11231041 -0.01369148  0.06734239  0.09726311  0.74360515 -1.87168373
  0.74312978  0.09916461  0.06021179  0.01292939 -0.11192937]
yloc =  [0.03846154 0.0375228  0.03758116 0.03851063 0.04018519 0.04247885
 0.0452656  0.04841945 0.05181439 0.05532442 0.05882353]
yloc =  [0.05882353 0.06222023 0.06556106 0.06892704 0.0723992  0.07605858
 0.07998622 0.08426315 0.0889704  0.094189   0.1       ]
yloc =  [0.1        0.1064759  0.11365515 0.12156766 0.13024335 0.13971216
 0.15000399 0.16114877 0.17317641 0.18611685 0.2       ]
yloc =  [0.2        0.21495852 0.23153601 0.25037881 0.27213327 0.29744573
 0.32696254 0.36133002 0.40119453 0.44720241 0.5       ]
yloc =  [0.5        0.55969003 0.62420083 0.6909171  0.75722356 0.82050491
 0.87814587 0.92753115 0.96604545 0.9910735  1.        ]
yloc =  [1.         0.99108135 0.96606067 0.92755278 0.87817249 0.82053462
 0.75725398 0.69094539 0.62422365 0.55970358 0.5       ]
yloc =  [0.5        0.44718459 0.4011565  0.36127179 0.32688648 0.2973566
 0.2720382  0.2502873  0.23145995 0.21491217 0.2       ]
yloc =  [0.2        0.18618031 0.17331332 0.16136007 0.1502816  0.14003897
 0.13059323 0.12190541 0.11393657 0.10664775 0.1       ]
yloc =  [0.1        0.09395298 0.0884608  0.08347617 0.07895181 0.07484044
 0.07109478 0.06766754 0.06451144 0.06157919 0.05882353]
yloc =  [0.05882353 0.05826568 0.05771226 0.05703842 0.0561193  0.05483003
 0.05304577 0.05064165 0.04749281 0.04347439 0.03846154]
nerr =  0.07442360466708572

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
M = [ 0.16209625 -0.02770291  0.03739299  0.04148443  0.12611225  0.1879408
  0.81989333 -1.2439847  -1.24395453  0.81980281  0.18827269  0.12487519
  0.0461008   0.02016459  0.03659435 -0.16654197]
yloc =  [0.03846154 0.03774528 0.03836529 0.04003686 0.04247529 0.0453959
 0.04851397]
yloc =  [0.05154717 0.05435478 0.05701554 0.05962711 0.06228714 0.06509325
 0.06814311]
yloc =  [0.07152983 0.075294   0.07944234 0.08398097 0.08891603 0.09425366
 0.1       ]
yloc =  [0.1        0.10618132 0.11290442 0.12029625 0.12848375 0.13759387
 0.14775353]
yloc =  [0.15908948 0.17171578 0.18572685 0.20121545 0.21827432 0.23699619
 0.25747381]
yloc =  [0.27984216 0.30472715 0.33307142 0.36582292 0.40392956 0.44833928
 0.5       ]
yloc =  [0.5        0.5591857  0.62347451 0.68977062 0.75497822 0.81600148
 0.86974459]
yloc =  [0.91313084 0.94423014 0.96288965 0.96910942 0.9628895  0.94422992
 0.91313074]
yloc =  [0.86974487 0.81600232 0.75497961 0.68977239 0.62347629 0.55918695
 0.5       ]
yloc =  [0.5        0.44833725 0.40392524 0.36581667 0.33306424 0.30472065
 0.27983862]
yloc =  [0.2574761  0.2370067  0.21829323 0.2012406  0.1857537  0.17173745
 0.15909674]
yloc =  [0.14773535 0.13754379 0.12840405 0.12019796 0.11280736 0.1061141
 0.1       ]
yloc =  [0.1        0.09436012 0.08914235 0.08430777 0.07981749 0.0756326
 0.0717142 ]
yloc =  [0.06802377 0.06454634 0.06130342 0.05831965 0.05561967 0.05322813
 0.05116967]
yloc =  [0.05010955 0.04953864 0.04882583 0.04766642 0.04575571 0.04278898
 0.03846154]
nerr =  0.07742258917641649

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
M = [ 0.2132662  -0.04268278  0.03348299  0.0259539   0.05182459  0.08841332
  0.17383247  0.311217    0.61206875 -0.17487662 -2.31256228 -0.17487427
  0.61205935  0.31125224  0.17370092  0.08890428  0.04999231  0.03279207
  0.0079626   0.05256063 -0.21820513]
yloc =  [0.03846154 0.03796326 0.03908575 0.04131711 0.04414543 0.04705882]
yloc =  [0.04705882 0.04965609 0.05197887 0.05417948 0.05641025 0.05882353]
yloc =  [0.05882353 0.06154374 0.06458371 0.06792841 0.07156275 0.0754717 ]
yloc =  [0.0754717  0.07965131 0.08414221 0.08899613 0.09426481 0.1       ]
yloc =  [0.1        0.10625701 0.11310543 0.12061846 0.12886927 0.13793103]
yloc =  [0.13793103 0.14789321 0.15891035 0.17115331 0.18479291 0.2       ]
yloc =  [0.2        0.21696274 0.23593857 0.25720226 0.28102858 0.30769231]
yloc =  [0.30769231 0.33752269 0.37106695 0.40892679 0.4517039  0.5       ]
yloc =  [0.5        0.55405419 0.61265517 0.67422906 0.73720197 0.8       ]
yloc =  [0.8        0.86059902 0.9151739  0.95944927 0.98914976 1.        ]
yloc =  [1.         0.98914974 0.95944924 0.91517386 0.86059899 0.8       ]
yloc =  [0.8        0.73720202 0.67422916 0.61265529 0.55405428 0.5       ]
yloc =  [0.5        0.45170373 0.40892644 0.37106652 0.33752234 0.30769231]
yloc =  [0.30769231 0.28102921 0.25720354 0.23594018 0.21696403 0.2       ]
yloc =  [0.2        0.18479056 0.17114854 0.15890434 0.14788837 0.13793103]
yloc =  [0.13793103 0.12887804 0.12063626 0.11312788 0.10627506 0.1       ]
yloc =  [0.1        0.0942321  0.08892971 0.08405845 0.07958392 0.0754717 ]
yloc =  [0.0754717  0.07168486 0.06817628 0.06489631 0.06179528 0.05882353]
yloc =  [0.05882353 0.05595455 0.0532544  0.05081226 0.04871734 0.04705882]
yloc =  [0.04705882 0.04645428 0.04583381 0.04465589 0.04237897 0.03846154]
nerr =  0.010845764657746849

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 81
    b[-1] = ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: invalid value encountered in scalar divide
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 142, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 30, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 97, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
h vec [0.12273707 0.24245194 0.35619684 0.46117099 0.55478959 0.63474742
 0.69907566 0.74619034 0.77493134 0.78459096 0.77493134 0.74619034
 0.69907566 0.63474742 0.55478959 0.46117099 0.35619684 0.24245194
 0.12273707 0.        ]
xint [-4.98458667 -4.8618496  -4.61939766 -4.26320082 -3.80202983 -3.24724024
 -2.61249282 -1.91341716 -1.16722682 -0.39229548  0.39229548  1.16722682
  1.91341716  2.61249282  3.24724024  3.80202983  4.26320082  4.61939766
  4.8618496   4.98458667  4.98458667]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 81
    b[-1] = ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.03038616  0.00176417  0.00351015  0.00647762  0.01229336  0.02535679
  0.05922053  0.1556776   0.29233211 -0.57209505 -0.57209505  0.29233211
  0.1556776   0.05922053  0.02535679  0.01229336  0.00647762  0.00351015
  0.00176417  0.                 nan]
A matrix:  [[0.04091236 0.02045618 0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.02045618 0.12172967 0.04040866 0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.04040866 0.19954959 0.05936614 0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.05936614 0.27245594 0.07686183 0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.07686183 0.33865353 0.09246493
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.09246493 0.39651233
  0.10579124 0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.10579124
  0.44460769 0.11651261 0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.11651261 0.48175533 0.12436506 0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.12436506 0.50704056 0.12915522 0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.12915522 0.51984077 0.13076516 0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.13076516 0.51984077 0.12915522
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.12915522 0.50704056
  0.12436506 0.         0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.12436506
  0.48175533 0.11651261 0.         0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.11651261 0.44460769 0.10579124 0.         0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.10579124 0.39651233 0.09246493 0.         0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.09246493 0.33865353 0.07686183 0.
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.07686183 0.27245594 0.05936614
  0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.05936614 0.19954959
  0.04040866 0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.04040866
  0.12172967 0.02045618 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.02045618 0.04091236 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 142, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 30, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 97, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.00633484  0.00976693  0.01576027  0.02680547  0.04827586
  0.09124668  0.16923077  0.21538462 -0.2        -0.8        -0.2
  0.21538462  0.16923077  0.09124668  0.04827586  0.02680547  0.01576027
  0.00976693  0.          0.        ]
A matrix:  

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.01446173  0.01817117  0.03005669  0.05072525  0.08870789
  0.17375355  0.31123814  0.61206312 -0.17487522 -2.31256222 -0.17487589
  0.6120658   0.31122808  0.1737911   0.08856773  0.05124833  0.02810453
  0.02545674 -0.01272837  0.        ]
yloc =  [0.03846154 0.0400653  0.04169799 0.04338852 0.04516583 0.04705882]
yloc =  [0.04705882 0.04909285 0.05127892 0.05362444 0.05613684 0.05882353]
yloc =  [0.05882353 0.06169466 0.06477126 0.06807713 0.07163601 0.0754717 ]
yloc =  [0.0754717  0.07961088 0.08409196 0.08895628 0.09424518 0.1       ]
yloc =  [0.1        0.10626784 0.1131189  0.12062914 0.12887453 0.13793103]
yloc =  [0.13793103 0.1478903  0.15890674 0.17115045 0.1847915  0.2       ]
yloc =  [0.2        0.21696351 0.23593953 0.25720302 0.28102896 0.30769231]
yloc =  [0.30769231 0.33752248 0.37106669 0.40892658 0.4517038  0.5       ]
yloc =  [0.5        0.55405424 0.61265524 0.67422912 0.737202   0.8       ]
yloc =  [0.8        0.860599   0.91517387 0.95944925 0.98914975 1.        ]
yloc =  [1.         0.98914975 0.95944926 0.91517389 0.86059901 0.8       ]
yloc =  [0.8        0.73720198 0.67422909 0.61265521 0.55405422 0.5       ]
yloc =  [0.5        0.45170385 0.40892668 0.37106681 0.33752258 0.30769231]
yloc =  [0.30769231 0.28102878 0.25720266 0.23593907 0.21696314 0.2       ]
yloc =  [0.2        0.18479217 0.17115181 0.15890846 0.14789169 0.13793103]
yloc =  [0.13793103 0.12887203 0.12062406 0.11311249 0.10626269 0.1       ]
yloc =  [0.1        0.09425452 0.08897524 0.08411587 0.07963012 0.0754717 ]
yloc =  [0.0754717  0.07160116 0.06800636 0.06468203 0.06162285 0.05882353]
yloc =  [0.05882353 0.05626693 0.05388854 0.05161197 0.04936085 0.04705882]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan inf inf inf inf nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
h vec [1.81635632 2.93892626 2.93892626 1.81635632 0.        ]
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 81
    b[-1] = ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.05086888  0.27114227 -0.60990735  0.27114227  0.                 nan]
A matrix:  [[0.60545211 0.30272605 0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 142, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 30, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 97, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
B vector [ 0.          0.00176417  0.00351015  0.00647762  0.01229336  0.02535679
  0.05922053  0.1556776   0.29233211 -0.57209505 -0.57209505  0.29233211
  0.1556776   0.05922053  0.02535679  0.01229336  0.00647762  0.00351015
  0.00176417  0.          0.        ]
A matrix:  

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 89
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.01080065  0.01112161  0.01439204  0.02466994  0.0306343
  0.10330541  0.08625083  0.82088511 -1.04228478 -1.04228476  0.82088505
  0.08625105  0.10330455  0.03063764  0.02465659  0.01444682  0.01088751
  0.01187624 -0.00593812  0.        ]
yloc =  [0.03869055 0.04022456]
yloc =  [0.04183925 0.04356212]
yloc =  [0.0453947  0.04734125 0.04941049 0.05161153]
yloc =  [0.05395441 0.05645722 0.05914202 0.06203088]
yloc =  [0.06514587 0.0685063  0.07212402 0.0760097  0.08017398 0.08462752]
yloc =  [0.08938419 0.09451162 0.10012192 0.10632851 0.11324484 0.12098433]
yloc =  [0.12966022 0.13934634 0.15003001 0.16168706 0.17429332 0.18782462
 0.20225678]
yloc =  [0.21756685 0.23401015 0.25247468 0.27393587 0.29936916 0.32974998
 0.36605377 0.40925597]
yloc =  [0.46013311 0.51746727 0.57889021 0.64201978 0.70447384 0.76387026
 0.8178269  0.86396163]
yloc =  [0.90021693 0.92611364 0.94165167 0.94683102 0.94165167 0.92611364
 0.90021693]
yloc =  [0.86396163 0.8178269  0.76387026 0.70447384 0.64201978 0.57889021
 0.51746728 0.46013311]
yloc =  [0.40925597 0.36605377 0.32974998 0.29936915 0.27393587 0.25247468
 0.23401015 0.21756685]
yloc =  [0.20225679 0.18782463 0.17429334 0.16168708 0.15003003 0.13934635
 0.12966022]
yloc =  [0.12098432 0.1132448  0.10632846 0.10012185 0.09451156 0.08938416]
yloc =  [0.08462755 0.08017409 0.07600988 0.07212423 0.06850646 0.0651459 ]
yloc =  [0.06203066 0.05914155 0.05645664 0.053954  ]
yloc =  [0.05161171 0.04941157 0.04734276 0.0453954 ]
yloc =  [0.04356025 0.04183607]
yloc =  [0.04022652 0.03869055]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 99
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
h vec [4.33012702 4.33012702 0.        ]
xint [-4.33012702e+00  3.06161700e-16  4.33012702e+00  4.33012702e+00]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 81
    b[-1] = ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.24144916 -0.43849388  0.                 nan]
A matrix:  [[1.44337567 0.72168784 0.         0.        ]
 [0.72168784 2.88675135 0.72168784 0.        ]
 [0.         0.72168784 1.44337567 0.        ]
 [0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 142, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 30, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 97, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 142, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 26, in driver
    xeval =  np.linspace(xint[0],xint[Nint],Neval+1)
IndexError: index 3 is out of bounds for axis 0 with size 3

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [4.33012702 4.33012702]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 27, in driver
    xeval =  np.linspace(xint[0],xint[Nint],Neval+1)
IndexError: index 3 is out of bounds for axis 0 with size 2

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
xint [ 4.98458667  4.98458667  4.8618496   4.61939766  4.26320082  3.80202983
  3.24724024  2.61249282  1.91341716  1.16722682  0.39229548 -0.39229548
 -1.16722682 -1.91341716 -2.61249282 -3.24724024 -3.80202983 -4.26320082
 -4.61939766 -4.8618496  -4.98458667]
B vector [ 0.          0.00176417  0.00351015  0.00647762  0.01229336  0.02535679
  0.05922053  0.1556776   0.29233211 -0.57209505 -0.57209505  0.29233211
  0.1556776   0.05922053  0.02535679  0.01229336  0.00647762  0.00351015
  0.00176417  0.          0.        ]
A matrix:  

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 91
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.01080065  0.01112161  0.01439204  0.02466994  0.0306343
  0.10330541  0.08625083  0.82088511 -1.04228478 -1.04228476  0.82088505
  0.08625105  0.10330455  0.03063764  0.02465659  0.01444682  0.01088751
  0.01187624 -0.00593812  0.        ]
yloc =  [0.03869055 0.04022456]
yloc =  [0.04183925 0.04356212]
yloc =  [0.0453947  0.04734125 0.04941049 0.05161153]
yloc =  [0.05395441 0.05645722 0.05914202 0.06203088]
yloc =  [0.06514587 0.0685063  0.07212402 0.0760097  0.08017398 0.08462752]
yloc =  [0.08938419 0.09451162 0.10012192 0.10632851 0.11324484 0.12098433]
yloc =  [0.12966022 0.13934634 0.15003001 0.16168706 0.17429332 0.18782462
 0.20225678]
yloc =  [0.21756685 0.23401015 0.25247468 0.27393587 0.29936916 0.32974998
 0.36605377 0.40925597]
yloc =  [0.46013311 0.51746727 0.57889021 0.64201978 0.70447384 0.76387026
 0.8178269  0.86396163]
yloc =  [0.90021693 0.92611364 0.94165167 0.94683102 0.94165167 0.92611364
 0.90021693]
yloc =  [0.86396163 0.8178269  0.76387026 0.70447384 0.64201978 0.57889021
 0.51746728 0.46013311]
yloc =  [0.40925597 0.36605377 0.32974998 0.29936915 0.27393587 0.25247468
 0.23401015 0.21756685]
yloc =  [0.20225679 0.18782463 0.17429334 0.16168708 0.15003003 0.13934635
 0.12966022]
yloc =  [0.12098432 0.1132448  0.10632846 0.10012185 0.09451156 0.08938416]
yloc =  [0.08462755 0.08017409 0.07600988 0.07212423 0.06850646 0.0651459 ]
yloc =  [0.06203066 0.05914155 0.05645664 0.053954  ]
yloc =  [0.05161171 0.04941157 0.04734276 0.0453954 ]
yloc =  [0.04356025 0.04183607]
yloc =  [0.04022652 0.03869055]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 101
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
xint [ 4.33012702e+00  4.33012702e+00  3.06161700e-16 -4.33012702e+00]
B vector [ 0.         -0.43849388  0.          0.        ]
A matrix:  [[1.         0.         0.         0.        ]
 [0.72168784 2.88675135 0.72168784 0.        ]
 [0.         0.72168784 1.44337567 0.        ]
 [0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 91
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.         -0.17359855  0.08679928  0.        ]
yloc =  [0.05063291 0.08046582 0.11027269 0.14002749 0.16970416 0.19927667
 0.22871899 0.25800506 0.28710886 0.31600434 0.34466546 0.37306618
 0.40118047 0.42898228 0.45644557 0.4835443  0.51025244 0.53654394
 0.56239277 0.58777288 0.61265823 0.63702278 0.66084051 0.68408535
 0.70673128 0.72875226 0.75012224 0.77081519 0.79080506 0.81006582
 0.82857143 0.84629584 0.86321302 0.87929693 0.89452152 0.90886076
 0.92228861 0.93477902 0.94630597 0.9568434  0.96636528 0.97484557
 0.98225823 0.98857722 0.99377649 0.99783002 1.00071175 1.00239566
 1.0028557  1.00206582 1.        ]
yloc =  [0.99664304 0.99202315 0.98617939 0.97915081 0.97097649 0.96169548
 0.95134684 0.93996962 0.92760289 0.91428571 0.90005714 0.88495624
 0.86902206 0.85229367 0.83481013 0.81661049 0.79773382 0.77821917
 0.75810561 0.73743219 0.71623797 0.69456203 0.6724434  0.64992116
 0.62703436 0.60382206 0.58032333 0.55657722 0.53262278 0.5084991
 0.48424521 0.45990018 0.43550307 0.41109295 0.38670886 0.36238987
 0.33817505 0.31410344 0.2902141  0.26654611 0.24313852 0.22003038
 0.19726076 0.17486872 0.15289331 0.1313736  0.11034864 0.0898575
 0.06993924 0.05063291]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 101
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
xint [ 4.75528258e+00  4.75528258e+00  2.93892626e+00  3.06161700e-16
 -2.93892626e+00 -4.75528258e+00]
B vector [ 0.          0.27114227 -0.60990735  0.27114227  0.          0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 90
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 91
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.31916917 -0.47929939  0.35286475 -0.17643238  0.        ]
yloc =  [0.04235007 0.03640173 0.03060456 0.0251097  0.02006833 0.0156316
 0.01195067 0.00917671 0.00746087 0.00695432 0.00780822 0.01017372
 0.01420199 0.02004418 0.02785147 0.037775   0.04996595 0.06457547
 0.08175471 0.10165486]
yloc =  [0.12438002 0.1497813  0.17762503 0.2076775  0.23970499 0.27347379
 0.30875018 0.34530045 0.38289088 0.42128775 0.46025736 0.49956597
 0.53897988 0.57826537 0.61718873 0.65551624 0.69301417 0.72944883
 0.76458649 0.79819344 0.83003595 0.85988032 0.88749283 0.91263977
 0.9350874  0.95460203 0.97094994 0.98389741 0.99321071 0.99865615
 1.        ]
yloc =  [0.99708809 0.99008446 0.97923269 0.96477634 0.94695901 0.92602427
 0.90221569 0.87577686 0.84695136 0.81598276 0.78311465 0.74859059
 0.71265418 0.67554899 0.63751859 0.59880657 0.55965651 0.52031198
 0.48101657 0.44201384 0.40354738 0.36586078 0.3291976  0.29380143
 0.25991584 0.22778441 0.19765073 0.16975837 0.14435091 0.12167192]
yloc =  [0.10196492 0.08536457 0.07168059 0.06066231 0.05205903 0.0456201
 0.04109482 0.03823251 0.03678251 0.03649412 0.03711668 0.0383995
 0.04009191 0.04194321 0.04370275 0.04511983 0.04594379 0.04592393
 0.04480958 0.04235007]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 100
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 101
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [4.75528258e+00 4.75528258e+00 2.93892626e+00 3.06161700e-16]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 27, in driver
    xeval =  np.linspace(xint[0],xint[Nint],Neval+1)
IndexError: index 5 is out of bounds for axis 0 with size 4

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [ 4.75528258e+00  4.75528258e+00  2.93892626e+00  3.06161700e-16
 -2.93892626e+00 -4.75528258e+00]
h vec [1.81635632 2.93892626 2.93892626 1.81635632 0.        ]
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 82
    b[-1] = ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.05086888  0.27114227 -0.60990735  0.27114227  0.                 nan]
A matrix:  [[0.60545211 0.30272605 0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 31, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 98, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
xint [ 4.75528258e+00  4.75528258e+00  2.93892626e+00  3.06161700e-16
 -2.93892626e+00 -4.75528258e+00]
B vector [ 0.          0.27114227 -0.60990735  0.27114227  0.          0.        ]
hvec [1.81635632 2.93892626 2.93892626 1.81635632 0.         0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 91
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 92
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.31916917 -0.47929939  0.35286475 -0.17643238  0.        ]
yloc =  [0.04235007 0.03640173 0.03060456 0.0251097  0.02006833 0.0156316
 0.01195067 0.00917671 0.00746087 0.00695432 0.00780822 0.01017372
 0.01420199 0.02004418 0.02785147 0.037775   0.04996595 0.06457547
 0.08175471 0.10165486]
yloc =  [0.12438002 0.1497813  0.17762503 0.2076775  0.23970499 0.27347379
 0.30875018 0.34530045 0.38289088 0.42128775 0.46025736 0.49956597
 0.53897988 0.57826537 0.61718873 0.65551624 0.69301417 0.72944883
 0.76458649 0.79819344 0.83003595 0.85988032 0.88749283 0.91263977
 0.9350874  0.95460203 0.97094994 0.98389741 0.99321071 0.99865615
 1.        ]
yloc =  [0.99708809 0.99008446 0.97923269 0.96477634 0.94695901 0.92602427
 0.90221569 0.87577686 0.84695136 0.81598276 0.78311465 0.74859059
 0.71265418 0.67554899 0.63751859 0.59880657 0.55965651 0.52031198
 0.48101657 0.44201384 0.40354738 0.36586078 0.3291976  0.29380143
 0.25991584 0.22778441 0.19765073 0.16975837 0.14435091 0.12167192]
yloc =  [0.10196492 0.08536457 0.07168059 0.06066231 0.05205903 0.0456201
 0.04109482 0.03823251 0.03678251 0.03649412 0.03711668 0.0383995
 0.04009191 0.04194321 0.04370275 0.04511983 0.04594379 0.04592393
 0.04480958 0.04235007]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 101
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 102
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]
B vector [ 0.          0.27114227 -0.60990735  0.27114227  0.          0.        ]
hvec [1.81635632 2.93892626 2.93892626 1.81635632 0.         0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 91
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 92
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.31916917 -0.47929939  0.35286475 -0.17643238  0.        ]
yloc =  [0.04235007 0.03640173 0.03060456 0.0251097  0.02006833 0.0156316
 0.01195067 0.00917671 0.00746087 0.00695432 0.00780822 0.01017372
 0.01420199 0.02004418 0.02785147 0.037775   0.04996595 0.06457547
 0.08175471 0.10165486]
yloc =  [0.12438002 0.1497813  0.17762503 0.2076775  0.23970499 0.27347379
 0.30875018 0.34530045 0.38289088 0.42128775 0.46025736 0.49956597
 0.53897988 0.57826537 0.61718873 0.65551624 0.69301417 0.72944883
 0.76458649 0.79819344 0.83003595 0.85988032 0.88749283 0.91263977
 0.9350874  0.95460203 0.97094994 0.98389741 0.99321071 0.99865615
 1.        ]
yloc =  [0.99708809 0.99008446 0.97923269 0.96477634 0.94695901 0.92602427
 0.90221569 0.87577686 0.84695136 0.81598276 0.78311465 0.74859059
 0.71265418 0.67554899 0.63751859 0.59880657 0.55965651 0.52031198
 0.48101657 0.44201384 0.40354738 0.36586078 0.3291976  0.29380143
 0.25991584 0.22778441 0.19765073 0.16975837 0.14435091 0.12167192]
yloc =  [0.10196492 0.08536457 0.07168059 0.06066231 0.05205903 0.0456201
 0.04109482 0.03823251 0.03678251 0.03649412 0.03711668 0.0383995
 0.04009191 0.04194321 0.04370275 0.04511983 0.04594379 0.04592393
 0.04480958 0.04235007]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 101
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 102
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
xint [-4.75528258e+00 -4.75528258e+00 -2.93892626e+00  3.06161700e-16
  2.93892626e+00  4.75528258e+00]
B vector [ 0.          0.01818641  0.27114227 -0.60990735  0.          0.        ]
hvec [1.77635684e-15 1.81635632e+00 2.93892626e+00 2.93892626e+00
 0.00000000e+00 0.00000000e+00]
A matrix:  [[1.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00
  0.00000000e+00 0.00000000e+00]
 [2.96059473e-16 6.05452107e-01 3.02726053e-01 0.00000000e+00
  0.00000000e+00 0.00000000e+00]
 [0.00000000e+00 3.02726053e-01 1.58509419e+00 4.89821044e-01
  0.00000000e+00 0.00000000e+00]
 [0.00000000e+00 0.00000000e+00 4.89821044e-01 1.95928417e+00
  4.89821044e-01 0.00000000e+00]
 [0.00000000e+00 0.00000000e+00 0.00000000e+00 4.89821044e-01
  9.79642087e-01 0.00000000e+00]
 [0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00
  0.00000000e+00 1.00000000e+00]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 91
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 92
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.         -0.13857962  0.33723471 -0.45211381  0.22605691  0.        ]
yloc =  [0.04235007]
yloc =  [0.04324692 0.04311566 0.04218163 0.04067018 0.03880666 0.03681642
 0.03492482 0.03335719 0.03233888 0.03209525 0.03285165 0.03483342
 0.03826591 0.04337448 0.05038446 0.05952122 0.07101009 0.08507643
 0.10194558]
yloc =  [0.12178713 0.14447059 0.16976499 0.19743928 0.22726241 0.25900334
 0.29243102 0.3273144  0.36342244 0.40052409 0.43838831 0.47678405
 0.51548025 0.55424589 0.59284991 0.63106125 0.66864889 0.70538177
 0.74102884 0.77535906 0.80814138 0.83914476 0.86813814 0.89489049
 0.91917076 0.94074789 0.95939085 0.97486859 0.98695006 0.99540421
 1.        ]
yloc =  [1.00057798 0.99726505 0.99025972 0.97976049 0.96596588 0.94907437
 0.92928449 0.90679472 0.88180358 0.85450956 0.82511118 0.79380694
 0.76079533 0.72627487 0.69044406 0.6535014  0.6156454  0.57707455
 0.53798738 0.49858237 0.45905803 0.41961287 0.38044539 0.3417541
 0.30373749 0.26659408 0.23052237 0.19572085 0.16238804 0.13072244]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 102
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf inf
 inf nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [ 4.75528258e+00  4.75528258e+00  2.93892626e+00  3.06161700e-16
 -2.93892626e+00 -4.75528258e+00]
h vec [1.81635632 2.93892626 2.93892626 1.81635632 0.        ]
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 82
    b[-1] = ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.05086888  0.27114227 -0.60990735  0.27114227  0.                 nan]
A matrix:  [[0.60545211 0.30272605 0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 31, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 98, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]
h vec [1.81635632 2.93892626 2.93892626 1.81635632 0.        ]
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 82
    b[-1] = ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.05086888  0.27114227 -0.60990735  0.27114227  0.                 nan]
A matrix:  [[0.60545211 0.30272605 0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 31, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 98, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]
hvec [1.81635632 2.93892626 2.93892626 1.81635632 0.        ]
h vec [1.81635632 2.93892626 2.93892626 1.81635632 0.        ]
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 82
    b[-1] = ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.05086888  0.27114227 -0.60990735  0.27114227  0.                 nan]
A matrix:  [[0.60545211 0.30272605 0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 31, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 98, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 31, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
NameError: name 'yint' is not defined. Did you mean: 'Nint'?

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
hvec [2. 2. 2. 2. 0.]
h vec [2. 2. 2. 2. 2.]
xint [-5. -3. -1.  1.  3.  5.]
B vector [ 0.04556213  0.16923077 -0.2        -0.2         0.         -0.04556213]
A matrix:  [[0.66666667 0.33333333 0.         0.         0.         0.        ]
 [0.33333333 1.33333333 0.33333333 0.         0.         0.        ]
 [0.         0.33333333 1.33333333 0.33333333 0.         0.        ]
 [0.         0.         0.33333333 1.33333333 0.33333333 0.        ]
 [0.         0.         0.         0.33333333 1.33333333 0.33333333]
 [0.         0.         0.         0.         0.33333333 0.66666667]]
M = [-0.0175901   0.17186659 -0.16218397 -0.12313072  0.05470683 -0.09569661]
nerr =  1.342895288230576

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
hvec [2. 2. 2. 2. 0.]
h vec [2. 2. 2. 2. 0.]
xint [-5. -3. -1.  1.  3.  5.]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 82
    b[-1] = ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: divide by zero encountered in scalar divide
B vector [ 0.04556213  0.16923077 -0.2        -0.2         0.                -inf]
A matrix:  [[0.66666667 0.33333333 0.         0.         0.         0.        ]
 [0.33333333 1.33333333 0.33333333 0.         0.         0.        ]
 [0.         0.33333333 1.33333333 0.33333333 0.         0.        ]
 [0.         0.         0.33333333 1.33333333 0.33333333 0.        ]
 [0.         0.         0.         0.33333333 0.66666667 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 31, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 98, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]
hvec [1.81635632 2.93892626 2.93892626 1.81635632 0.        ]
h vec [1.81635632 2.93892626 2.93892626 1.81635632 0.        ]
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 82
    b[-1] = ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: invalid value encountered in scalar divide
B vector [ 0.05086888  0.27114227 -0.60990735  0.27114227  0.                 nan]
A matrix:  [[0.60545211 0.30272605 0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         0.        ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 31, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 98, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-5. -3. -1.  1.  3.  5.]
hvec [2. 2. 2. 2. 0.]
h vec [2. 2. 2. 2. 2.]
xint [-5. -3. -1.  1.  3.  5.]
B vector [ 0.04556213  0.16923077 -0.2        -0.2         0.         -0.04556213]
A matrix:  [[0.66666667 0.33333333 0.         0.         0.         0.        ]
 [0.33333333 1.33333333 0.33333333 0.         0.         0.        ]
 [0.         0.33333333 1.33333333 0.33333333 0.         0.        ]
 [0.         0.         0.33333333 1.33333333 0.33333333 0.        ]
 [0.         0.         0.         0.33333333 1.33333333 0.33333333]
 [0.         0.         0.         0.         0.33333333 0.66666667]]
M = [-0.0175901   0.17186659 -0.16218397 -0.12313072  0.05470683 -0.09569661]
nerr =  1.342895288230576

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-5. -4. -3. -2. -1.  0.  1.  2.  3.  4.  5.]
hvec [1. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
h vec [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
xint [-5. -4. -3. -2. -1.  0.  1.  2.  3.  4.  5.]
B vector [ 0.03515489  0.02081448  0.05882353  0.2         0.2        -1.
  0.2         0.2         0.05882353  0.         -0.03515489]
A matrix:  [[0.33333333 0.16666667 0.         0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.16666667 0.66666667 0.16666667 0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.16666667 0.66666667 0.16666667 0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.16666667 0.66666667 0.16666667 0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.16666667 0.66666667 0.16666667
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.16666667 0.66666667
  0.16666667 0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.16666667
  0.66666667 0.16666667 0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.16666667 0.66666667 0.16666667 0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.16666667 0.66666667 0.16666667 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.16666667 0.66666667 0.16666667]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.16666667 0.33333333]]
M = [ 0.11231041 -0.01369148  0.06734239  0.09726311  0.74360515 -1.87168373
  0.74312978  0.09916461  0.06021179  0.01292939 -0.11192937]
nerr =  0.07442360466708572

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-5. -4. -3. -2. -1.  0.  1.  2.  3.  4.  5.]
hvec [1. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
h vec [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
xint [-5. -4. -3. -2. -1.  0.  1.  2.  3.  4.  5.]
B vector [ 0.00556909  0.02081448  0.05882353  0.2         0.2        -1.
  0.2         0.2         0.05882353  0.         -0.00556909]
A matrix:  [[0.33333333 0.16666667 0.         0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.16666667 0.66666667 0.16666667 0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.16666667 0.66666667 0.16666667 0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.16666667 0.66666667 0.16666667 0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.16666667 0.66666667 0.16666667
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.16666667 0.66666667
  0.16666667 0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.16666667
  0.66666667 0.16666667 0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.16666667 0.66666667 0.16666667 0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.16666667 0.66666667 0.16666667 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.16666667 0.66666667 0.16666667]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.16666667 0.33333333]]
M = [ 0.00982259  0.01376937  0.0599868   0.0992246   0.74311478 -1.87168373
  0.74362015  0.09720312  0.06756738 -0.01453146 -0.00944155]
nerr =  0.07173482535597515

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-5. -3. -1.  1.  3.  5.]
hvec [2. 2. 2. 2. 0.]
h vec [2. 2. 2. 2. 2.]
xint [-5. -3. -1.  1.  3.  5.]
B vector [ 0.01597633  0.16923077 -0.2        -0.2         0.         -0.01597633]
A matrix:  [[0.66666667 0.33333333 0.         0.         0.         0.        ]
 [0.33333333 1.33333333 0.33333333 0.         0.         0.        ]
 [0.         0.33333333 1.33333333 0.33333333 0.         0.        ]
 [0.         0.         0.33333333 1.33333333 0.33333333 0.        ]
 [0.         0.         0.         0.33333333 1.33333333 0.33333333]
 [0.         0.         0.         0.         0.33333333 0.66666667]]
M = [-0.06897596  0.18588092 -0.16685541 -0.11845927  0.04069251 -0.04431075]
nerr =  1.3404521024677658

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-5.         -1.66666667  1.66666667  5.        ]
hvec [3.33333333 3.33333333 0.        ]
h vec [3.33333333 3.33333333 3.33333333]
xint [-5.         -1.66666667  1.66666667  5.        ]
B vector [ 0.0530804 -0.0678733  0.        -0.0530804]
A matrix:  [[1.11111111 0.55555556 0.         0.        ]
 [0.55555556 2.22222222 0.55555556 0.        ]
 [0.         0.55555556 2.22222222 0.55555556]
 [0.         0.         0.55555556 1.11111111]]
M = [ 0.07633136 -0.057118    0.02996867 -0.0627567 ]
nerr =  2.449537516055232

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-5.  0.  5.]
hvec [0. 0.]
h vec [5. 5.]
xint [-5.  0.  5.]
B vector [ 0.17751479  0.         -0.17751479]
A matrix:  [[1.66666667 0.83333333 0.        ]
 [0.83333333 3.33333333 0.83333333]
 [0.         0.83333333 1.66666667]]
M = [ 1.06508876e-01 -1.80657593e-19 -1.06508876e-01]
nerr =  3.0687830885332854

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-3.53553391  3.53553391  3.53553391]
hvec [0. 0.]
h vec [7.07106781 0.        ]
xint [-3.53553391  3.53553391  3.53553391]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 82
    b[-1] = -ypint[-1] + (yint[-1] - yint[-2])/h[N-1]
RuntimeWarning: invalid value encountered in scalar divide
B vector [-0.03879873  0.                 nan]
A matrix:  [[2.3570226 1.1785113 0.       ]
 [1.1785113 2.3570226 0.       ]
 [0.        0.        0.       ]]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 31, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 98, in create_natural_spline
    Ainv = inv(A)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-3.53553391  3.53553391]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 27, in driver
    xeval =  np.linspace(xint[0],xint[Nint],Neval+1)
IndexError: index 2 is out of bounds for axis 0 with size 2

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py
xint [-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]
B vector [ 0.          0.27114227 -0.60990735  0.27114227  0.          0.        ]
hvec [1.81635632 2.93892626 2.93892626 1.81635632 0.         0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.        ]
 [0.30272605 1.58509419 0.48982104 0.         0.         0.        ]
 [0.         0.48982104 1.95928417 0.48982104 0.         0.        ]
 [0.         0.         0.48982104 1.58509419 0.30272605 0.        ]
 [0.         0.         0.         0.30272605 0.60545211 0.        ]
 [0.         0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 91
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 92
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.          0.31916917 -0.47929939  0.35286475 -0.17643238  0.        ]
yloc =  [0.04235007 0.03640173 0.03060456 0.0251097  0.02006833 0.0156316
 0.01195067 0.00917671 0.00746087 0.00695432 0.00780822 0.01017372
 0.01420199 0.02004418 0.02785147 0.037775   0.04996595 0.06457547
 0.08175471 0.10165486]
yloc =  [0.12438002 0.1497813  0.17762503 0.2076775  0.23970499 0.27347379
 0.30875018 0.34530045 0.38289088 0.42128775 0.46025736 0.49956597
 0.53897988 0.57826537 0.61718873 0.65551624 0.69301417 0.72944883
 0.76458649 0.79819344 0.83003595 0.85988032 0.88749283 0.91263977
 0.9350874  0.95460203 0.97094994 0.98389741 0.99321071 0.99865615
 1.        ]
yloc =  [0.99708809 0.99008446 0.97923269 0.96477634 0.94695901 0.92602427
 0.90221569 0.87577686 0.84695136 0.81598276 0.78311465 0.74859059
 0.71265418 0.67554899 0.63751859 0.59880657 0.55965651 0.52031198
 0.48101657 0.44201384 0.40354738 0.36586078 0.3291976  0.29380143
 0.25991584 0.22778441 0.19765073 0.16975837 0.14435091 0.12167192]
yloc =  [0.10196492 0.08536457 0.07168059 0.06066231 0.05205903 0.0456201
 0.04109482 0.03823251 0.03678251 0.03649412 0.03711668 0.0383995
 0.04009191 0.04194321 0.04370275 0.04511983 0.04594379 0.04592393
 0.04480958 0.04235007]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 101
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
RuntimeWarning: invalid value encountered in divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated.py", line 102
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-3.53553391  3.53553391]
hvec [0.]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 31, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 76, in create_natural_spline
    h[N-2] = xint[N] -xint[N-1]
IndexError: index 2 is out of bounds for axis 0 with size 2

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-3.53553391  3.53553391]
hvec [0.]
h vec [7.07106781]
xint [-3.53553391  3.53553391]
B vector [-0.03879873  0.03879873]
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 143, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 31, in driver
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py", line 95, in create_natural_spline
    A[N-1][N-1] = h[N-1]/3
IndexError: index 1 is out of bounds for axis 0 with size 1

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-3.53553391  3.53553391]
hvec [0.]
h vec [7.07106781]
xint [-3.53553391  3.53553391]
B vector [-0.03879873  0.03879873]
A matrix:  [[2.3570226 1.1785113]
 [1.1785113 2.3570226]]
M = [-0.03292181  0.03292181]
nerr =  4.144568217107

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-4.33012702e+00  3.06161700e-16  4.33012702e+00]
hvec [0. 0.]
h vec [4.33012702 4.33012702]
xint [-4.33012702e+00  3.06161700e-16  4.33012702e+00]
B vector [ 0.19704472  0.         -0.19704472]
A matrix:  [[1.44337567 0.72168784 0.        ]
 [0.72168784 2.88675135 0.72168784]
 [0.         0.72168784 1.44337567]]
M = [ 1.36516584e-01  9.20731824e-18 -1.36516584e-01]
nerr =  2.752746817988993

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-4.82962913 -3.53553391 -1.29409523  1.29409523  3.53553391  4.82962913]
hvec [1.29409523 2.24143868 2.58819045 2.24143868 0.        ]
h vec [1.29409523 2.24143868 2.58819045 2.24143868 1.29409523]
xint [-4.82962913 -3.53553391 -1.29409523  1.29409523  3.53553391  4.82962913]
B vector [ 0.00914911  0.10828119 -0.13375431 -0.13375431  0.         -0.00914911]
A matrix:  [[0.43136508 0.21568254 0.         0.         0.         0.        ]
 [0.21568254 1.1785113  0.37357311 0.         0.         0.        ]
 [0.         0.37357311 1.60987638 0.43136508 0.         0.        ]
 [0.         0.         0.43136508 1.60987638 0.37357311 0.        ]
 [0.         0.         0.         0.37357311 1.1785113  0.21568254]
 [0.         0.         0.         0.         0.21568254 0.43136508]]
M = [-0.04403542  0.1304902  -0.09638089 -0.06338163  0.02638743 -0.03440339]
nerr =  1.8170952333277148

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-4.82962913 -3.53553391 -1.29409523  1.29409523  3.53553391  4.82962913]
hvec [1.29409523 2.24143868 2.58819045 2.24143868 0.        ]
h vec [1.29409523 2.24143868 2.58819045 2.24143868 1.29409523]
xint [-4.82962913 -3.53553391 -1.29409523  1.29409523  3.53553391  4.82962913]
B vector [ 0.00914911  0.10828119 -0.13375431 -0.13375431  0.         -0.00914911]
A matrix:  [[0.43136508 0.21568254 0.         0.         0.         0.        ]
 [0.21568254 1.1785113  0.37357311 0.         0.         0.        ]
 [0.         0.37357311 1.60987638 0.43136508 0.         0.        ]
 [0.         0.         0.43136508 1.60987638 0.37357311 0.        ]
 [0.         0.         0.         0.37357311 1.1785113  0.21568254]
 [0.         0.         0.         0.         0.21568254 0.43136508]]
M = [-0.04403542  0.1304902  -0.09638089 -0.06338163  0.02638743 -0.03440339]
nerr =  1.8170952333277148

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-4.94910721e+00 -4.54815998e+00 -3.77874787e+00 -2.70320409e+00
 -1.40866278e+00  1.41638472e-15  1.40866278e+00  2.70320409e+00
  3.77874787e+00  4.54815998e+00  4.94910721e+00]
hvec [0.40094723 0.76941211 1.07554378 1.2945413  1.40866278 1.40866278
 1.2945413  1.07554378 0.76941211 0.        ]
h vec [0.40094723 0.76941211 1.07554378 1.2945413  1.40866278 1.40866278
 1.2945413  1.07554378 0.76941211 0.40094723]
xint [-4.94910721e+00 -4.54815998e+00 -3.77874787e+00 -2.70320409e+00
 -1.40866278e+00  1.41638472e-15  1.40866278e+00  2.70320409e+00
  3.77874787e+00  4.54815998e+00  4.94910721e+00]
B vector [ 0.00194902  0.0079526   0.02593703  0.11478774  0.30616351 -0.94403929
  0.30616351  0.11478774  0.02593703  0.         -0.00194902]
A matrix:  [[0.13364908 0.06682454 0.         0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.06682454 0.39011978 0.12823535 0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.12823535 0.6149853  0.1792573  0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.1792573  0.79002836 0.21575688 0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.21575688 0.90106803 0.23477713
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.23477713 0.93910852
  0.23477713 0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.23477713
  0.90106803 0.21575688 0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.21575688 0.79002836 0.1792573  0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.1792573  0.6149853  0.12823535 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.12823535 0.39011978 0.06682454]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.06682454 0.13364908]]
M = [ 0.01572189 -0.00227752  0.06075158 -0.06210203  0.70894583 -1.3597831
  0.70918465 -0.06309938  0.06485971 -0.02058492 -0.00429067]
nerr =  0.3042205662542034

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-4.97592363 -4.78470168 -4.40960632 -3.86505227 -3.17196642 -2.35698368
 -1.45142339 -0.4900857   0.4900857   1.45142339  2.35698368  3.17196642
  3.86505227  4.40960632  4.78470168  4.97592363]
hvec [0.19122195 0.37509536 0.54455405 0.69308585 0.81498274 0.9055603
 0.96133768 0.9801714  0.96133768 0.9055603  0.81498274 0.69308585
 0.54455405 0.37509536 0.        ]
h vec [0.19122195 0.37509536 0.54455405 0.69308585 0.81498274 0.9055603
 0.96133768 0.9801714  0.96133768 0.9055603  0.81498274 0.69308585
 0.54455405 0.37509536 0.19122195]
xint [-4.97592363 -4.78470168 -4.40960632 -3.86505227 -3.17196642 -2.35698368
 -1.45142339 -0.4900857   0.4900857   1.45142339  2.35698368  3.17196642
  3.86505227  4.40960632  4.78470168  4.97592363]
B vector [ 0.00086085  0.00296352  0.00657149  0.01452098  0.03633506  0.11075703
  0.31691614 -0.50392255 -0.50392255  0.31691614  0.11075703  0.03633506
  0.01452098  0.00657149  0.         -0.00086085]
A matrix:  
M = [ 0.00912524  0.00876068  0.01629866  0.01132071  0.07247074 -0.01032848
  0.70787217 -0.76164742 -0.7616512   0.70788358 -0.0103715   0.07263971
  0.01063597  0.01919609 -0.00445294 -0.01127911]
nerr =  0.2804699472307506

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\clamped cubic spline.py
xint [-4.98601899e+00 -4.87463956e+00 -4.65436874e+00 -4.33012702e+00
 -3.90915741e+00 -3.40086369e+00 -2.81660029e+00 -2.16941870e+00
 -1.47377587e+00 -7.45211331e-01  3.06161700e-16  7.45211331e-01
  1.47377587e+00  2.16941870e+00  2.81660029e+00  3.40086369e+00
  3.90915741e+00  4.33012702e+00  4.65436874e+00  4.87463956e+00
  4.98601899e+00]
hvec [0.11137942 0.22027082 0.32424172 0.42096961 0.50829372 0.5842634
 0.64718159 0.69564282 0.72856454 0.74521133 0.74521133 0.72856454
 0.69564282 0.64718159 0.5842634  0.50829372 0.42096961 0.32424172
 0.22027082 0.        ]
h vec [0.11137942 0.22027082 0.32424172 0.42096961 0.50829372 0.5842634
 0.64718159 0.69564282 0.72856454 0.74521133 0.74521133 0.72856454
 0.69564282 0.64718159 0.5842634  0.50829372 0.42096961 0.32424172
 0.22027082 0.11137942]
xint [-4.98601899e+00 -4.87463956e+00 -4.65436874e+00 -4.33012702e+00
 -3.90915741e+00 -3.40086369e+00 -2.81660029e+00 -2.16941870e+00
 -1.47377587e+00 -7.45211331e-01  3.06161700e-16  7.45211331e-01
  1.47377587e+00  2.16941870e+00  2.81660029e+00  3.40086369e+00
  3.90915741e+00  4.33012702e+00  4.65436874e+00  4.87463956e+00
  4.98601899e+00]
B vector [ 4.87425717e-04  1.58141075e-03  3.09264379e-03  5.55013752e-03
  1.01069875e-02  1.96576427e-02  4.24228001e-02  1.03463203e-01
  2.48500351e-01  2.93569947e-02 -9.58261686e-01  2.93569947e-02
  2.48500351e-01  1.03463203e-01  4.24228001e-02  1.96576427e-02
  1.01069875e-02  5.55013752e-03  3.09264379e-03  0.00000000e+00
 -4.87425717e-04]
A matrix:  
M = [ 0.0085111   0.00923539  0.01096226  0.01413574  0.02061473  0.03222189
  0.06342858  0.12282967  0.35916713  0.52500441 -2.19134097  0.52500425
  0.35916775  0.1228273   0.06343778  0.03218576  0.02075949  0.01354026
  0.0135115  -0.00249158 -0.011883  ]
nerr =  0.006275547793654514

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py
B vector [ 0.00000000e+00  0.00000000e+00  9.86076132e-32 -1.47911420e-31
  0.00000000e+00  0.00000000e+00]
hvec [1.25663706 1.25663706 1.25663706 1.25663706 0.         0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.        ]
 [0.20943951 0.83775804 0.20943951 0.         0.         0.        ]
 [0.         0.20943951 0.83775804 0.20943951 0.         0.        ]
 [0.         0.         0.20943951 0.83775804 0.20943951 0.        ]
 [0.         0.         0.         0.20943951 0.41887902 0.        ]
 [0.         0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 91
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 92
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.00000000e+00 -4.85378012e-32  1.94151205e-31 -2.57250346e-31
  1.28625173e-31  0.00000000e+00]
yloc =  [ 0.00000000e+00 -2.44929360e-17 -4.89858720e-17 -7.34788079e-17
 -9.79717439e-17 -1.22464680e-16 -1.46957616e-16 -1.71450552e-16
 -1.95943488e-16 -2.20436424e-16 -2.44929360e-16 -2.69422296e-16
 -2.93915232e-16 -3.18408168e-16 -3.42901104e-16 -3.67394040e-16
 -3.91886976e-16 -4.16379912e-16 -4.40872848e-16 -4.65365784e-16
 -4.89858720e-16]
yloc =  [-4.89858720e-16 -5.14351656e-16 -5.38844592e-16 -5.63337528e-16
 -5.87830464e-16 -6.12323400e-16 -6.36816336e-16 -6.61309272e-16
 -6.85802208e-16 -7.10295144e-16 -7.34788079e-16 -7.59281015e-16
 -7.83773951e-16 -8.08266887e-16 -8.32759823e-16 -8.57252759e-16
 -8.81745695e-16 -9.06238631e-16 -9.30731567e-16 -9.55224503e-16
 -9.79717439e-16]
yloc =  [-9.79717439e-16 -1.00421038e-15 -1.02870331e-15 -1.05319625e-15
 -1.07768918e-15 -1.10218212e-15 -1.12667506e-15 -1.15116799e-15
 -1.17566093e-15 -1.20015386e-15 -1.22464680e-15 -1.24913974e-15
 -1.27363267e-15 -1.29812561e-15 -1.32261854e-15 -1.34711148e-15
 -1.37160442e-15 -1.39609735e-15 -1.42059029e-15 -1.44508322e-15]
yloc =  [-1.46957616e-15 -1.49406909e-15 -1.51856203e-15 -1.54305497e-15
 -1.56754790e-15 -1.59204084e-15 -1.61653377e-15 -1.64102671e-15
 -1.66551965e-15 -1.69001258e-15 -1.71450552e-15 -1.73899845e-15
 -1.76349139e-15 -1.78798433e-15 -1.81247726e-15 -1.83697020e-15
 -1.86146313e-15 -1.88595607e-15 -1.91044901e-15 -1.93494194e-15
 -1.95943488e-15]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 102
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [ nan -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf -inf
 -inf -inf -inf -inf -inf -inf  nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py
B vector [ 0.00000000e+00  0.00000000e+00  9.86076132e-32 -1.47911420e-31
  0.00000000e+00  2.95822839e-31 -2.95822839e-31  0.00000000e+00
  0.00000000e+00  0.00000000e+00  0.00000000e+00]
hvec [0.62831853 0.62831853 0.62831853 0.62831853 0.62831853 0.62831853
 0.62831853 0.62831853 0.62831853 0.         0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.10471976 0.41887902 0.10471976 0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.10471976 0.41887902 0.10471976 0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.10471976 0.41887902 0.10471976 0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.10471976 0.41887902 0.10471976
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.10471976 0.41887902
  0.10471976 0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.10471976
  0.41887902 0.10471976 0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.10471976 0.41887902 0.10471976 0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.10471976 0.41887902 0.10471976 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.10471976 0.20943951 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 91
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 92
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.00000000e+00 -8.98310111e-32  3.59324044e-31 -4.05831823e-31
 -1.48446768e-31  9.99618896e-31 -1.02512878e-30  2.75996211e-31
 -7.88560603e-32  3.94280302e-32  0.00000000e+00]
yloc =  [ 0.00000000e+00 -2.44929360e-17 -4.89858720e-17 -7.34788079e-17
 -9.79717439e-17 -1.22464680e-16 -1.46957616e-16 -1.71450552e-16
 -1.95943488e-16 -2.20436424e-16 -2.44929360e-16]
yloc =  [-2.44929360e-16 -2.69422296e-16 -2.93915232e-16 -3.18408168e-16
 -3.42901104e-16 -3.67394040e-16 -3.91886976e-16 -4.16379912e-16
 -4.40872848e-16 -4.65365784e-16 -4.89858720e-16]
yloc =  [-4.89858720e-16 -5.14351656e-16 -5.38844592e-16 -5.63337528e-16
 -5.87830464e-16 -6.12323400e-16 -6.36816336e-16 -6.61309272e-16
 -6.85802208e-16 -7.10295144e-16]
yloc =  [-7.34788079e-16 -7.59281015e-16 -7.83773951e-16 -8.08266887e-16
 -8.32759823e-16 -8.57252759e-16 -8.81745695e-16 -9.06238631e-16
 -9.30731567e-16 -9.55224503e-16 -9.79717439e-16]
yloc =  [-9.79717439e-16 -1.00421038e-15 -1.02870331e-15 -1.05319625e-15
 -1.07768918e-15 -1.10218212e-15 -1.12667506e-15 -1.15116799e-15
 -1.17566093e-15 -1.20015386e-15]
yloc =  [-1.22464680e-15 -1.24913974e-15 -1.27363267e-15 -1.29812561e-15
 -1.32261854e-15 -1.34711148e-15 -1.37160442e-15 -1.39609735e-15
 -1.42059029e-15 -1.44508322e-15]
yloc =  [-1.46957616e-15 -1.49406909e-15 -1.51856203e-15 -1.54305497e-15
 -1.56754790e-15 -1.59204084e-15 -1.61653377e-15 -1.64102671e-15
 -1.66551965e-15 -1.69001258e-15 -1.71450552e-15]
yloc =  [-1.71450552e-15 -1.73899845e-15 -1.76349139e-15 -1.78798433e-15
 -1.81247726e-15 -1.83697020e-15 -1.86146313e-15 -1.88595607e-15
 -1.91044901e-15 -1.93494194e-15 -1.95943488e-15]
yloc =  [-1.95943488e-15 -1.98392781e-15 -2.00842075e-15 -2.03291369e-15
 -2.05740662e-15 -2.08189956e-15 -2.10639249e-15 -2.13088543e-15
 -2.15537837e-15 -2.17987130e-15]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 102
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [-inf -inf -inf -inf -inf -inf -inf -inf -inf -inf  nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py
B vector [ 0.00000000e+00  0.00000000e+00  9.86076132e-32 -1.47911420e-31
  0.00000000e+00  2.95822839e-31 -2.95822839e-31  0.00000000e+00
  0.00000000e+00  0.00000000e+00  0.00000000e+00]
hvec [0.62831853 0.62831853 0.62831853 0.62831853 0.62831853 0.62831853
 0.62831853 0.62831853 0.62831853 0.         0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.10471976 0.41887902 0.10471976 0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.10471976 0.41887902 0.10471976 0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.10471976 0.41887902 0.10471976 0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.10471976 0.41887902 0.10471976
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.10471976 0.41887902
  0.10471976 0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.10471976
  0.41887902 0.10471976 0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.10471976 0.41887902 0.10471976 0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.10471976 0.41887902 0.10471976 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.10471976 0.20943951 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 91
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 92
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.00000000e+00 -8.98310111e-32  3.59324044e-31 -4.05831823e-31
 -1.48446768e-31  9.99618896e-31 -1.02512878e-30  2.75996211e-31
 -7.88560603e-32  3.94280302e-32  0.00000000e+00]
yloc =  [ 0.00000000e+00 -2.44929360e-17 -4.89858720e-17 -7.34788079e-17
 -9.79717439e-17 -1.22464680e-16 -1.46957616e-16 -1.71450552e-16
 -1.95943488e-16 -2.20436424e-16 -2.44929360e-16]
yloc =  [-2.44929360e-16 -2.69422296e-16 -2.93915232e-16 -3.18408168e-16
 -3.42901104e-16 -3.67394040e-16 -3.91886976e-16 -4.16379912e-16
 -4.40872848e-16 -4.65365784e-16 -4.89858720e-16]
yloc =  [-4.89858720e-16 -5.14351656e-16 -5.38844592e-16 -5.63337528e-16
 -5.87830464e-16 -6.12323400e-16 -6.36816336e-16 -6.61309272e-16
 -6.85802208e-16 -7.10295144e-16]
yloc =  [-7.34788079e-16 -7.59281015e-16 -7.83773951e-16 -8.08266887e-16
 -8.32759823e-16 -8.57252759e-16 -8.81745695e-16 -9.06238631e-16
 -9.30731567e-16 -9.55224503e-16 -9.79717439e-16]
yloc =  [-9.79717439e-16 -1.00421038e-15 -1.02870331e-15 -1.05319625e-15
 -1.07768918e-15 -1.10218212e-15 -1.12667506e-15 -1.15116799e-15
 -1.17566093e-15 -1.20015386e-15]
yloc =  [-1.22464680e-15 -1.24913974e-15 -1.27363267e-15 -1.29812561e-15
 -1.32261854e-15 -1.34711148e-15 -1.37160442e-15 -1.39609735e-15
 -1.42059029e-15 -1.44508322e-15]
yloc =  [-1.46957616e-15 -1.49406909e-15 -1.51856203e-15 -1.54305497e-15
 -1.56754790e-15 -1.59204084e-15 -1.61653377e-15 -1.64102671e-15
 -1.66551965e-15 -1.69001258e-15 -1.71450552e-15]
yloc =  [-1.71450552e-15 -1.73899845e-15 -1.76349139e-15 -1.78798433e-15
 -1.81247726e-15 -1.83697020e-15 -1.86146313e-15 -1.88595607e-15
 -1.91044901e-15 -1.93494194e-15 -1.95943488e-15]
yloc =  [-1.95943488e-15 -1.98392781e-15 -2.00842075e-15 -2.03291369e-15
 -2.05740662e-15 -2.08189956e-15 -2.10639249e-15 -2.13088543e-15
 -2.15537837e-15 -2.17987130e-15]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 102
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
yloc =  [-inf -inf -inf -inf -inf -inf -inf -inf -inf -inf  nan]
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py
yint [ 0.00000000e+00 -2.44929360e-16 -4.89858720e-16 -7.34788079e-16
 -9.79717439e-16 -1.22464680e-15 -1.46957616e-15 -1.71450552e-15
 -1.95943488e-15 -2.20436424e-15 -2.44929360e-15]
B vector [ 0.00000000e+00  0.00000000e+00  9.86076132e-32 -1.47911420e-31
  0.00000000e+00  2.95822839e-31 -2.95822839e-31  0.00000000e+00
  0.00000000e+00  0.00000000e+00  0.00000000e+00]
hvec [0.62831853 0.62831853 0.62831853 0.62831853 0.62831853 0.62831853
 0.62831853 0.62831853 0.62831853 0.         0.        ]
A matrix:  [[1.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.10471976 0.41887902 0.10471976 0.         0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.10471976 0.41887902 0.10471976 0.         0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.10471976 0.41887902 0.10471976 0.
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.10471976 0.41887902 0.10471976
  0.         0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.10471976 0.41887902
  0.10471976 0.         0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.10471976
  0.41887902 0.10471976 0.         0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.10471976 0.41887902 0.10471976 0.         0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.10471976 0.41887902 0.10471976 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.10471976 0.20943951 0.        ]
 [0.         0.         0.         0.         0.         0.
  0.         0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 92
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 93
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.00000000e+00 -8.98310111e-32  3.59324044e-31 -4.05831823e-31
 -1.48446768e-31  9.99618896e-31 -1.02512878e-30  2.75996211e-31
 -7.88560603e-32  3.94280302e-32  0.00000000e+00]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 103
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py
yint [ 0.00000000e+00  8.66025404e-01 -8.66025404e-01 -2.44929360e-15]
B vector [ 0.         -1.24049001  0.          0.        ]
hvec [2.0943951 2.0943951 0.        0.       ]
A matrix:  [[1.         0.         0.         0.        ]
 [0.34906585 1.3962634  0.34906585 0.        ]
 [0.         0.34906585 0.6981317  0.        ]
 [0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 92
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 93
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.         -1.01535489  0.50767745  0.        ]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 103
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py
xint [0.         2.0943951  4.1887902  6.28318531]
yint [ 0.00000000e+00  8.66025404e-01 -8.66025404e-01 -2.44929360e-15]
B vector [ 0.         -1.24049001  0.          0.        ]
hvec [2.0943951 2.0943951 0.        0.       ]
A matrix:  [[1.         0.         0.         0.        ]
 [0.34906585 1.3962634  0.34906585 0.        ]
 [0.         0.34906585 0.6981317  0.        ]
 [0.         0.         0.         1.        ]]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 92
    C[j] = yint[j]/h[j]-h[j]*M[j]/6
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 93
    D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
RuntimeWarning: divide by zero encountered in scalar divide
M = [ 0.         -1.01535489  0.50767745  0.        ]

Warning (from warnings module):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\cubic spline updated - Naturally Periodic.py", line 103
    + C*(xip-xeval) + D*(xeval-xi)
RuntimeWarning: invalid value encountered in multiply
nerr =  nan

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\hermite_int.py
[-9.51056516e-01 -5.87785252e-01  6.12323400e-17  5.87785252e-01
  9.51056516e-01]

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\hermite_int.py
[-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00]

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\hermite_int.py
[-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\hermite_int.py
[-4.98458667 -4.8618496  -4.61939766 -4.26320082 -3.80202983 -3.24724024
 -2.61249282 -1.91341716 -1.16722682 -0.39229548  0.39229548  1.16722682
  1.91341716  2.61249282  3.24724024  3.80202983  4.26320082  4.61939766
  4.8618496   4.98458667  4.98458667]

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\hermite_int.py
[-4.75528258e+00 -2.93892626e+00  3.06161700e-16  2.93892626e+00
  4.75528258e+00  4.75528258e+00]

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\hermite_int.py
[-4.82962913 -3.53553391 -1.29409523  1.29409523  3.53553391  4.82962913
  4.82962913]

======= RESTART: C:\Users\cambr\Downloads\hermite_int.py ======

Warning (from warnings module):
  File "C:\Users\cambr\Downloads\hermite_int.py", line 104
    lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\Downloads\hermite_int.py", line 67
    lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])
RuntimeWarning: divide by zero encountered in scalar divide

Warning (from warnings module):
  File "C:\Users\cambr\Downloads\hermite_int.py", line 76
    lpj[count] = lpj[count]+ 1./(xint[count] - xint[jj])
RuntimeWarning: divide by zero encountered in scalar divide
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\hermite_int.py
[-4.82962913 -3.53553391 -1.29409523  1.29409523  3.53553391  4.82962913
  4.82962913]
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\hermite_int.py
[-4.94910721e+00 -4.54815998e+00 -3.77874787e+00 -2.70320409e+00
 -1.40866278e+00  1.41638472e-15  1.40866278e+00  2.70320409e+00
  3.77874787e+00  4.54815998e+00  4.94910721e+00  4.94910721e+00]
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\hermite_int.py
[-4.97592363 -4.78470168 -4.40960632 -3.86505227 -3.17196642 -2.35698368
 -1.45142339 -0.4900857   0.4900857   1.45142339  2.35698368  3.17196642
  3.86505227  4.40960632  4.78470168  4.97592363  4.97592363]
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 8\hermite_int.py
[-4.98601899e+00 -4.87463956e+00 -4.65436874e+00 -4.33012702e+00
 -3.90915741e+00 -3.40086369e+00 -2.81660029e+00 -2.16941870e+00
 -1.47377587e+00 -7.45211331e-01  3.06161700e-16  7.45211331e-01
  1.47377587e+00  2.16941870e+00  2.81660029e+00  3.40086369e+00
  3.90915741e+00  4.33012702e+00  4.65436874e+00  4.87463956e+00
  4.98601899e+00  4.98601899e+00]
