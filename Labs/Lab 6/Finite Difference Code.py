import numpy as np
from tabulate import tabulate

def driver():


    f = lambda x: np.cos(x)

    s = np.pi/2

    h = 0.01*2.**(-np.arange(0,10))

    forward = forward_difference(f, s, h)

    centered = centered_difference(f, s, h) 

    print("Forward Difference Vector:", forward)

    print("Order of Convergence - Forward:", orderconvergence(-1, forward)[0])

    print("Centered Difference Vector:", centered)

    print("Order of Convergence - Centered:", orderconvergence(-1, centered)[0])


def forward_difference(f, s, h):
   

    return (f(s+h) - f(s))/(h)


def centered_difference(f, s, h):

    return (f(s+h) - f(s-h))/(2*h)

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
