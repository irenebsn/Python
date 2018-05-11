from random import randint
#Saludo
nombre = input ("Hola, ¿me podrias decir tu nombre?")
#Se escribe la frase 
print(nombre,",")
frase= input("¿podrias decirme el refran que deseas que te adivinen?")
#frase= ("en abril aguas mil")
asci= randint(33,126)
#dividir la frase
frase = str (frase)
#print(frase)

#adivinar la frase
def mostrarTablero( letrasIncorrectas, letrasCorrectas, fraseSecreta):
   # print([len(letrasIncorrectas)])
    print()
    print('Letras incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end=' ')
    print()
    espaciosVacíos = '_' * len(fraseSecreta)
# completar los espacios vacíos con las letras adivinadas   
    for i in range(len(fraseSecreta)):
        if fraseSecreta[i] in letrasCorrectas:
            espaciosVacíos = espaciosVacíos[:i] + fraseSecreta[i] + espaciosVacíos[i+1:]
# mostrar la frase secreta con espacios entre cada letra
    for letra in espaciosVacíos:
        print(letra, end=' ')
    print()
    
def obtenerIntento(letrasProbadas):  
# Devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado sólo una letra, y no otra cosa.
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
           print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento
       
def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')

letrasIncorrectas = ''
letrasCorrectas = ''
fraseSecreta = frase
juegoTerminado = False

while True:
    mostrarTablero(letrasIncorrectas, letrasCorrectas, fraseSecreta)
    # Permite al jugador escribir una letra.
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)
    if intento in fraseSecreta:
            letrasCorrectas = letrasCorrectas + intento
        # Verifica si el jugador ha ganado.
            encontradoTodasLasLetras = True
            for i in range(len(fraseSecreta)):
                if fraseSecreta[i] not in letrasCorrectas:
                    encontradoTodasLasLetras = False
                    break
                if encontradoTodasLasLetras:
                    print('¡Sí! ¡Has acertado!')
                    juegoTerminado = True
            else:
                letrasIncorrectas = letrasIncorrectas + intento
            # Comprobar si el jugador ha agotado sus intentos y ha perdido.
                if len(letrasIncorrectas) == len(IMÁGENES_AHORCADO) - 1:
                    mostrarTablero(letrasIncorrectas, letrasCorrectas, fraseSecreta)
                    print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la frase era:' + fraseSecreta )     
                    juegoTerminado = True
                
            #Preguntar al jugador si quiere volver a jugar (pero sólo si el juego ha terminado).
                if juegoTerminado:
                    if jugarDeNuevo():
                        letrasIncorrectas = ''
                        letrasCorrectas = ''
                        juegoTerminado = False
                        fraseSecreta = frase
                    else:
                        break
    
