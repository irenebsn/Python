# Voy a resolver la ecuacion de segundo grado
import sys
print("vamos a resolver una ecuacion de tipo ax^2+bx+c=0")
print("primero introduce los coeficientes")
while True:
    a= input('Introduce el valor del coeficiente de grado 2:')
    try:
        a=float (a)
        break
    except ValueError:
        print("No es un numero, debes añadir un numero")
while True:
    b= input('Introduce el valor del coeficiente de grado 1:')
    try:
        b=float (b)
        break
    except ValueError:
        print("No es un numero, debes añadir un numero")
while True:
    c= input('Introduce el valor del coeficiente d grado 0:')
    try:
        c=float (c)
        break
    except ValueError:
        print("No es un numero, debes añadir un numero")

#Calculo de variables auxiliares
discriminante = b**2- 4*a*c
print('el disciminante es')
print(discriminante)
if discriminante <0:
    print('no hay solucion')
elif discriminante >0:
    primera = (-b+(discriminante**.5))/(2*a)
    segunda = (-b-(discriminante**.5))/(2*a)
    print('las soluciones son:')
    print (primera)
    print (segunda)
else:
    solucion = (-b+(discriminante**.5))/(2*a)
    print ('la solucion es:')
    print (solucion)
 
