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

    mydata = []
    for i in range(count):
        mydata.append([i, p[i] - pstar])

    headers = ["Iteration", "Error"]

    print(tabulate(mydata, headers = headers, tablefmt = "fancy_grid"))

    # Plot xn - root and xn+1 - root

    yn = []

    y1 = []
    
    for i in range(len(mydata)-1):
        yn.append(mydata[i][1])

    for i in range(len(mydata)-1):
        y1.append(mydata[(i+1)][1])
    
    plt.loglog(y1, yn)
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
            pstar = p2
            ier = 0
            return [p, pstar, ier, count]

        p0 = p1
        fp0 = fp1
        p1 = p2
        fp2 = f(p2)



    pstar = p2
    ier = 1
    return [p, pstar, ier, count]
    


driver()
