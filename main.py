


from dato import *
from datos import *
from generar import *
from redesNeuronalesActual import *
from graficos import *


def prueba(cantidad):
    muestra = generarDatos(cantidad)
    i = 1
    for item in muestra:
        print(f'[{i}] : {item}')
        i += 1
    
    ordenado=ordenandoDatosNecesarios(muestra)      #Esto ordena el [0,25,2] etc.. (para poder sacar resultado en la red neuronal)
    ordenadoCompleto=ordenado[0]             
    ordenadoDesertor=ordenado[1]
    
    ordenadoDict=ordenandoDatosNecesariosDict(muestra)  #Esto clasifica por desertores y no desertores pero en el arreglo mismo
    ordenadoDesertor00=ordenadoDict[0]
    ordenadoDesertorNo00=ordenadoDict[1]
    
    
    
    
    #Aqui calcula el porcentaje de cada estudiante que se graduen de la universidad, (solo están los estudiantes que se graduaron)
    desertor0Red=entrenandoMaquinaCompleto(ordenadoCompleto)
    
    #Aqui calcula el porcentaje de cada estudiante que vuelva al colegio, (solo están los estudiantes que desertaron)
    desertorNo0Red=entrenandoMaquinaDesertores(ordenadoDesertor)
    #invocacion de los metodos anteriores
    arreglo_definitivoDesertores = busqueda(inginieria_inversa(ordenadoDesertor00,desertor0Red)) 
    grafica_definitiva(arreglo_definitivoDesertores)

    arreglo_definitivoNoDesertores = busqueda(inginieria_inversa(ordenadoDesertorNo00,desertorNo0Red)) 
    grafica_definitiva(arreglo_definitivoDesertores)


if __name__ == "__main__":
    print("-"*50)
    print("Generar Conjunto de datos. ")
    prueba(int(input("Cantidad de datos a generar? ")))
    print("-"*50)
    


