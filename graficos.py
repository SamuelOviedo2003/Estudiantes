
import matplotlib as plt
import metodosOrdenar as mo
from dato import *
import datos as das
from generar import *
from redesNeuronalesActual import *
import ubicacion_grafica 

# metodo utlizado para conventir los datos y despues organizarlos

def inginieria_inversa(muestra, resultado):
    # Como primera parte se asigana el porcentaje correspondiente a cada estudiante
    # hay que resolver el problema de separar los datos, los registros que se utilizaron para la listacompleta y los registros utilizados para los desertores
    i = 0
    lista_final = []
    
    
    for item in muestra:
        item["porcentaje"] = resultado[i]
        i+=1
    
    # ii=1                                          #####AQUI IMPRIME EL ARREGLO CON EL POCENTAJE ACTUALIZADO
    # for item in muestra:                      
    #     print(f'[{ii}] : {item}')
    #     ii += 1
        
    
    #Despues de tener los registros completos, se pregunta por el departamento por el que se quiere ver la grafica
    dep = str(input('Departamento a analizar: '))
    #Los metodos utilizados aqui se explican en ubicacion_grafica.py
    muestra0 = ubicacion_grafica.retorno_lista(dep,ubicacion_grafica.agrupacion_dep(muestra, dep)) 
    
    #por ultimo se convierte cada dato ya clasificado por el departamento a la clase de dato, para asi poder utlizar el ordenamiento
    for item in muestra0:
        muestra_final = das.anadirDatos(item)
        lista_final.append(muestra_final)
    listaQ = mo.QuickSort(lista_final)
    return listaQ


# Metodo utilizado para la busqueda de la edad y asi poder clasificar en una rango de edad, cada dato
def busqueda(lista_ordenada):
    r1 = []
    r2 = []
    
    #La clasificacion se hace de acuerdo a si tiene maximo 17 o si es mayor de  17
    #El metodo funciona buscando en una sola cadena de str en que lugar se encuentra los numeros de la edad, para posteriormente convertirlo y comparar
    #por ultimo se clasifica y se guarda en un arreglo el porcentaje de ese registro analizado, fuciona basicamente igual en los dos, solo cambia la comparacion de edad 
    for k in lista_ordenada:
        numero = k[0].find(']')
        buscador = k[0][numero-2:numero]
        if int(buscador) <= 17:
            numero1 = k[0].rfind(']')
            numero2 = k[0].rfind(':') + 1
            buscador = k[0][numero2:numero1]
            r1.append(float(buscador))
    
    for k in lista_ordenada:
        numero = k[0].find(']')
        buscador = k[0][numero-2:numero]
        if int(buscador) > 17:
            numero1 = k[0].rfind(']')
            numero2 = k[0].rfind(':') + 1
            buscador = k[0][numero2:numero1]
            r2.append(float(buscador))
    return ([r1,r2])


#Despues de obtener los porcentaje se promedian y retorna el procenta promedio
#Promedio 1, se promedia el procentaje de hasta 17
#Promedio 2, se promedia el procentaje de mas 17
def PromedioPorcentajes1(arreglo):
    media  = 0
    for elem in arreglo[0]:
        media += elem
    mediaT = media / len(arreglo[0])
    return (mediaT *100)


def PromedioPorcentajes2(arreglo):
    media  = 0
    for elem in arreglo[1]:
        media += elem
    mediaT = media / len(arreglo[1])
    return (mediaT *100)

#En este ultimo metodo se pasa el arreglo obtenido en la funcion busqueda, y se ultiza junto con las funciones de promediar
#Para posteriormente invocar los metodos de matplotlib y graficar 

def grafica_definitiva(arreglo):
    rangoEdad = ['Hasta 17', 'Más 17']
    porcentanjes = [PromedioPorcentajes1(arreglo),PromedioPorcentajes2(arreglo)]
    plt.bar(rangoEdad, porcentanjes)
    plt.show()




# #basicamente lo mismo que en el main
# cantidad  = 100
# muestra = generarDatos(cantidad)

# a = muestra
# b = muestra
# #b1=b.pop(["deserción"] !=0)



# i = 1
# for item in b:
#     print(f'[{i}] : {item}')
#     i += 1




# b1=[]
# for item in b:
#     if item["desercion"]==0:
#         b1.append(item)
        



# ordenado=ordenandoDatosNecesarios(a)
# ordenadoCompleto=ordenado[0]
# ordenadoDesertor=ordenado[1]


# #Aqui calcula el porcentaje de cada estudiante que se graduen de la universidad, (solo están los estudiantes que se graduaron)
# resultado1 = entrenandoMaquinaCompleto(ordenadoCompleto)

# #Aqui calcula el porcentaje de cada estudiante que vuelva al colegio, (solo están los estudiantes que desertaron)
# resultado2 = entrenandoMaquinaDesertores(ordenadoDesertor)

# #----------------------------------------------------------


# #invocacion de los metodos anteriores
# arreglo_definitivo = busqueda(inginieria_inversa(b1, resultado1)) 
# grafica_definitiva(arreglo_definitivo)
