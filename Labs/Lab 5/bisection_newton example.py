# import libraries
import numpy as np

def driver():

# use routines    
    f = lambda x: np.sin(x)
    fp = lambda x: np.cos(x)
    a = 0.5
    b = 3*np.pi*0.25

#    f = lambda x: np.sin(x)
#    a = 0.1
#    b = np.pi+0.1

    tol = 1e-10
    Nmax = 100

    [points, pstar, ier, count] = bisection_newton(f,fp,a,b,tol,Nmax)
    print('the approximate root is',pstar)
    print('the error message reads:',ier)
    print('f(astar) =', f(pstar))
    print('The number of iterations is: ', count)




# define routines
def bisection_newton(f,fp,a,b,tol,Nmax):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b);
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, ier]

    count = 0
    d = 0.5*(a+b)

    condition = d - f(d)/fp(d)

    if condition > a and condition < b:
        return newton(f, fp, d, tol, Nmax)

    else:
        points = np.zeros(Nmax + 1)
        count = 0
        while (abs(d-a)> tol):
          fd = f(d)
          count = count + 1
          points[count] = d
          
          if (fd ==0):
            astar = d
            ier = 0
            return [points, astar, ier, count]
          if (fa*fd<0):
             b = d
          else: 
            a = d
            fa = fd
          d = 0.5*(a+b)
          count = count +1
    #      print('abs(d-a) = ', abs(d-a))
      
        astar = d
        ier = 0
        return [points, astar, ier, count]

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
  points = np.zeros(Nmax+1);
  points[0] = p0
  count = 0
  for it in range(Nmax):
      p1 = f(p0)/fp(p0)
      p[it+1] = p1
      count = count + 1
      if (abs(p1-p0) < tol):
          pstar = p1
          info = 0
          return [points,pstar,info,count]
      p0 = p1
  pstar = p1
  info = 1
  return [points,pstar,info, count]
      
driver()               

