import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from numpy.linalg import inv

def driver():


    f = lambda x: 1/(1+(10*x)**2)

    N = 5
    ''' interval'''
    a = -1
    b = 1
   
       
    ''' create equispaced interpolation nodes'''
    xint = np.linspace(a,b,N+1)
    
    h = 2/(N-1)
    xint = np.array([-1+(i-1)*h for i in range(N+1)])
    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1001
    xeval = np.linspace(a,b,Neval+1)
    yeval_l= np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)
    yeval_b = np.zeros(Neval + 1)

    yeval_mono = f(xeval)
    
    #[a_vec, polynomial_eval, vander_inv] = monomials(f, xint, N, xeval)
    #print("The Vandermonde Matrix is:", vander_inv)
    #print("The coefficients are:", a_vec)
    #plt.plot(xeval, yeval_mono, label = "Actual Plot")
    #plt.plot(xeval, polynomial_eval, label = "Approximation of Monomial")
    #plt.plot(xeval, abs(yeval_mono - polynomial_eval), label = "Error of Monomial")
    #plt.legend()
    #plt.show()
    
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    for j in range(N+1):
       y[j][0]  = yint[j]

    y = dividedDiffTable(xint, y, N+1)

    print("Y Table", y)
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
       yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
       yeval_b[kk] = barycentric_lagrange(xeval[kk],xint,yint,N)
          


    ''' create vector with exact values'''
    fex = f(xeval)
       
    'Approximation Plot'
    plt.figure()    
    plt.plot(xeval,fex,'ro-', label = 'Actual Plot')
    #plt.plot(xeval,yeval_l,'bs--', label = 'Lagrange')
    plt.plot(xeval,yeval_b, 'c.--', label = "Barycentric")
    #plt.plot(xeval,yeval_dd,'c.--', label = 'Newton DD')
    plt.legend()

    'Error Plot'
    plt.figure() 
    err_l = abs(yeval_l-fex)
    err_dd = abs(yeval_dd-fex)
    err_b = abs(yeval_b - fex)
    #plt.semilogy(xeval,err_l,'ro--',label='lagrange')
    plt.semilogy(xeval, err_b, 'bs--', label = 'Barycentric')
    #plt.semilogy(xeval,err_dd,'bs--',label='Newton DD')
    plt.legend()
    plt.show()

# Try Number 1 for Barycentric Code
def bary_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    w = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])
              w[count] *= (xint[count] - xint[jj])

    w = 1/w
    yeval = 0.
    num = 0
    denom = 0
    
    for jj in range(N+1):
        if xeval != xint[jj]:
           num += w[jj]*yint[jj] / (xeval - xint[jj])
           denom += w[jj]/(xeval - xint[jj])

    yeval = num/denom
  
    return(yeval)

#Try Number 2 for Barycentric Code - THE CORRECT ONE
def barycentric_lagrange(xeval,xint,yint,N):

    lj = 1
    
    for count in range(N+1):
        lj = lj*(xeval - xint[count])

    wj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
                wj[count] = wj[count]*(xint[count] - xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
        #if xeval != xint[jj]:
           yeval = yeval + lj*yint[jj]*(1/wj[jj])*(1/(xeval - xint[jj]))
  
    return(yeval)

def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  
    


''' create divided difference matrix'''
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
    
def evalDDpoly(xval, xint,y,N):
    ''' evaluate the polynomial terms'''
    ptmp = np.zeros(N+1)
    
    ptmp[0] = 1.
    for j in range(N):
      ptmp[j+1] = ptmp[j]*(xval-xint[j])
     
    '''evaluate the divided difference polynomial'''
    yeval = 0.
    for j in range(N+1):
       yeval = yeval + y[0][j]*ptmp[j]  

    return yeval

def monomials(f,x,N, xeval):
    
    vander = np.zeros([N+1,N+1])
    for i in range(N+1):
        for v in range(N+1):
            vander[i][v] = x[i]**(v)

    vander_inv = inv(vander)

    y = f(x)

    a = vander_inv.dot(y)

    #print(a)

    polynomial_eval = []
    
    for v in xeval:
        num = 0
        for i in range(N+1):
            num += a[i]*v**i

        polynomial_eval.append(num)

    return [a, polynomial_eval, vander_inv]
       

driver()        
