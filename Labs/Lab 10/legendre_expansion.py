import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import math
import scipy
from scipy.integrate import quad

def driver():

#  function you want to approximate
    f = lambda x: math.exp(x)

# Interval of interest    
    a = -1
    b = 1
# weight function    
    w = lambda x: 1.

# order of approximation
    n = 2

#  Number of points you want to sample in [a,b]
    N = 1000
    xeval = np.linspace(a,b,N+1)
    pval = np.zeros(N+1)

    for kk in range(N+1):
      pval[kk] = eval_legendre_expansion(f,a,b,w,n,xeval[kk])
      
    ''' create vector with exact values'''
    fex = np.zeros(N+1)
    for kk in range(N+1):
        fex[kk] = f(xeval[kk])
        
    plt.figure()    
    plt.plot(xeval,fex,'ro-', label= 'f(x)')
    plt.plot(xeval,pval,'bs--',label= 'Expansion') 
    plt.legend()
    plt.show()    
    
    err = abs(pval-fex)
    plt.semilogy(xeval,err_l,'ro--',label='error')
    plt.legend()
    plt.show()
    
      
def eval_legendre_expansion(f,a,b,w,n,x): 

#   This subroutine evaluates the Legendre expansion

#  Evaluate all the Legendre polynomials at x that are needed
# by calling your code from prelab 
  p = eval_legendre(n,x)
  # initialize the sum to 0 
  pval = 0.0    
  for j in range(0,n+1):
      # make a function handle for evaluating phi_j(x)
      phi_j = lambda x: eval_legendre(n,x)[j]
      # make a function handle for evaluating phi_j^2(x)*w(x)
      phi_j_sq = lambda x: phi_j(x)**2
      aj = coefficients(f, phi_j,phi_j_sq, w, a, b)
      # accumulate into pval
      pval = pval+aj*p[j] 
       
  return pval

def eval_legendre_expansion1(f,a,b,w,n,x): 

#   This subroutine evaluates the Legendre expansion

#  Evaluate all the Legendre polynomials at x that are needed
# by calling your code from prelab 
  p = eval_legendre(n,x)
  # initialize the sum to 0 
  pval = 0.0    
  for j in range(0,n+1):
      # make a function handle for evaluating phi_j(x)
      phi_j = lambda x: x**2
      # make a function handle for evaluating phi_j^2(x)*w(x)
      phi_j_sq = lambda x: x**4
      # use the quad function from scipy to evaluate normalizations
      norm_fac,err = coefficients(f, phi_j, phi_j_sq, w, a, b)
      # make a function handle for phi_j(x)*f(x)*w(x)/norm_fac
      func_j = lambda x: ...
      # use the quad function from scipy to evaluate coeffs
      aj,err = ...
      # accumulate into pval
      pval = pval+aj*p[j] 
       
  return pval

def coefficients(f,Q, Q_s, w, a, b):

    function1 = lambda x: f(x) * Q(x)*w(x)
    function2 = lambda x: w(x) * Q_s(x)

    [integral1, error1] = scipy.integrate.quad(function1,a, b)
    [integral2, error2] = scipy.integrate.quad(function2,a, b)

    return integral1/integral2

def eval_legendre(n,x):

    p = [1,x]

    for i in range(2,n+2):
        term = (1/i)*((2*(i-1)+1)*x*p[i-1] - (i-1)*p[i-2])
        p.append(term)

    return p
    
if __name__ == '__main__':
  # run the drivers only if this is called from the command line
  driver()               
