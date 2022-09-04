import random


def AllRandom(cant: int):
    lista2 = []
    for i in range(cant):
        A = [
        (random.randint(0,1)),
        (random.randint(1,32)),	
        (random.randint(1,11))	
        ]
        lista2.append(A)
    #print (lista2)
    return lista2


#Valor normalizado = (Valor - Característica mínima)/(Característica máxima - Característica mínima)

def DatosPruebaRedCompleto(lista2):
    decF = []
    for i in range(len(lista2)):
        dec = [((lista2[i][2]+lista2[i][1]+lista2[i][0])*2.27)/100]
        decF.append(dec)
        
    #print (decF)
    return decF

def DatosPruebaRedDesertaron(lista2):
    decF=[]
    for i in range(len(lista2)):
        dec=[((lista2[i][2]+lista2[i][1]+lista2[i][0])*2.94)/100] #formula de los que desertaron (nose cual formula)
        decF.append(dec)
    return decF 
