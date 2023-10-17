import numpy as np
import matplotlib.pyplot as plt

def driver():

    xeval = np.linspace(0,10,1000)

    xint = np.linspace(0,10,11)

    evaluation = interval_finder(xeval, xint)

    print(evaluation)

    x0 = 4
    y0 = 8

    x1 = -9
    y1 = -7

    [x, y] = line_finder(x0,y0,x1,y1, np.linspace(-10,10,1000))
    
    plt.plot(x, y)
    plt.plot(x0, y0, color = "red", marker = 'o')
    plt.plot(x1, y1, color = "red", marker = 'o')
    plt.show()

def interval_finder(xeval, xint):

    evaluation = []   

    for i in range(len(xint) - 1):
        
        ind = np.where((xeval > xint[i]) & (xeval < xint[(i+1)]))

        xeval_interval = []

        for v in ind:
            xeval_interval.append(xeval[v])
            

        #print("indices of xeval in interval ", i , "are:", xeval_interval)

        evaluation.append(xeval_interval)

    return evaluation

def line_finder(x0, y0, x1, y1, xeval):

    slope = (y1 - y0)/(x1 - x0)

    f = lambda x: slope * (x - x0) + y0

    y = f(xeval)

    return [xeval, y]
    

driver()
