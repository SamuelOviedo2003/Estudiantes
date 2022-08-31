
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

def preparandoRed():
    sexoEdadAñosReprobados()



if __name__ == "__main__":
    preparandoRed() 
    print("-"*50)

    print("Generar Conjunto de datos. ")
    prueba(int(input("Cantidad de datos a generar? ")))
    print("-"*50)
