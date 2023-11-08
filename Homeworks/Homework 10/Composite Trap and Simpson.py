import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import quad

def driver():

    f = lambda x: 1/(1+x**2)
    a = -5
    b = 5

    actual = quad(f,a,b)
    print('The Actual Integral is: ', actual[0])
    
    integral = composite_trap(f, a, b, 1291)
    print('The Composite Trapezoidal Approximation is: ', integral)
    print("The Error is:", abs(actual[0] - integral))

    integral1 = composite_simp(f, a, b, 108)
    print('The Composite Simpson Approximation is: ', integral1)
    print("The Error is:", abs(actual[0] - integral1))

    actual_6 = quad(f,a,b,epsabs = 10**(-6), full_output = 1)
    actual_4 = quad(f,a,b,epsabs = 10**(-4), full_output = 1)
    print("The actual value with 10^-6 is:", actual_6[0], " with ", list(actual_6[2].items())[0])
    print("The actual value with 10^-4 is:", actual_4[0], " with ", list(actual_4[2].items())[0])

def composite_trap(f, a, b,n):

    xint = np.linspace(a,b,n+1)

    h = (b-a)/n

    summ = 0
    for i in range(1,n):
        summ = summ + f(xint[i])       
    

    return (h/2)*(f(a) + 2*summ + f(b))

def composite_simp(f, a, b,n):

    xint = np.linspace(a,b,n+1)

    h = (b-a)/n

    summ1 = 0
    for i in range(1,int(n/2)):
        summ1 = summ1 + f(xint[(i*2)])

    summ2 = 0
    for i in range(1, int((n/2)+1)):
        summ2 = summ2 + f(xint[int(2*i - 1)])
        
    return (h/3)*(f(a) + 2*summ1 + 4* summ2 + f(b))

    
driver()
