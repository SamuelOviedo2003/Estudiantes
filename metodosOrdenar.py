from re import L, T
import time

from datos import generarDatos


#Algoritmos de ordenamiento hechos con edison en clase, se utiliza el quick sort para el ordenamiento

def burbuja(lista):
    for i in range(len(lista)):
        for j in range (len(lista)):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def QuickSort(datos):
    if len(datos)<= 1:
        return datos
    pivote = datos[len(datos)//2]
    izq = [x for x in datos if x < pivote]
    centro = [x for x in datos if x == pivote]
    der  = [x for x in datos if x > pivote]
    return QuickSort(izq) + centro + QuickSort(der)



def MergeSort(datos):
    if len(datos) <= 1:
        return datos
    if len(datos) == 2:
        return sorted(datos)
    mitad = len(datos)  // 2
    return op_Merge(MergeSort(datos[:mitad]), MergeSort(datos[mitad:])) 


def op_Merge(datosX, datosY):
    indA = indB = 0
    out = []
    while indA < len(datosX) and indB < len(datosY):
        if datosX[indA] < datosY[indB]:
            out.append(datosX[indA])
            indA+= 1
        else:
            out.append(datosY[indB])
            indB+= 1
            
    out += datosX[indA:] + datosY[indB:]
    return out


def pythonSort(datos):
    return sorted(datos)

def pedirDatos():
    c = int(input("Cantidad de registros totales a analizar: "))
    e = int(input("Exponencial de crecimiento: "))
    t = (c, e)
    return t

def recoleccionDatos(func, tupla):
    n = 1
    ListaDeListas = []
    listaA1 = []
    listaA2 = []
    
    while n <= tupla[0]:
        muestra = generarDatos(n)
        inicio = time.time()
        func(muestra)
        fin = time.time()
        listaA1.append(fin-inicio)
        listaA2.append(n)
        n = n * tupla[1]
    
    ListaDeListas.append(listaA1)
    ListaDeListas.append(listaA2)
    print(ListaDeListas)
    return ListaDeListas

