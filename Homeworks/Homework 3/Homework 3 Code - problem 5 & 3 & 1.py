Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Problem 1 (c)

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example.py
Traceback (most recent call last):
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example.py", line 82, in <module>
    driver()
  File "C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example.py", line 17, in driver
    [astar,ier] = bisection(f,a,b,tol)
ValueError: too many values to unpack (expected 2)

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example.py
the approximate root is 0.8878622129559517
the error message reads: 0
f(astar) = 1.8960828462866175e-09
the number of iterations is:  27
# Problem 3 (b)

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example - Copy.py
the approximate root is 1.378662109375
the error message reads: 0
f(astar) = -0.0009021193400258198
the number of iterations is:  11
# Problem 5 (a)
x = np.linspace(-10,10,100)
y = []
for i in x:
    y.append(i - 4*np.sin(2*i) - 3)

    
zeros = []
for i in range(len(y)):
    if y[i] == 0:
        zeros.append(x[i])

        
plt.plot(x,y)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    plt.plot(x,y)
NameError: name 'plt' is not defined
import matplotlib.pyplot as plt
plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x0000020EE4C874D0>]
for i in zeros:
    plt.plot(i,0, 'x')

    
plt.show()
zeros
[]
y
[-9.34821899708949, -10.081967932787547, -11.25310302406407, -12.640491542286886, -13.988175338414296, -15.046590306073583, -15.612756148938624, -15.562964298115668, -14.872699922077828, -13.620589791567154, -11.97574023587488, -10.170504284178126, -8.463063567529598, -7.095850786559497, -6.2565083846410925, -6.047670636112709, -6.470435437672034, -7.424187503251692, -8.72280143504753, -10.124615330498903, -11.371347979914173, -12.229692434898299, -12.528887725375197, -12.188218181362272, -11.230011872719915, -9.776044900030044, -8.027930589077334, -6.234651710200553, -4.6524643291852845, -3.5036303677162945, -2.9406245758494927, -3.0215800204487313, -3.7009263445566627, -4.8367284110484565, -6.213543516462169, -7.57711625261638, -8.675323760548379, -9.298777559036523, -9.314543435149174, -8.687549150552682, -7.486232469669467, -5.871519952053454, -4.070911362655, -2.3418431427756192, -0.9302308830189121, -0.0308671123616171, 0.24394806236962863, -0.11750825063857118, -1.024493875394442, -2.298414674919364, -3.701585325080636, -4.975506124605558, -5.882491749361429, -6.243948062369629, -5.969132887638388, -5.069769116981088, -3.6581568572243808, -1.9290886373449998, -0.1284800479465611, 1.486232469669467, 2.687549150552682, 3.314543435149174, 3.298777559036525, 2.675323760548382, 1.5771162526163804, 0.21354351646216818, -1.163271588951549, -2.2990736554433333, -2.978419979551267, -3.0593754241505073, -2.4963696322837055, -1.3475356708147217, 0.23465171020054587, 2.027930589077334, 3.776044900030045, 5.23001187271991, 6.188218181362268, 6.528887725375197, 6.229692434898299, 5.371347979914178, 4.124615330498898, 2.7228014350475283, 1.4241875032517015, 0.47043543767203433, 0.047670636112709275, 0.2565083846410974, 1.095850786559497, 2.463063567529585, 4.170504284178134, 5.975740235874881, 7.6205897915671414, 8.872699922077828, 9.562964298115665, 9.61275614893862, 9.046590306073583, 7.988175338414306, 6.640491542286886, 5.253103024064069, 4.0819679327875384, 3.3482189970894893]
x = np.linspace(-10,10,1000)
y = []
x = np.linspace(-6*np.pi,6*np.pi,np.pi/100)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x = np.linspace(-6*np.pi,6*np.pi,np.pi/100)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\core\function_base.py", line 122, in linspace
    num = operator.index(num)
TypeError: 'float' object cannot be interpreted as an integer
x = np.linspace(-6*np.pi,6*np.pi,pi)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x = np.linspace(-6*np.pi,6*np.pi,pi)
NameError: name 'pi' is not defined. Did you mean: 'i'?
x = np.linspace(-6*np.pi,6*np.pi,np.pi)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x = np.linspace(-6*np.pi,6*np.pi,np.pi)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\core\function_base.py", line 122, in linspace
    num = operator.index(num)
TypeError: 'float' object cannot be interpreted as an integer
x = np.linspace((-6)*np.pi,6*np.pi,np.pi)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    x = np.linspace((-6)*np.pi,6*np.pi,np.pi)
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\numpy\core\function_base.py", line 122, in linspace
    num = operator.index(num)
TypeError: 'float' object cannot be interpreted as an integer
x = np.linspace(np.pi,2*np.pi,1)
x = np.arange(-6*np.pi, 6*np.pi, np.pi/100)
y = []
for i in x:
    y.append(i - 4*np.sin(2*i) - 3)

    
y

# use the bisection method to find the roots
zeros =[]
for i in range(len(y)-1):
    if y[i]*y[(i+1)] < 0:
        avg = 0.5*(x[i] + x[(i+1)])
        zeros.append(avg)

        
zeros
[-0.8953539062721774, -0.5497787143772825, 1.7435839227433831, 3.157300616858862, 4.508185457902542]
plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x0000020EE6A7F910>]
for i in zeros:
    plt.plot(i,0, 'x')

    
[<matplotlib.lines.Line2D object at 0x0000020EE6A74790>]
[<matplotlib.lines.Line2D object at 0x0000020EE6A90710>]
[<matplotlib.lines.Line2D object at 0x0000020EE6A91690>]
[<matplotlib.lines.Line2D object at 0x0000020EE6A922D0>]
[<matplotlib.lines.Line2D object at 0x0000020EE6A91E10>]
plt.show()
# there are 5 zeros for this function
# use bisection method to find the zeros to the given tolerance

================================ RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example - Copy.py ================================
the approximate root is 1.7320695021771826
the error message reads: 0
f(astar) = 2.884927852164765e-10
the number of iterations is:  34

================================ RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example - Copy.py ================================
the approximate root is 3.16182648652466
the error message reads: 0
f(astar) = 1.9082291302652266e-10
the number of iterations is:  33

================================ RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example - Copy.py ================================
the approximate root is 4.517789514211472
the error message reads: 0
f(astar) = 2.641429297511877e-10
the number of iterations is:  33

================================ RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example - Copy.py ================================
the approximate root is -0.5444424007320776
the error message reads: 0
f(astar) = 1.3912604401866702e-10
the number of iterations is:  32

================================ RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\bisection_example - Copy.py ================================
the approximate root is -0.8983565815724431
the error message reads: 0
f(astar) = -7.498934806449142e-11
the number of iterations is:  31
f1 = lambda x: -np.sin(2*x) + 5*x*0.25 - 0.75
iterations = []
# Problem 5(b)

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py
the approximate fixed point is: -0.544442400663504
f1(xstar): -0.5444424006751432
Error message reads: 0

===================================== RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py ====================================
the approximate fixed point is: -1.935899898395806e+97
f1(xstar): -2.4198748729947575e+97
Error message reads: 1

===================================== RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py ====================================
the approximate fixed point is: -0.5444424007083105
f1(xstar): -0.544442400689618
Error message reads: 0

===================================== RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py ====================================
the approximate fixed point is: 3.1618264865177657
f1(xstar): 3.1618264865775254
Error message reads: 0

===================================== RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py ====================================
the approximate fixed point is: 1005052065.3599
f1(xstar): 1256315081.1587708
Error message reads: 1

===================================== RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py ====================================
the approximate fixed point is: 151523183.30816656
f1(xstar): 189403977.39088857
Error message reads: 1

===================================== RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py ====================================
the approximate fixed point is: -62462281512.63856
f1(xstar): -78077851891.13457
Error message reads: 1

= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py
the approximate fixed point is: -0.5444424006609242
f1(xstar): -0.5444424006743097
Error message reads: 0
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py
the approximate fixed point is: 3.161826486515382
f1(xstar): 3.1618264865793093
Error message reads: 0
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py
the approximate fixed point is: 3.161826486515382
f1(xstar): 3.1618264865793093
Error message reads: 0
>>> 
= RESTART: C:\Users\cambr\.ssh\APPM-4600\Homeworks\Homework 3\fixedpt_example.py
the approximate fixed point is: -0.5444424006609242
f1(xstar): -0.5444424006743097
Error message reads: 0
