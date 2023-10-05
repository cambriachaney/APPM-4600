Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0006590461730957031
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0007811546325683594
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0007833480834960937
Broyden: number of iterations is: 4
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 199, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 43, in driver
    [xstar,ier,its] = SlackerNewton(x0, tol,Nmax)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 120, in SlackerNewton
    if abs(iterates[-1] - iterates[-2]) < 10**(-2):
IndexError: list index out of range

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0007776403427124023
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0003955602645874023
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0003887772560119629
Broyden: number of iterations is: 4
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 199, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 43, in driver
    [xstar,ier,its] = SlackerNewton(x0, tol,Nmax)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 120, in SlackerNewton
    if abs(iterates[its] - iterates[its - 1]) < 10**(-2):
UnboundLocalError: cannot access local variable 'its' where it is not associated with a value

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0006453132629394531
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.00035245418548583983
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0007833600044250488
Broyden: number of iterations is: 4
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 201, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 43, in driver
    [xstar,ier,its] = SlackerNewton(x0, tol,Nmax)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 121, in SlackerNewton
    if abs(iterates[count] - iterates[count - 1]) > 0.5:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0008698463439941406
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0007259130477905273
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.001071619987487793
Broyden: number of iterations is: 4
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 201, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 43, in driver
    [xstar,ier,its] = SlackerNewton(x0, tol,Nmax)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 121, in SlackerNewton
    if abs(iterates[count] - iterates[count - 1]) > np.array([0.5, 0.5]):
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0005747413635253906
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0004155397415161133
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0001536250114440918
Broyden: number of iterations is: 4
[1 0]
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 202, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 43, in driver
    [xstar,ier,its] = SlackerNewton(x0, tol,Nmax)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 122, in SlackerNewton
    if abs(iterates[count] - iterates[count - 1]) > np.array([0.5, 0.5]):
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0005012226104736329
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0004457235336303711
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0008715152740478516
Broyden: number of iterations is: 4
[ 0 -1]
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 202, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 43, in driver
    [xstar,ier,its] = SlackerNewton(x0, tol,Nmax)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 122, in SlackerNewton
    if abs(iterates[count] - iterates[count - 1]) > np.array([0.5, 0.5]):
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0005878782272338867
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0008261322975158692
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0010664701461791993
Broyden: number of iterations is: 4
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 201, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 43, in driver
    [xstar,ier,its] = SlackerNewton(x0, tol,Nmax)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 121, in SlackerNewton
    if abs(iterates[count] - iterates[count - 1]) > [0.5,0.5]:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.001245427131652832
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0004930615425109864
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0009455084800720215
Broyden: number of iterations is: 4
[1 0]
[ 0 -1]
[False False]
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 205, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 43, in driver
    [xstar,ier,its] = SlackerNewton(x0, tol,Nmax)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 125, in SlackerNewton
    if abs(iterates[count] - iterates[count - 1]) > [0.5,0.5]:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0008025360107421875
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0009101152420043946
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.00104600191116333
Broyden: number of iterations is: 4
[1 0]
[ 0 -1]
[False  True]
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 205, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 43, in driver
    [xstar,ier,its] = SlackerNewton(x0, tol,Nmax)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 125, in SlackerNewton
    if abs(iterates[count] - iterates[count - 1]) > [0.5,0.5]:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0011895656585693359
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0008827686309814453
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0006638050079345703
Broyden: number of iterations is: 4
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[1 0]
[ 0 -1]
[False  True]
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.05302574634552002
Slacker: number of iterations is: 7

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00047116756439208985
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0004505157470703125
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0006743311882019043
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.000477445125579834
Slacker: number of iterations is: 7
# Slacker Newton ended up taking more time than normal Newton with the same number of iterations. My classmates Slacker code took longer than mine did and they had 23 iterations while mine had 7.

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0008795642852783203
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0006898880004882812
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0010047674179077149
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.00010925531387329102
Slacker: number of iterations is: 7
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 257, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 54, in driver
    [xstar,ier,its] = NewtonFinite(x0, tol,Nmax,h)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 112, in NewtonFinite
    Jinv = inv(J)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0013405799865722657
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0006520986557006836
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.001044297218322754
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0010428547859191895
Slacker: number of iterations is: 7
[[8.04       1.54450062]
 [0.46391402 0.        ]]
[[5.30623454 1.43066012]
 [0.56033647 0.        ]]
[[-4.23433880e+01  3.65595182e-02]
 [ 1.96607133e+00  0.00000000e+00]]
[[-114.29040432    1.79647967]
 [   0.19751367    0.        ]]
[[1.13920000e+06 1.35995150e+00]
 [6.30742311e-01 0.00000000e+00]]
[[0. 0.]
 [0. 0.]]
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 259, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 54, in driver
    [xstar,ier,its] = NewtonFinite(x0, tol,Nmax,h)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 114, in NewtonFinite
    Jinv = inv(J)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0006278085708618164
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0007021427154541016
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0009380936622619629
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0007859706878662109
Slacker: number of iterations is: 7
[[8.04       1.54450062]
 [0.46391402 0.        ]]
0
[[5.30623454 1.43066012]
 [0.56033647 0.        ]]
1
[[-4.23433880e+01  3.65595182e-02]
 [ 1.96607133e+00  0.00000000e+00]]
2
[[-114.29040432    1.79647967]
 [   0.19751367    0.        ]]
3
[[1.13920000e+06 1.35995150e+00]
 [6.30742311e-01 0.00000000e+00]]
4
[[0. 0.]
 [0. 0.]]
5
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 260, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 54, in driver
    [xstar,ier,its] = NewtonFinite(x0, tol,Nmax,h)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 115, in NewtonFinite
    Jinv = inv(J)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0012286376953125
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.00010664463043212891
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0007257223129272461
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0008516788482666015
Slacker: number of iterations is: 7
[[8.08       1.54868072]
 [0.46814814 0.        ]]
0
[[5.37095984 1.43982953]
 [0.54229838 0.        ]]
1
[[-43.63163958   0.64750333]
 [  1.37114083   0.        ]]
2
[[-146.40583682    1.74113071]
 [   0.27244334    0.        ]]
3
[[5.65049316e+04 2.73591664e-01]
 [1.74000693e+00 0.00000000e+00]]
4
[[0.         1.85546875]
 [0.04882812 0.        ]]
5
[[0. 0.]
 [0. 0.]]
6
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 263, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 54, in driver
    [xstar,ier,its, iterations] = NewtonFinite(x0, tol,Nmax,h)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 116, in NewtonFinite
    Jinv = inv(J)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0006309986114501953
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0003968358039855957
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0006232619285583496
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0006865262985229492
Slacker: number of iterations is: 7
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 263, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 54, in driver
    [xstar,ier,its, iterations] = NewtonFinite(x0, tol,Nmax,h)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 116, in NewtonFinite
    Jinv = inv(J)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 561, in inv
    ainv = _umath_linalg.inv(a, signature=signature, extobj=extobj)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\linalg\linalg.py", line 112, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0014103937149047851
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0006807923316955566
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0006458878517150879
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0004638791084289551
Slacker: number of iterations is: 7
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
0
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
1
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
2
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
3
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
4
[[0. 0.]
 [0. 0.]]
5
[ 1.69045622e+10 -7.08267520e+17]
Slacker: the error message reads: 1
Slacker: took this many seconds: 0.24066145420074464
Slacker: number of iterations is: 5

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00021829605102539063
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.00011907815933227539
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0
Slacker: number of iterations is: 7
[ 1.69045622e+10 -7.08267520e+17]
Slacker: the error message reads: 1
Slacker: took this many seconds: 0.00023434162139892578
Slacker: number of iterations is: 5

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0003394937515258789
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0006753087043762207
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0005030274391174316
Slacker: number of iterations is: 7
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
1.0001
0
1.0001
0
0.6552766324646763
1.7909792823634936
0.6552766324646763
1.7909792823634936
-5.140296230763102
22.51387220749153
-5.140296230763102
22.51387220749153
-15.039100846529148
-5434.062588019854
-15.039100846529148
-5434.062588019854
2744.0548361253605
-1168807450.1272068
2744.0548361253605
-1168807450.1272068
16904562234.954123
-7.082675197942191e+17
16904562234.954123
-7.082675197942191e+17
[ 1.69045622e+10 -7.08267520e+17]
Slacker: the error message reads: 1
Slacker: took this many seconds: 0.13502484560012817
Slacker: number of iterations is: 5

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00029644966125488283
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.00021992921829223634
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0002525925636291504
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0004001975059509277
Slacker: number of iterations is: 7
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[8.0004     0.45973977]
[8.0004     0.45973977]
[5.24181306 0.57854999]
[5.24181306 0.57854999]
[-41.12276985   1.81381137]
[-41.12276985   1.81381137]
[-120.31324208    1.97504108]
[-120.31324208    1.97504108]
[0.         0.06914139]
[0.         0.06914139]
[0. 0.]
[0. 0.]
[ 1.69045622e+10 -7.08267520e+17]
Finite Difference Newton: the error message reads: 1
Finite Difference Newton: took this many seconds: 0.09496588706970215
Finite Difference Newton: number of iterations is: 5

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00026611804962158205
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 6.188154220581055e-05
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.00016205310821533204
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.00019087791442871094
Slacker: number of iterations is: 7
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
Return: [8.0004     0.45973977]
Return: [8.0004     0.45973977]
Return: [5.24181306 0.57854999]
Return: [5.24181306 0.57854999]
Return: [-41.12276985   1.81381137]
Return: [-41.12276985   1.81381137]
Return: [-120.31324208    1.97504108]
Return: [-120.31324208    1.97504108]
Return: [0.         0.06914139]
Return: [0.         0.06914139]
Return: [0. 0.]
Return: [0. 0.]
[ 1.69045622e+10 -7.08267520e+17]
Finite Difference Newton: the error message reads: 1
Finite Difference Newton: took this many seconds: 0.1000599980354309
Finite Difference Newton: number of iterations is: 5

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 7.211685180664063e-05
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.000515890121459961
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0001435399055480957
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0
Slacker: number of iterations is: 7
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[[8.0004     1.54034438]
 [0.45973977 0.        ]]
[[5.24181306 1.42135932]
 [0.57854999 0.        ]]
[[-41.12276985   0.18613052]
 [  1.81381137   0.        ]]
[[-1.20313242e+02  2.49811183e-02]
 [ 1.97504108e+00  0.00000000e+00]]
[[0.         1.9288063 ]
 [0.06914139 0.        ]]
[[0. 0.]
 [0. 0.]]
[ 1.69045622e+10 -7.08267520e+17]
Finite Difference Newton: the error message reads: 1
Finite Difference Newton: took this many seconds: 0.06522926092147827
Finite Difference Newton: number of iterations is: 5

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00023543834686279297
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 8.05974006652832e-05
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0003418922424316406
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.00025475025177001953
Slacker: number of iterations is: 7
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[9.99999994e-05 1.54034438e+00]
[9.99999994e-05 1.54034438e+00]
[3.58205856 1.42135932]
[3.58205856 1.42135932]
[45.02784441  0.18613052]
[45.02784441  0.18613052]
[-1.08681251e+04  2.49811183e-02]
[-1.08681251e+04  2.49811183e-02]
[-2.3347200e+09  1.9288063e+00]
[-2.3347200e+09  1.9288063e+00]
[0. 0.]
[0. 0.]
[ 1.69045622e+10 -7.08267520e+17]
Finite Difference Newton: the error message reads: 1
Finite Difference Newton: took this many seconds: 0.1009405255317688
Finite Difference Newton: number of iterations is: 5

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00032065391540527345
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 7.520914077758789e-05
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0
Slacker: number of iterations is: 7
[ 0.99860694 -0.10553049]
Finite Difference Newton: the error message reads: 0
Finite Difference Newton: took this many seconds: 0.0006755232810974121
Finite Difference Newton: number of iterations is: 3

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0002716445922851562
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0008358001708984375
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.00024216175079345704
Slacker: number of iterations is: 7
[ 0.99860694 -0.10553049]
Finite Difference Newton: the error message reads: 0
Finite Difference Newton: took this many seconds: 0.0008117556571960449
Finite Difference Newton: number of iterations is: 3

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0002460432052612305
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 2.5272369384765625e-05
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.00012600421905517578
Slacker: number of iterations is: 7
[ 0.99860694 -0.10553049]
Finite Difference Newton: the error message reads: 0
Finite Difference Newton: took this many seconds: 0.00047795772552490235
Finite Difference Newton: number of iterations is: 3
# h = 0.0001

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00033856868743896483
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0003597855567932129
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.00027797222137451174
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.0004842042922973633
Slacker: number of iterations is: 7
[ 0.99860694 -0.10553049]
Finite Difference Newton: the error message reads: 0
Finite Difference Newton: took this many seconds: 0.0007490277290344238
Finite Difference Newton: number of iterations is: 3

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00028656959533691407
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0003766655921936035
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 9.413957595825196e-05
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.00019453763961791993
Slacker: number of iterations is: 7
[ 0.99860694 -0.10553049]
Finite Difference Newton: the error message reads: 0
Finite Difference Newton: took this many seconds: 0.0006310224533081054
Finite Difference Newton: number of iterations is: 5
# h = 0.0000000000001

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0004034757614135742
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0005541324615478515
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0002976298332214355
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.00048601627349853516
Slacker: number of iterations is: 7
[ 0.99860694 -0.10553049]
Finite Difference Newton: the error message reads: 0
Finite Difference Newton: took this many seconds: 0.0011293530464172364
Finite Difference Newton: number of iterations is: 4
# h = 10^-3 * x0

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00025030136108398436
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.0
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.00018446445465087892
Slacker: number of iterations is: 7
Traceback (most recent call last):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 263, in <module>
    driver()
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 54, in driver
    [xstar,ier,its, iterations] = NewtonFinite(x0, tol,Nmax,h)
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 111, in NewtonFinite
    J[0,0] = forward_difference_xvar(x0[0], h, x0[1])[0]
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 136, in forward_difference_xvar
    x0 = np.array([s+h, y])
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (2,) + inhomogeneous part.

========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.0003507900238037109
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.00048127174377441404
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.00038734674453735354
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.00023708343505859374
Slacker: number of iterations is: 7

Warning (from warnings module):
  File "C:\Users\cambr\Downloads\newtonNONLinear2.py", line 149
    return (evalF(x0) - evalF(x1))/h
RuntimeWarning: invalid value encountered in divide
[nan nan]
Finite Difference Newton: the error message reads: 1
Finite Difference Newton: took this many seconds: 0.00834949016571045
Finite Difference Newton: number of iterations is: 99
>>> # The choice of h affects the number of iterations needed and how fast the algorithm runs. Smaller h means less iterations and quicker speed.
>>> 
========= RESTART: C:\Users\cambr\Downloads\newtonNONLinear2.py =========
[ 0.99860694 -0.10553049]
Newton: the error message reads: 0
Newton: took this many seconds: 0.00040194034576416013
Netwon: number of iterations is: 3
[ 0.99860694 -0.10553049]
Lazy Newton: the error message reads: 0
Lazy Newton: took this many seconds: 0.0
Lazy Newton: number of iterations is: 7
[ 0.99860694 -0.10553049]
Broyden: the error message reads: 0
Broyden: took this many seconds: 0.00044509172439575193
Broyden: number of iterations is: 4
[ 0.99860694 -0.10553049]
Slacker: the error message reads: 0
Slacker: took this many seconds: 0.00021857023239135742
Slacker: number of iterations is: 7
[ 0.99860694 -0.10553049]
Finite Difference Newton: the error message reads: 0
Finite Difference Newton: took this many seconds: 0.0009120225906372071
Finite Difference Newton: number of iterations is: 7
