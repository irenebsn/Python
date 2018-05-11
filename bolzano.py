from random import randint
from math import sin
#calcular f(x)=sen(x)-x^2-5X en un trozo (-10,-1) con el teorema de bolzano
a=-10
b=-1
m=(a+b)/2
tol=0.0000000001
#f(a)= sen(x)-x**2- 5*x

def funci(a):
    f1= (sin(a))-(a)**2-5*(a)
    return f1

while (b-a)>tol:
    m=(a+b)/2
    funci(m)
    if funci(m)>0:
        b=m
    elif funci(m)<0:
        a=m
    funci(a)
    print(a,b)


    





  

  




