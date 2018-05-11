import random
ganamoustruos=0
ganasoldados=0

combates = int(input("¿Cuantos combates hago?"))
for i in range (combates):
    grande = random.randrange(20)+1
    mediano = random.randrange(12)+1
    moustruito = random.randrange(2)+1
    soldado1 = random.randrange(6)+1
    soldado2= random.randrange(6)+1
    soldado3= random.randrange(6)+1
    soldado4= random.randrange(6)+1
    soldado5= random.randrange(6)+1
    escudero= random.randrange(2)+1
    sumamoustruos= (grande + mediano + moustruito)
    sumasoldados=(soldado1+soldado2+soldado3+soldado4+soldado5+escudero)
    print(sumamoustruos,sumasoldados)
    if sumamoustruos>sumasoldados:
        ganamoustruos=ganamoustruos+1
    elif sumamoustruos<sumasoldados:
        ganasoldados=ganasoldados+1
    else:
        ganasoldados=ganasoldados+0.5
        ganamoustruos=ganamoustruos+0.5
    print(ganamoustruos, ganasoldados)
    
porcentaje_moustruos = ((ganamoustruos /combates )*100)
porcentaje_soldados = ((ganasoldados /combates)*100)
print ("El porcentaje de los moustruos:",porcentaje_moustruos)
print("El porcentaje de los soldados:", porcentaje_soldados)

