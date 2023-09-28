import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

def driver():


    f = lambda x: x**6 - x - 1

    p0 = 2
    p1 = 1

    Nmax = 100
    tol = 1.e-14

    (p, pstar, ier, count) = secant(p0, p1, f, tol, Nmax)
    print('the approximate root is', '%16.16e' % pstar)
    print('the error message reads:', '%d' % ier)
    print('Number of iterations:', '%d' % count)

    [alpha, constant] = orderconvergence(pstar, p)
    print("The order of convergence is: ", alpha)

    mydata = []
    for i in range(count):
        mydata.append([i, p[i] - pstar])

    headers = ["Iteration", "Error"]

    print(tabulate(mydata, headers = headers, tablefmt = "fancy_grid"))

    # Plot xn - root and xn+1 - root

    yn = []

    y1 = []
    
    for i in range(len(mydata)-1):
        yn.append(abs(mydata[i][1]))

    for i in range(len(mydata)-1):
        y1.append(abs(mydata[(i+1)][1]))

    slope = (np.log(y1[6]) - np.log(y1[4]))/(np.log(yn[6]) - np.log(yn[4]))
    print("The slope of the log log graph is: ", slope)
    
    plt.plot(y1, yn)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
  
def secant(p0,p1,f,tol, Nmax):

    p = np.zeros(Nmax +1)
    p[0] = p0
    count = 0
        
    if abs(f(p0)) == 0:
        pstar = p0
        ier = 0
        return [p, pstar, ier, count]
        
    if abs(f(p1)) == 0:
        pstar = p1
        ier = 0
        return [p, pstar, ier, count]

    fp1 = f(p1)
    fp0 = f(p0)

    for i in range(1, Nmax +1):
        count = count + 1
            
        if abs(fp1 - fp0) == 0:
            ier = 1
            pstar = p1
            return [p, pstar, ier, count]

        p2 = p1 - (fp1 *(p1-p0))/(fp1 - fp0)

        p[i] = p2

        if abs(p2 - p1) < tol:
            pstar = p1
            ier = 0
            return [p, pstar, ier, count]

        p0 = p1
        fp0 = fp1
        p1 = p2
        fp1 = f(p2)



    pstar = p2
    ier = 1
    return [p, pstar, ier, count]

def orderconvergence(point, vector):
     N = len(vector)
     num = abs(vector[(N-1)] - point)
     denom = abs(vector[(N-2)] - point)
     if (isinstance(num/denom, float)) and (num/denom < 1):
        alpha = 1
        constant = num/denom
        return [alpha, constant]
     alpha = 2
     while num/(denom**alpha) == float("INF"):
         alpha = alpha + 1
     return [alpha, num/(denom**alpha)]


driver()
