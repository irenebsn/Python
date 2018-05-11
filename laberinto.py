
#laberinto
import random
import turtle

window = turtle.Screen()
flecha = turtle.Turtle()


#teclado
def arriba():
    flecha.setheading(90)
    flecha.forward(10)

def abajo():
    flecha.setheading(270)
    flecha.forward(10)

def izquierda():
    flecha.setheading(180)
    flecha.forward(10)

def derecha():
    flecha.setheading(0)
    flecha.forward(10)

#Oido de pyton
    
window.listen()
window.onkeypress(arriba,'Up')
window.onkeypress(abajo,'Down')
window.onkeypress(derecha,'Right')
window.onkeypress(izquierda,'Left')


