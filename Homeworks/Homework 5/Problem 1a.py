#Problem 1a

import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm
from tabulate import tabulate

def driver():

    x0 = np.array([1,1])

    points = [x0]


    for i in range(25):
        J = evalJ(x0)
        F = evalF(x0)
        
        x1 = x0 - J.dot(F)
        
        points.append(x1)
        
        x0 = x1

    print(tabulate(points, headers = ["x0", "y0"], tablefmt = "fancy_grid"))
    

def evalF(x): 

    F = np.zeros(2)
    
    F[0] = 3*x[0]**2 - x[1]**2
    F[1] = 3*x[0]*x[1]**2 - x[0]**3 - 1
    return F

def evalJ(x): 

    
    J = np.array([[1/6,1/18 ], 
        [0,1/6]])
    
    return J

driver()
