import random

# probabilidad de 30 % de ser desertor,aparte nos genera en que grado academico abandono
def desercion():
    num = random.randint(1, 100)
    desercion = 0
    if num in (1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30):
        desercion = random.randint(0, 11)
    return desercion


# probabilidad de 35% de perder una materia ,aparte nos genera cuantos años reprobo
def reprobados():
    num = random.randint(1, 100)
    reprobados = 0
    if num in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35):
        reprobados = random.randint(1, 11)
    return reprobados
# a la edad en el mejor de los casos se le suman los grados reprobados, si hay desercion este predomina sobre los años reprobados 
#y genera una lista mas pequeña con la edad en que deserto


def edad(reprobados, desercion):
    edad_ingresar = 7
    edad_salir = 18
    if reprobados > 0:
        edad_salir = edad_salir+reprobados
    if desercion > 0:
        edad_salir = edad_ingresar+desercion
    edad = []
    for i in range(edad_ingresar, edad_salir):
        edad.append(i)
    return edad

#en un rango de 1980 y 2000 ,porque en el peor de los casos puede haber ingresado en 2000 perder 11 veces un año lo que nos da 2022 
def anos_Estudio(edad):
    anos_Estudio = []
    ano_Ingreso = random.randint(1980, 2000)
    for i in range(len(edad)):
        anos_Estudio.append(i+ano_Ingreso)
    return anos_Estudio

#comprueba con el tamaño de la lista si es desertor o no ,en el caso afirmativo llena los grados academicos hasta el grado en que deserto
#en caso contrario usa el numero de reprobados y escoge un grado aleatorio el cual fue perdido 
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

