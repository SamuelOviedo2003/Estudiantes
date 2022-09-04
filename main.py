

from dato import *
from datos import *
from generar import *
from redesNeuronalesActual import *


def prueba(cantidad):
    muestra = generarDatos(cantidad)
    i = 1
    for item in muestra:
        print(f'[{i}] : {item}')
        i += 1
    ordenado=ordenandoDatosNecesarios(muestra)
    ordenadoCompleto=ordenado[0]
    ordenadoDesertor=ordenado[1]
    
    
    #Aqui calcula el porcentaje de cada estudiante que se graduen de la universidad, (solo están los estudiantes que se graduaron)
    entrenandoMaquinaCompleto(ordenadoCompleto)
    
    #Aqui calcula el porcentaje de cada estudiante que vuelva al colegio, (solo están los estudiantes que desertaron)
    entrenandoMaquinaDesertores(ordenadoDesertor)



if __name__ == "__main__":
    print("-"*50)
    print("Generar Conjunto de datos. ")
    prueba(int(input("Cantidad de datos a generar? ")))
    print("-"*50)



