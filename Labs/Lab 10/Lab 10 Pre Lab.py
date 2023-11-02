import numpy as np

def driver():


    p = eval_legendre(5, 0.5)

    print('p vector', p)


def eval_legendre(n,x):

    p = [1,x]

    for i in range(2,n+2):
        term = (1/i)*((2*(i-1)+1)*x*p[i-1] - (i-1)*p[i-2])
        p.append(term)

    return p

driver()
