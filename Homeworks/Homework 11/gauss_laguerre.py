import numpy as np

def driver():
    x = 10
    f = lambda t: t**(x-1)
    M = 7
    tol = 10**(-8)
    a = 0
    b = 100000
    I_ex = 362880
  

    [I,nodes,weights] = eval_gauss_quad(M,a,b,f)
    print("The approximate integral using Gauss-Laguerre is:", I)
    print("The error of this method is:", abs(I - I_ex))
    #print("the number of intervals using Gaussian are:", intervals)
    #print("The nodes using Gaussian are:", nodes)
  
def eval_gauss_quad(M,a,b,f):
  """
  Non-adaptive numerical integrator for \int_a^b f(x)w(x)dx
  Input:
    M - number of quadrature nodes
    a,b - interval [a,b]
    f - function to integrate
  
  Output:
    I_hat - approx integral
    x - quadrature nodes
    w - quadrature weights

  Currently uses Gauss-Legendre rule
  """
  t,w = np.polynomial.laguerre.laggauss(M)
  I_hat = np.sum(f(t)*w)
  return I_hat,t,w

driver()
