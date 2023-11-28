import numpy as np
import math
import sympy as sym
from numpy.linalg import inv 
from numpy.linalg import norm

def driver():

    x0 = [1,1,1]
    variables = ['a', 'b', 'c']
    Nmax = 100
    tol = 10**(-4)
    [xstar, ier] = NewtonDescent(x0, tol, Nmax, variables)

    gval = evalF(xstar)

    print("The optimal x_vector from this method is:", xstar)
    print("The optimal function value from this method is:", gval)
    


def eval_hessian(x, variables):

    M = len(variables)

    a = sym.Symbol('a')
    b = sym.Symbol('b')
    c = sym.Symbol('c')

    #### MUST CHANGE FUNCTION HERE TOO!!!!!
    
    function = a + sym.cos(a*b*c) - 1
    
    matrix = np.zeros([M,M])

    for i in range(M): #rows
        for j in range(M): #variables
            first = sym.diff(function,variables[j])
            #print(first)
            second = sym.diff(first,variables[i])
            #print(second)
            evaluate = second.subs({a:x[0], b:x[1], c:x[2]})
            matrix[i][j] = evaluate    

    return matrix

def evalF(x):

    F = x[0] + math.cos(x[0]*x[1]*x[2]) - 1.
    return F

def eval_grad(x):
    F = evalF(x)
    grad = np.array([1 + x[1] * x[2] * math.sin(x[0] * x[1] * x[2]),x[0] * x[2] * math.sin(x[0] * x[1] * x[2]),x[0] * x[1] * math.sin(x[0] * x[1] * x[2])])
    return grad

def NewtonDescent(x0,tol,Nmax, variables):

    hessian = eval_hessian(x0, variables)
    hessian_inv = inv(hessian)
    gradient = eval_grad(x0)
    p = hessian_inv.dot(gradient)
    x1 = x0 - p

    it = 1

    x_vec = []
    
    while norm(x1 - x0)>tol:

        x0 = x1
        hessian = eval_hessian(x0, variables)
        hessian_inv = inv(hessian)
        gradient = eval_grad(x0)
        p = hessian_inv.dot(gradient)
        x1 = x0 - p
        it = it + 1

        if it >= Nmax:
            xstar = x1
            ier = 1
            print("The Max Number of Iterations was Met")
            return [xstar, ier]

    xstar = x1
    ier = 0

    return [xstar, ier]

driver()
