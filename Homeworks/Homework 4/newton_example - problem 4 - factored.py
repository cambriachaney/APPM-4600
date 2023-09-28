# import libraries
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
        
def driver():
#f = lambda x: (x-2)**3
#fp = lambda x: 3*(x-2)**2
#p0 = 1.2

  f = lambda x: (np.e**x - 3*x**2)**3
  fp = lambda x: 3*(np.e**x - 3*x**2)**2 * (np.e**x - 6*x)
  fp2 = lambda x: 3*(np.e**x - 3*x**2)**2 * (np.e**x - 6) + (np.e**x - 6*x)*6*(np.e**x - 3*x**2)*(np.e**x - 6*x)

  f_input = lambda x: f(x)/fp(x)
  f_derivative = lambda x: ((fp(x))**2 - f(x)*fp2(x))/ (fp(x))**2
  
  p0 = 4

  Nmax = 100
  tol = 1.e-10

  (p,pstar,info,it, count) = newton(f,fp,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)
  [alpha, constant] = orderconvergence(pstar, p)
  print("The order of convergence is: ", alpha)

def newton(f,fp,p0,tol,Nmax):
  """
  Newton iteration.
  
  Inputs:
    f,fp - function and derivative
    p0   - initial guess for root
    tol  - iteration stops when p_n,p_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    p     - an array of the iterates
    pstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
     
  """
  p = np.zeros(Nmax+1);
  p[0] = p0
  count = 0
  for it in range(Nmax):
      p1 = p0 - 3*f(p0)/fp(p0)
      p[it+1] = p1
      count = count + 1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [p,pstar,info,it, count]
      p0 = p1
  pstar = p1
  info = 1
  return [p,pstar,info,it, count]

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
