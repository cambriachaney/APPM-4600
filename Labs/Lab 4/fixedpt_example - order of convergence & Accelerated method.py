# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: (10/(x+4))**(0.5)
# fixed point is alpha1 = 1.4987....

    # f2 = lambda x: x - (x**5 - 7)/(12)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-10

# test f1 '''
     x0 = 1.5
     [xstar,ier, points] = fixedpt(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print("Vector of Iterations", points)
     print("The Number of Iterations is:", len(points))

     p = 1.3652300134140976
     [alpha, constant] = orderconvergence(p, points)
     print("The order of convergence is: ",alpha)
     print("The error constant is: ", constant)

     approx = accelerator(points)
     print('Vector of Accelerated Iterations:', approx)
     print('the number of iterations is:', len(approx))

     [alpha, constant] = orderconvergence(p, approx)
     print("The order of convergence of the accelerated version: ",alpha)
     print("The error constant of the accelerated version: ", constant)
     
#test f2 '''
    # x0 = 1.0
    # [xstar,ier] = fixedpt(f2,x0,tol,Nmax)
    # print('the approximate fixed point is:',xstar)
    # print('f2(xstar):',f2(xstar))
    # print('Error message reads:',ier)



# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    points = np.zeros((Nmax,1))
    
    while (count <Nmax):
       x1 = f(x0)
       points[count] = x1
       count = count +1
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          points = points[points != 0]
          return [xstar,ier, points]
       x0 = x1

    xstar = x1
    ier = 1
    points = points[points != 0]
    return [xstar, ier, points]

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

def accelerator(vector):
     approx = []
     for i in range(len(vector)-2):
          num = (vector[i+1] - vector[i])**2
          denom = vector[i+2] - 2*vector[i+1] + vector[i]
          approx.append(vector[i] - (num/denom))

     return approx


driver()
