import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 


def driver():
    
    f = lambda x: 1/(1+(10*x)**2)
    a = -1
    b = 1
    
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(a,b,Neval)
    
    ''' number of intervals'''
    Nint = 3
    
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    
    ''' evaluate f at the evaluation points'''
    #fex = np.zeros(Neval)
    #for j in range(Neval):
     # fex[j] = f(xeval[j]) 
      
    
    #plt.figure()
    #plt.plot(xeval,fex,'ro-')
    #plt.plot(xeval,yeval,'bs-')
    #plt.legend()
    #plt.show() 
     
    #err = abs(yeval-fex)
    #plt.figure()
    #plt.plot(xeval,err,'ro-')
   # plt.show()

    ''' evaluate the cubic spline '''
    [Si, x_eval] = cubic_spliness(xeval, a, b, f, Nint)
    
    fex1 = np.zeros(Neval)
    for j in range(Neval):
        fex1[j] = f(xeval[j])

    plt.figure()
    plt.plot(xeval, fex1, 'ro-')
    for i in range(len(Si)):
        plt.plot(x_eval[i], Si[i], 'bs-')
    plt.show()
    
    

    
    
def  eval_lin_spline(xeval,Neval,a,b,f,Nint):

    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a,b,Nint+1)
   
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval) 
    
    
    for jint in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        '''let n denote the length of ind'''
        ind = np.where((xint[jint] < xeval) & (xint[jint+1] > xeval))
        n = len(ind[0])
        
        '''temporarily store your info for creating a line in the interval of 
         interest'''
        a1= xint[jint]
        fa1 = f(a1)
        b1 = xint[jint+1]
        fb1 = f(b1)
        
        for kk in range(n):
           '''use your line evaluator to evaluate the lines at each of the points 
           in the interval'''
           '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with 
           the points (a1,fa1) and (b1,fb1)'''

           yeval[ind[0][kk]] = line_finder(a1, fa1, b1, fb1, xeval[ind[0][kk]])

    return yeval
           
           
def interval_finder(xeval, xint1, xint2):

    ind = np.where((xeval > xint1) & (xeval < xint2))

    return ind

def line_finder(x0, y0, x1, y1, xeval):

    slope = (y1 - y0)/(x1 - x0)

    return slope*(xeval - x0) + y0

def cubic_splines(xeval, a, b, f, Nint):

    xint = np.linspace(a,b,Nint+1)
    
    h = (b-a)/Nint
    
    matrix = np.zeros([Nint-1, Nint-1])

    for i in range(Nint - 1):
        for j in range(Nint - 1):
            if i == j:
                matrix[i][j] = 1/3
            elif abs(i - j) == 1:
                matrix[i][j] = 1/12

    yvec = np.zeros([Nint -1, 1])

    for i in range(1,Nint-1):
        yvec[i] = (f(xint[i+1]) - 2*f(xint[i]) + f(xint[i-1]))/(2*h**2)

    matrix_inv = inv(matrix)

    coef = matrix_inv.dot(yvec)

    Si_matrix = []
    x_eval = []

    for i in range(Nint):
        ind = np.where((xint[i] < xeval) & (xint[i+1] > xeval))
        x_eval.append(xeval[ind[0]])

    for i in range(Nint):
        
        first = (coef[i]*(xint[i+1] - x_eval[i])**3)/(6*h)
        second = coef[i+1]*(x_eval[i] - xint[i])**3
        C = f(xint[i])/h - (h/6)*coef[i]
        D = f(xint[i+1])/h - (h*coef[i+1])/6
        third = C*(xint[i+1] - 1)
        fourth = D*(x_eval[i] - xint[i])

        Si_matrix.append(first + second + third + fourth)

    print(len(Si_matrix))
    print(len(x_eval))

    return [Si_matrix, x_eval]
            
def cubic_spline(xeval, a, b, f, Nint):

    xint = np.linspace(a,b,Nint+1)
    print("xint:", len(xint))
    
    h = (b-a)/Nint
    print("h: ", h)
    
    matrix = np.zeros([Nint+1, Nint+1])

    for i in range(Nint + 1):
        for j in range(Nint + 1):
            if i == j:
                matrix[i][j] = h*(2/3)
            elif abs(i - j) == 1:
                matrix[i][j] = h/6

    yvec = np.zeros([Nint + 1, 1])

    for i in range(1,Nint):
        yvec[i] = (f(xint[i+1]) - 2*f(xint[i]) + f(xint[i-1]))/(h)

    print("yvec: ", len(yvec))
    
    matrix_inv = inv(matrix)

    coef = matrix_inv.dot(yvec)

    print("Coef:", len(coef))
    
    Si_matrix = []
    x_eval = []


    for i in range(Nint):
        ind = np.where((xint[i] < xeval) & (xint[i+1] > xeval))
        x_eval.append(xeval[ind[0]])

    print("Xeval:", len(x_eval))

    for i in range(Nint):
        
        first = (coef[i]*(xint[i+1] - x_eval[i])**3)/(6*h)
        second = (coef[i+1]*(x_eval[i] - xint[i])**3)/(6*h)
        C = f(xint[i])/h - ((h/6)*coef[i])
        D = f(xint[i+1])/h - ((h*coef[i+1])/6)
        third = C*(xint[i+1] - 1)
        fourth = D*(x_eval[i] - xint[i])

        Si_matrix.append(first + second + third + fourth)

    print("Si: ", len(Si_matrix))
    print("Si[0]: ", len(Si_matrix[0]))
    print(Si_matrix)

    return [Si_matrix, x_eval]

def cubic_spliness(xeval, a, b, f, Nint):

    xint = np.linspace(a,b,Nint+1)
    print("xint:", len(xint))
    
    h = (b-a)/Nint
    print("h: ", h)
    
    matrix = np.zeros([Nint+1, Nint+1])

    for i in range(Nint + 1):
        for j in range(Nint + 1):
            if i == j:
                matrix[i][j] = h/6
            elif i+1 == j:
                matrix[i][j] = (2/3)*h
            elif i+2 == j:
                matrix[i][j] = h/6

    print(matrix)

    yvec = np.zeros([Nint + 1, 1])

    for i in range(1,Nint):
        yvec[i] = (f(xint[i+1]) - 2*f(xint[i]) + f(xint[i-1]))/(h)

    print("yvec: ", len(yvec))
    
    matrix_inv = inv(matrix)

    coef = matrix_inv.dot(yvec)

    print("Coef:", len(coef))
    
    Si_matrix = []
    x_eval = []


    for i in range(Nint):
        ind = np.where((xint[i] < xeval) & (xint[i+1] > xeval))
        x_eval.append(xeval[ind[0]])

    print("Xeval:", len(x_eval))
    print("xeval[0]: ", len(x_eval[0]))

    for i in range(Nint):
        
        first = (coef[i]*(xint[i+1] - x_eval[i])**3)/(6*h)
        second = (coef[i+1]*(x_eval[i] - xint[i])**3)/(6*h)
        C = f(xint[i])/h - ((h/6)*coef[i])
        D = f(xint[i+1])/h - ((h*coef[i+1])/6)
        third = C*(xint[i+1] - 1)
        fourth = D*(x_eval[i] - xint[i])

        Si_matrix.append(first + second + third + fourth)

    print("Si: ", len(Si_matrix))
    print("Si[0]: ", len(Si_matrix[0]))
    print(Si_matrix)

    return [Si_matrix, x_eval]
        
    
    

if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()
