Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Steffenson's Method

def driver():







return


def steffensons(function, p0, tol):

    points = np.zeros((Nmax,1))
    count = 0

    while (count < Nmax):
        a = p0
        b = function(p0)
        c = g(b)
        p1 = a - ((b-a)**2 / (c-2*b + a))
        points[count] = p1
        
        count = count + 1

        if (abs(p1 - p0) < tol):
            xstar = p1
            ier = 0
            points = points[points != 0]
            return [xstar, ier, points]
        p0 = p1

        xstar = p1
        ier = 1
        points = points[points !=0]
        return [xstar,ier, points]

