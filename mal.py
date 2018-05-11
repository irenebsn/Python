#! /usr/bin/env python
# -*- coding: utf-8 -*-
import random
digitos = ('0','1','2','3','4','5','6','7','8','9')
codigo = ''
for i in range(4):
    candidato = random.choice(digitos)
# vamos eligiendo digitos no repetidos*
    while candidato in codigo:
        candidato = random.choice(digitos)
        codigo = codigo + candidato
print ("Bienvenido/a al Mastermind!")
print ("Tienes que adivinar un numero de", 4, "cifras distintas")
propuesta = input("¿Que codigo propones?: ")
intentos = 1
while propuesta != codigo:
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0
#comprobacion de la respuesta
for i in range(4):
    if propuesta[i] == codigo[i]:
        aciertos = aciertos + 1
    elif propuesta[i] in codigo:
        coincidencias = coincidencias + 1
    print ("Tu propuesta (", propuesta, ") tiene", aciertos, \
          "aciertos y ", coincidencias, "coincidencias.")
    # pedimos siguiente propuesta*
    propuesta = input("Propón otro codigo: ")
 
    print ("Felicitaciones! Adivinaste el codigo en", intentos, "intentos.")
