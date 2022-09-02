# muestra tomada de personas que maximo se hayan graduado en 2022
import random

# probabilidad de 75 % de estar cursando actualmente,aparte nos genera en que grado academico esta


def anos_Cursados():
    num = random.randint(1, 100)
    anos_Cursados = 0
    if num in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75):
        anos_Cursados = random.randint(1, 11)
    return anos_Cursados
# probabilidad de 30% de perder una materia ,aparte nos genera cuantos años reprobo


def reprobados():
    num = random.randint(1, 100)
    reprobados = 0
    if num in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30):
        reprobados = random.randint(1, 11)
    return reprobados
# a la edad en el mejor de los casos se le suman los grados reprobados, si esta estudiando actualmente este predomina sobre los años reprobados
# y genera una lista mas pequeña o mas grande con la edad en que cursa


def edad(reprobados, anos_Actuales):
    edad_ingresar = 7
    edad_salir = 18
    if reprobados > 0:
        edad_salir = edad_salir+reprobados
    if anos_Actuales > 0:
        edad_salir = edad_ingresar+anos_Actuales+reprobados
    edad = []
    for i in range(edad_ingresar, edad_salir):
        edad.append(i)
    return edad

# en un rango de 1980 y 2000 ,porque en el peor de los casos puede haber ingresado en 2000 perder 11 veces un año lo que nos da 2022


def anos_Estudio(edad):
    anos_Estudio = []
    ano_Ingreso = random.randint(1980, 2000)
    for i in range(len(edad)):
        anos_Estudio.append(i+ano_Ingreso)
    return anos_Estudio

# comprueba con el tamaño de la lista si cursa actualmente o no ,en el caso afirmativo llena los grados academicos hasta el grado en que deserto
# en caso contrario usa el numero de reprobados y escoge un grado aleatorio el cual fue perdido


def grados(edad_list, reprobados):
    anos = []
    if reprobados > 0 and len(edad_list) > 11:
        for i in range(1, len(edad_list)-reprobados+1):
            anos.append(str(i)+"°")
        for i in range(reprobados):
            ano_repetido = random.choice(anos)
            indice = anos.index(ano_repetido)
            anos.insert(indice, ano_repetido)
    if len(edad_list) <= 11:
        for i in range(1, len(edad_list)+1):
            anos.append(str(i)+"°")
    return anos




