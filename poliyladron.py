#Paisaje
import random
import turtle

window = turtle.Screen()
flecha = turtle.Turtle()
flecha.penup()
policia = turtle.Turtle()
ladron = turtle.Turtle()
captura = False
coger = True
policia.shape('turtle')
ladron.pencolor('#16ECFC')
ladron.pensize(0)
ladron.shape('turtle')


#Diseño
def cielo(longitud):
    flecha.speed(20)
    flecha.heading()
    flecha.begin_fill()
    flecha.color('black','#16ECFC')
    flecha.goto(-410,400)
    flecha.pendown()
    for i in range(4):
        flecha.forward(longitud)
        flecha.right(90)
    flecha.end_fill()
    flecha.penup()
    flecha.home()

def marco(longitud):
    flecha.speed(20)
    flecha.heading()
    flecha.begin_fill()
    flecha.color('black','#04F977')
    flecha.goto(-1000,1000)
    flecha.pendown()
    for i in range(4):
        flecha.forward(longitud)
        flecha.right(90)
    flecha.end_fill()
    flecha.penup()
    flecha.home()
marco(2000)
cielo(790)
policia.penup()
policia.goto(-300,300)
policia.pendown()
ladron.penup()
ladron.goto(300,-300)
ladron.pendown()

def muere(longitud):
    ladron.speed(10)
    ladron.pendown()
    ladron.heading()
    ladron.begin_fill()
    ladron.color('black','#F7F707')
    for i in range(5):
        ladron.right(144)
        ladron.forward(longitud)
    ladron.end_fill()
    ladron.penup()
    ladron.home()

#Policia
policia.begin_fill()
policia.color('#16ECFC','#F91704')
def arriba():
    policia.setheading(90)
    policia.forward(10)

def abajo():
    policia.setheading(270)
    policia.forward(10)


def izquierda():
    policia.setheading(180)
    policia.forward(10)

    
def derecha():
    policia.setheading(0)
    policia.forward(10)
policia.end_fill()


#Oido de pyton
    
window.listen()
window.onkeypress(arriba,'Up')
window.onkeypress(abajo,'Down')
window.onkeypress(derecha,'Right')
window.onkeypress(izquierda,'Left')

#Ladron
while captura == False:
    ladron.speed(2)
    ladron.goto(random.randrange(-90,90),random.randrange(-90,90))
    # distancia del ladron al policia
    distancia= ladron.pos()-policia.pos()
    modulo=(distancia[0]**2+distancia[1]**2)**.5
    print(modulo)
    if modulo<30:
        captura=True
            
    #distancia del ladron al policia
    ladron.circle(random.randrange(-90,90),random.randrange(-90,90))
    distancia= ladron.pos()-policia.pos()
    modulo=(distancia[0]**2+distancia[1]**2)**.5
    print(modulo)
    if modulo<30:
        captura=True

if captura==True:
    ladron.speed(10)
    ladron.pendown()
    ladron.heading()
    ladron.begin_fill()
    ladron.color('black','#F7F707')
    for i in range(5):
        ladron.right(144)
        ladron.forward(200)
    ladron.end_fill()
    ladron.penup()
    ladron.goto(300,-300)
    policia.goto(-300,300)
    
        
            

    


