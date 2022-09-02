import numpy as np
from keras.models import *
from keras.layers.core import *
import CojuntoDePrueba as cp


#Aqui lo que llevo basicamente hice una red neuronal ya entrenada de 3 entradas: [sexo,Departamento,AñosReprobado]
# -->Sexo(se representa con 0->hombre, 1->mujer)
# -->Departamento (se representa entre 1 y 32)
# -->Años reprobados( se representa entre 1 y 11)
#Y hay una salida el cual es como el porcentaje (en decimales) de deserción

#El porcentaje de veracidad de la red neuronal es apenas 12.5%, no he podido aumentar ese porcentaje de fiabilidad


def ordenandoDatosNecesarios(arreglo):
    arregloListo=[]
    for i in arreglo:
        arr1=[]
        if i["sexo"]=="Masculino":
            arr1.append(0)
        elif i["sexo"] =="Femenino":
            arr1.append(1)
        #________________________________________________________________
        if i["departamento"] == "Santander":
            arr1.append(1)
        elif i["departamento"] == "Boyacá":
            arr1.append(2)
        elif i["departamento"] == "Casanare":
            arr1.append(3)
        elif i["departamento"] == "Cundinamarca":
            arr1.append(4)
        elif i["departamento"] == "Huila":
            arr1.append(5)
        elif i["departamento"] == "Sucre":
            arr1.append(6)
        elif i["departamento"] == "Norte de Santander":
            arr1.append(7)
        elif i["departamento"] == "Caldas":
            arr1.append(8)
        elif i["departamento"] == "Tolima":
            arr1.append(9)
        elif i["departamento"] == "Meta":
            arr1.append(10)
        elif i["departamento"] == "Risaralda":
            arr1.append(11)
        elif i["departamento"] == "Cesar":
            arr1.append(12)
        elif i["departamento"] == "Quindío":
            arr1.append(13)
        elif i["departamento"] == "Atlántico":
            arr1.append(14)
        elif i["departamento"] == "Córdoba":
            arr1.append(15)
        elif i["departamento"] == "Arauca":
            arr1.append(16)
        elif i["departamento"] == "Cauca":
            arr1.append(17)
        elif i["departamento"] == "Antioquia":
            arr1.append(18)
        elif i["departamento"] == "Nariño":
            arr1.append(19)
        elif i["departamento"] == "Bolívar":
            arr1.append(20)
        elif i["departamento"] == "Valle del Cauca":
            arr1.append(21)
        elif i["departamento"] == "Magdalena":
            arr1.append(22)
        elif i["departamento"] == "Putumayo":
            arr1.append(23)
        elif i["departamento"] == "Caquetá":
            arr1.append(24)
        elif i["departamento"] == "Chocó":
            arr1.append(25)
        elif i["departamento"] == "La Guajira":
            arr1.append(26)
        elif i["departamento"] == "Amazonas":
            arr1.append(27)
        elif i["departamento"] == "Guanía":
            arr1.append(28)
        elif i["departamento"] == "Guaviare":
            arr1.append(29)
        elif i["departamento"] == "Vichada":
            arr1.append(30)
        elif i["departamento"] == "Vaupés":
            arr1.append(31)
        elif i["departamento"] == "San Andrés,Providencia y Santa Catalina":
            arr1.append(32)
        else:
            arr1.append(0000)
        
            
        #_______________________________________________________________
        
        arr1.append(i["anos_Reprobados"])
        
        #__________________________________________________________
        arregloListo.append(arr1)
    return (arregloListo)

cp1 = cp.AllRandom(24)

def entrenandoMaquina(datos):
    datosPracticaEntrada=np.array(cp1,"float32") 
    #hombre(0)-mujer(1)   ,departamento(1-32), añosReprobados(0-11)
    datosPracticaSalida=np.array(cp.DatosPruebaRed(cp1), "float32")
    
    n_entrada=len(datosPracticaEntrada[0]) #entran 3 datos 
    n_salida=1              #sale 1 dato
    n_nodos=32

    model=Sequential()
    model.add(Dense(n_nodos, input_dim=n_entrada, activation="relu"))
    model.add(Dense(n_salida, activation="sigmoid"))

    model.compile(loss='mean_squared_error',
                    optimizer='adam',
                    metrics=['categorical_accuracy'])
    model.fit(datosPracticaEntrada, datosPracticaSalida, epochs=1000, verbose=0)
    print("Modelo entrenado")
    scores = model.evaluate(datosPracticaEntrada, datosPracticaSalida, verbose=0)
    print(f'Metrica del modelo: {model.metrics_names[1]}, con un valor de: {scores[1]*100}')
    
    
    

    
    resultado=model.predict(datos, verbose=0)
    model.summary()
    
    print("Ha sido exitoso el proceso de resultado")
    
    for i in range(0,len(datos),1):
        print(datos[i],"->",resultado[i])




