# import libraries
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
        
def driver():
#f = lambda x: (x-2)**3
#fp = lambda x: 3*(x-2)**2
#p0 = 1.2

  f = lambda x: x**6 - x - 1
  fp = lambda x: 6*x**5 - 1
  p0 = 2

  Nmax = 100
  tol = 1.e-14

  (p,pstar,info,it, count) = newton(f,fp,p0,tol, Nmax)
  print('the approximate root is', '%16.16e' % pstar)
  print('the error message reads:', '%d' % info)
  print('Number of iterations:', '%d' % it)

  mydata = []
  for i in range(count):
    mydata.append([i, p[i] - pstar])

  headers = ["Iteration", "Error"]

  print(tabulate(mydata, headers = headers, tablefmt = "fancy_grid"))

  yn = []

  y1 = []
    
  for i in range(len(mydata)-1):
    yn.append(mydata[i][1])

  for i in range(len(mydata)-1):
      y1.append(mydata[(i+1)][1])
    
  plt.loglog(y1, yn)
  plt.show()

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
      p1 = p0-f(p0)/fp(p0)
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
        
driver()
