Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import numpy.linalg as la
import math
def driver():
    n = 100
    x = np.linspace(0,np.pi, n)

    
def driver():
    n = 100
    x = np.linspace(0,np.pi, n)

    
def driver():
    n = 100
    x = np.linspace(0,np.pi, n)
    f = lambda x: sin(n*np.pi*x)
    g = lambda x: cos(n*np.pi*x)
    y = f(x)
    w = g(x)
    dp = dotProduct(y,w,n)
    print('the dot product is: ', dp)
    return

def dotProduct(x,y,n):
    dp = 0
    for j in range(n):
        dp = dp+x[j]*y[j]
    return dp

driver()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    driver()
  File "<pyshell#18>", line 6, in driver
    y = f(x)
  File "<pyshell#18>", line 4, in <lambda>
    f = lambda x: sin(n*np.pi*x)
NameError: name 'sin' is not defined. Did you mean: 'bin'?
def driver():
    n = 100
    x = np.linspace(0,np.pi, n)
    f = lambda x: np.sin(n*np.pi*x)
    g = lambda x: np.cos(n*np.pi*x)
    y = f(x)
    w = g(x)
    dp = dotProduct(y,w,n)
    print('the dot product is: ', dp)
    return

driver()
the dot product is:  0.4004752194790446
def driver():
    n = 1000
    x = np.linspace(0,np.pi, n)
    f = lambda x: np.sin(n*np.pi*x)
    g = lambda x: np.cos(n*np.pi*x)
    y = f(x)
    w = g(x)
    dp = dotProduct(y,w,n)
    print('the dot product is: ', dp)
    return

driver()
the dot product is:  0.8010684645036469
def driver():
    n = 1000
    x = np.linspace(0,np.pi, n)
    f = lambda x: np.sin(np.pi*x)
    g = lambda x: np.cos(np.pi*x)
    y = f(x)
    w = g(x)
    dp = dotProduct(y,w,n)
    print('the dot product is: ', dp)
    return

driver()
the dot product is:  9.564799631325759
def driver():
    n = 1000
    x = np.linspace(0,np.pi, n)
    f = lambda x: np.sin(n*x)
    g = lambda x: np.cos(n*x)
    y = f(x)
    w = g(x)
    dp = dotProduct(y,w,n)
    print('the dot product is: ', dp)
    return

driver()
the dot product is:  -3.241219471883492e-13
def driver():
    n = 100
    x = np.linspace(0,np.pi, n)
    f = lambda x: np.sin(n*x)
    g = lambda x: np.cos(n*x)
    y = f(x)
    w = g(x)
    dp = dotProduct(y,w,n)
    print('the dot product is: ', dp)
    return

driver()
the dot product is:  9.715213329752784e-14
matrix1 = [[1,2], [3,4]]
matrix2 = [[5,6],[7,8]]
def matmult(matrix):
    for i in len(matrix)
    
SyntaxError: incomplete input
matrix1[1]
[3, 4]
matrix[1][1]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    matrix[1][1]
NameError: name 'matrix' is not defined. Did you mean: 'matrix1'?
matrix1[1][1]
4
matrix[,1]
SyntaxError: invalid syntax
np.matmult(matrix1, matrix2)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    np.matmult(matrix1, matrix2)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\__init__.py", line 328, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'matmult'. Did you mean: 'matmul'?
np.matmul(matrix1, matrix2)
                         
array([[19, 22],
       [43, 50]])
def matmult(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2):
                           
SyntaxError: incomplete input
def matmult(matrix1, matrix2):
    numrows = len(matrix1)
    numcols = len(matrix2[0])
    result = [[[0]*numcols]*numrows]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k]*matrix2[k][j]
    return result

numrows = len(matrix1)
numcols = len(matrix2[0])
numrows
2
numcols
2
[0]*numcols
[0, 0]
[[0]*numcols]*numrows
[[0, 0], [0, 0]]
[[[0]*numcols]*numrows]
[[[0, 0], [0, 0]]]
def matmult(matrix1, matrix2):
    numrows = len(matrix1)
    numcols = len(matrix2[0])
    result = [[0]*numcols]*numrows
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k]*matrix2[k][j]
    return result

matmult(matrix1, matrix2)
[[62, 72], [62, 72]]
matrix2[0]
[5, 6]
def matmult(matrix1, matrix2):
    numrows = len(matrix1)
    numcols = len(matrix2[0])
    result = [[[0]*numcols]*numrows]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                print(matrix1[i][k], matrix2[k][i])
                result[i][j] += matrix1[i][k]*matrix2[k][j]
    return result

matrix1
[[1, 2], [3, 4]]
matrix2
[[5, 6], [7, 8]]
matmult(matrix1, matrix2)
1 5
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    matmult(matrix1, matrix2)
  File "<pyshell#76>", line 9, in matmult
    result[i][j] += matrix1[i][k]*matrix2[k][j]
TypeError: 'int' object is not iterable
def matmult(matrix1, matrix2):
    numrows = len(matrix1)
    numcols = len(matrix2[0])
    result =[[0]*numcols]*numrows
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                print(matrix1[i][k], matrix2[k][i])
                result[i][j] += matrix1[i][k]*matrix2[k][j]
    return result

matmult(matrix1, matrix2)
1 5
2 7
1 5
2 7
3 6
4 8
3 6
4 8
[[62, 72], [62, 72]]
def matmult(matrix1, matrix2):
    numrows = len(matrix1)
    numcols = len(matrix2[0])
    result =[[0]*numcols]*numrows
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                print(matrix1[i][k], matrix2[k][i], 'i equals', i, 'j equals', j, 'k equals', k)
                result[i][j] += matrix1[i][k]*matrix2[k][j]
    return result

matmult(matrix1, matrix2)
1 5 i equals 0 j equals 0 k equals 0
2 7 i equals 0 j equals 0 k equals 1
1 5 i equals 0 j equals 1 k equals 0
2 7 i equals 0 j equals 1 k equals 1
3 6 i equals 1 j equals 0 k equals 0
4 8 i equals 1 j equals 0 k equals 1
3 6 i equals 1 j equals 1 k equals 0
4 8 i equals 1 j equals 1 k equals 1
[[62, 72], [62, 72]]
matrix1
[[1, 2], [3, 4]]
matrix2
[[5, 6], [7, 8]]
matrix2[0][1]
6
matrix2[1][1]
8
def matmult(matrix1, matrix2):
    numrows = len(matrix1)
    numcols = len(matrix2[0])
    result =[[0]*numcols]*numrows
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                print(matrix1[i][k], matrix2[k][j], 'i equals', i, 'j equals', j, 'k equals', k)
                result[i][j] += matrix1[i][k]*matrix2[k][j]
    return result

matmult(matrix1, matrix2]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
matmult(matrix1, matrix2)
1 5 i equals 0 j equals 0 k equals 0
2 7 i equals 0 j equals 0 k equals 1
1 6 i equals 0 j equals 1 k equals 0
2 8 i equals 0 j equals 1 k equals 1
3 5 i equals 1 j equals 0 k equals 0
4 7 i equals 1 j equals 0 k equals 1
3 6 i equals 1 j equals 1 k equals 0
4 8 i equals 1 j equals 1 k equals 1
[[62, 72], [62, 72]]
def matmult(matrix1, matrix2):
    numrows = len(matrix1)
    numcols = len(matrix2[0])
    result =[[0]*numcols]*numrows
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k]*matrix2[k][j]
                print(result[i][j], 'i:', i, 'j:
                      , j)
    return result
SyntaxError: unterminated string literal (detected at line 9)
return result
SyntaxError: 'return' outside function
def matmult(matrix1, matrix2):
    numrows = len(matrix1)
    numcols = len(matrix2[0])
    result =[[0]*numcols]*numrows
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k]*matrix2[k][j]
                print(result[i][j], 'i:', i, 'j:', j)
    return result

matmult(matrix1, matrix2)
5 i: 0 j: 0
19 i: 0 j: 0
6 i: 0 j: 1
22 i: 0 j: 1
34 i: 1 j: 0
62 i: 1 j: 0
40 i: 1 j: 1
72 i: 1 j: 1
[[62, 72], [62, 72]]
np.matmul(matrix1, matrix2)
array([[19, 22],
       [43, 50]])
[[0]*numcols]*numrows
[[0, 0], [0, 0]]
result = [[0]*numcols]*numrows
result[0,0] = 19
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    result[0,0] = 19
TypeError: list indices must be integers or slices, not tuple
result[0][0] = 19
result[0][1] = 22
result
[[19, 22], [19, 22]]
result[1][0] = 4
result
[[4, 22], [4, 22]]
def matmult(matrix1, matrix2):
    numrows = len(matrix1)
    numcols = len(matrix2[0])
    result =[[0,0],[0,0]]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k]*matrix2[k][j]
    return result

>>> matmul(matrix1, matrix2)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    matmul(matrix1, matrix2)
NameError: name 'matmul' is not defined. Did you mean: 'matmult'?
>>> matmult(matrix1, matrix2)
[[19, 22], [43, 50]]
>>> np.matmul(matrix1, matrix2)
array([[19, 22],
       [43, 50]])
>>> matrix1 = [[1,2,3,4][5,6,7,8]]
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    matrix1 = [[1,2,3,4][5,6,7,8]]
TypeError: list indices must be integers or slices, not tuple
>>> matrix1 = [[1,2,3,4],[5,6,7,8]]
>>> matrix2 = [[4,5,6],[7,8,9],[10,11,12],[1,2,3]]
>>> np.matmul(matrix1, matrix2)
array([[ 52,  62,  72],
       [140, 166, 192]])
>>> matmult(matrix1, matrix2)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    matmult(matrix1, matrix2)
  File "<pyshell#109>", line 8, in matmult
    result[i][j] += matrix1[i][k]*matrix2[k][j]
IndexError: list index out of range
>>> def matmult(matrix1, matrix2):
...     numrows = len(matrix1)
...     numcols = len(matrix2[0])
...     result =[[0,0,0],[0,0,0]]
...     for i in range(len(matrix1)):
...         for j in range(len(matrix2[0])):
...             for k in range(len(matrix2)):
...                 result[i][j] += matrix1[i][k]*matrix2[k][j]
...     return result
... 
>>> matmult(matrix1, matrix2)
[[52, 62, 72], [140, 166, 192]]
