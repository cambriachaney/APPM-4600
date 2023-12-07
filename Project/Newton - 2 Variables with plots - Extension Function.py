import numpy as np
import math
import sympy as sym
from numpy.linalg import inv 
from numpy.linalg import norm
import matplotlib.pyplot as plt

def driver():

    x0 = [10,-20]
    variables = ['a', 'b']
    Nmax = 100
    tol = 10**(-6)
    [xstar, ier, it, xvec, yvec, zvec] = NewtonDescent(x0, tol, Nmax, variables)

    gval = evalF(xstar)

    print("The optimal x_vector from this method is:", xstar)
    print("The optimal function value from this method is:", gval)
    print("The number of iterations this method took is:", it)

    # plotting the 3D function
    
    ax = plt.axes(projection = "3d")
    
    ax.scatter3D(xvec, yvec, zvec, c = zvec, cmap = 'rainbow_r')
    
    x = np.linspace(-50,50,100)
    y = np.linspace(-50,50,100)
    X,Y = np.meshgrid(x,y)
    Z = function(X,Y)
    ax.plot_surface(X,Y,Z, alpha = 0.5,rstride =1, cstride =1, cmap = 'viridis', edgecolor = 'none')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    plt.show()

def function(x,y):
    return 7.33*10**(-9)*(y*(x-36.536)**2) + 5*10**(-9)*(x*(y+0.00176)**2)

def eval_hessian(x, variables):

    M = len(variables)

    a = sym.Symbol('a')
    b = sym.Symbol('b')

    #### MUST CHANGE FUNCTION HERE TOO!!!!!
    
    function = 7.33*10**(-9)*(b*(a-36.536)**2) + 5*10**(-9)*(a*(b+0.00176)**2)
    
    matrix = np.zeros([M,M])

    for i in range(M): #rows
        for j in range(M): #variables
            first = sym.diff(function,variables[j])
            #print(first)
            second = sym.diff(first,variables[i])
            #print(second)
            evaluate = second.subs({a:x[0], b:x[1]})
            matrix[i][j] = evaluate    

    return matrix

def evalF(x):

    F = 7.33*10**(-9)*(x[1]*(x[0]-36.536)**2) + 5*10**(-9)*(x[0]*(x[1]+0.00176)**2)
    return F

def eval_grad(x):
    F = evalF(x)
    grad = np.array([7.33*10**(-9)*x[1]*2*(x[0]-36.536)+5*10**(-9)*(x[1]+0.00176)**2,7.33*10**(-9)*(x[0]-36.536)**2 + 5*10**(-9)*x[0]*2*(x[1]+0.00176)])
    return grad

def NewtonDescent(x0,tol,Nmax, variables):

    hessian = eval_hessian(x0, variables)
    hessian_inv = inv(hessian)
    gradient = eval_grad(x0)
    p = hessian_inv.dot(gradient)
    x1 = x0 - p

    it = 1

    x_vec = [x0[0],x1[0]] # for plotting
    y_vec = [x0[1],x1[1]]  # for plotting
    z_vec = [function(x0[0], x0[1]),function(x1[0], x1[1])]
    
    while norm(x1 - x0)>tol:

        x0 = x1
        hessian = eval_hessian(x0, variables)
        hessian_inv = inv(hessian)
        gradient = eval_grad(x0)
        p = hessian_inv.dot(gradient)
        x1 = x0 - p
        it = it + 1

        x_vec.append(x1[0])
        y_vec.append(x1[1])
        z_vec.append(function(x1[0], x1[1]))

        if it >= Nmax:
            xstar = x1
            ier = 1
            print("The Max Number of Iterations was Met")
            return [xstar, ier, it, x_vec, y_vec, z_vec]

    xstar = x1
    ier = 0

    print(x_vec)
    return [xstar, ier, it, x_vec, y_vec, z_vec]

driver()
