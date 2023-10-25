import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm


def driver():
    
    f = lambda x: 1/(1+ x**2)
    fp = lambda x: (-2*x)/(1+x**2)**2
    a = -5
    b = 5
    
    
    ''' number of intervals'''
    Nint = 20
    #xint = np.linspace(a,b,Nint+1)
    Nint = Nint +1
    xint = np.array([5*np.cos((2*i -1)*np.pi / (2*Nint)) for i in range(1,Nint+1)])
    xint = np.flip(xint)
    print('xint', xint)
    yint = f(xint)
    ypint = fp(xint)

    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(xint[0],xint[Nint-1],Neval+1)

    
    
    (M,C,D) = create_natural_spline(yint,xint,Nint, ypint)
    
    print('M =', M)
#    print('C =', C)
#    print('D=', D)
    
    yeval = eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D)
    
#    print('yeval = ', yeval)
    
    ''' evaluate f at the evaluation points'''
    fex = f(xeval)
        
    nerr = norm(fex-yeval)
    print('nerr = ', nerr)
    
    plt.figure()    
    plt.plot(xeval,fex,'ro-',label='exact function')
    plt.plot(xeval,yeval,'bs--',label='natural spline') 
    plt.legend()
    plt.show()
     
    err = abs(yeval-fex)
    plt.figure() 
    plt.semilogy(xeval,err,'ro--',label='absolute error')
    plt.legend()
    plt.show()
    
def create_natural_spline(yint,xint,N, ypint):

#    create the right  hand side for the linear system
    b = np.zeros(N)
#  vector values
    h = np.zeros(N-1)  
    for i in range(1,N-2):
       hi = xint[i]-xint[i-1]
       hip = xint[i+1] - xint[i]
       b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
       h[i-1] = hi
       h[i] = hip
    print('hvec', h)
    # has up to N-3
    # N-2
    h[N-3] = xint[N-2] - xint[N-3]
    #N-1
    h[N-2] = xint[N-1] -xint[N-2]
    
    print("h vec", h)
    print("xint", xint)
    b[0] = -ypint[0] + (yint[1] - yint[0])/h[0]

    b[-1] = -ypint[-1] + (yint[-1] - yint[-2])/h[N-2]

    print('B vector', b)

#  create matrix so you can solve for the M values
# This is made by filling one row at a time 
    A = np.zeros((N,N))
    A[0][0] = h[0]/3
    A[0][1] = h[0]/6
    for j in range(1,N-1):
       A[j][j-1] = h[j-1]/6
       A[j][j] = (h[j]+h[j-1])/3 
       A[j][j+1] = h[j]/6
    A[N-1][N-1] = h[N-2]/3
    A[N-1][N-2] = h[N-2]/6
    print("A matrix: ", A)
    Ainv = inv(A)
    
    M  = Ainv.dot(b)

#  Create the linear coefficients
    C = np.zeros(N-1)
    D = np.zeros(N-1)
    for j in range(N-1):
       C[j] = yint[j]/h[j]-h[j]*M[j]/6
       D[j] = yint[j+1]/h[j]-h[j]*M[j+1]/6
    return(M,C,D)
       
def eval_local_spline(xeval,xi,xip,Mi,Mip,C,D):
# Evaluates the local spline as defined in class
# xip = x_{i+1}; xi = x_i
# Mip = M_{i+1}; Mi = M_i

    hi = xip-xi
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
            + C*(xip-xeval) + D*(xeval-xi)
    return yeval 
    
    
def  eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D):
    
    yeval = np.zeros(Neval+1)
    
    for j in range(Nint-1):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        atmp = xint[j]
        btmp= xint[j+1]
        
#   find indices of values of xeval in the interval
        ind= np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]

# evaluate the spline
        yloc = eval_local_spline(xloc,atmp,btmp,M[j],M[j+1],C[j],D[j])
        #print('yloc = ', yloc)
#   copy into yeval
        yeval[ind] = yloc

    return(yeval)
           
driver()               

