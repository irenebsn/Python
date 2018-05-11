import random
#Saludo
nombre= input("¿Cual es tu nombre?")
print("Hola",nombre)
#Datos
intentos_realizados = 0
#vamos a elegir un numero de 4 cifras
numero_secreto= random.randrange(999,9999)+1
print(numero_secreto)
numero_secreto=str(numero_secreto)
#Adivina el numero 1-9999
numero_dado=' '
while numero_secreto !=numero_dado:
    aciertos=0
    coincidencias=0

    intentos_realizados= intentos_realizados+1
    numero_dado = input("Dime un numero de 4 digitos:")
    for i in numero_secreto:
        if i in numero_dado:
            aciertos += 1
    for j in range(4):
        if numero_secreto[j] == numero_dado[j]:
            coincidencias += 1     
    print("Vaya",nombre,"has tenido",coincidencias,"coincidencias y",aciertos,"aciertos.Te recomiento volver a jugar")
 elif numero_secreto = numero_dado:
     print(
    
# Concurso



