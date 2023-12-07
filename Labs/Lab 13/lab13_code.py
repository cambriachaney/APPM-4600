import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time
from numpy.linalg import inv

def driver():


     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     N = 100
 
     ''' Right hand side'''
     b = np.random.rand(N,1)
     A = np.random.rand(N,N)

     QR_solve(A,b)
     
     start1 = time.perf_counter()
     
     x = scila.solve(A,b)

     end1 = time.perf_counter()
     time1= end1 - start1

     print("The time it takes for the original method is:", time1)

     test = np.matmul(A,x)
     r = la.norm(test-b)
     
     print("The Test Norm of the original method is:", r)

     '''LU Method'''
     [x, factor_time, solve_time, total_time] = scipy_LU(A, b)
     print("The time it takes for the LU Method to factor is:", factor_time)
     print("The time it takes for the LU Method to solve is:", solve_time)
     print("The time it takes for the LU Method to do both is:", total_time)
     
     test = np.matmul(A,x)
     r = la.norm(test-b)
     
     print("The test norm of the LU Method is:", r)

     print("The LU solver is this times faster than the built in one:", time1/total_time)

     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)

     normal(A,b)
     QR_solve(A,b)

     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B

def scipy_LU(A,b):
     start2 = time.perf_counter()
     lu, piv = scila.lu_factor(A)
     mid2 = time.perf_counter()
     x = scila.lu_solve((lu, piv), b)
     end2 = time.perf_counter()

     factor_time = mid2 - start2
     solve_time = end2 - mid2
     total_time = end2 - start2
     
     return x, factor_time, solve_time, total_time

def QR_solve(A,b):
     Q,R = scila.qr(A)
     Qb = np.dot(Q.T,b)
     x_qr = scila.solve(R, Qb)
     test_qr = np.matmul(A, x_qr)
     r_qr = la.norm(test_qr - b)
     print("QR:", r_qr)

def normal(A,b):
     A_T = A.T
     ATA = np.matmul(A_T, A)
     ATb = np.dot(A_T, b)
     inverse = inv(ATA)
     x = np.dot(inverse, ATb)
     print("Normal:", x)
          
  
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       
