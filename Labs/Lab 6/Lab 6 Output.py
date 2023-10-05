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
>>> 
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
>>> # Slacker Newton ended up taking more time than normal Newton with the same number of iterations. My classmates Slacker code took longer than mine did and they had 23 iterations while mine had 7.
