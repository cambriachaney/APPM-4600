Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Homework 3 Problem 2
>>> # edited the bisection code given to use in class and ran it with the appropriate equations and values
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example.py
the approximate root is 5.000073242187501
the error message reads: 0
f(astar) = 6.065292655789404e-38
>>> # Problem 2b
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example.py
the approximate root is 5.12875
the error message reads: 0
f(astar) = 0.0
>>> #(c) What is happening is that with the larger floating point arithemetic (and potential rounding) in the expanded version, it is getting a root that is a little farther off than the actual answer, but the function at the root is exactly 0 in the expanded function but it not exactly 0 in the compressed version. This again makes sense because you don't want to subtract two similar items which is what you are doing in the compressed version but not in the expanded version.
