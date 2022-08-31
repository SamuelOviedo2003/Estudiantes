import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense

#Aqui lo que llevo basicamente hice una red neuronal ya entrenada de 3 entradas: [sexo,Departamento,AñosReprobado]
# -->Sexo(se representa con 0->hombre, 1->mujer)
# -->Departamento (se representa entre 1 y 32)
# -->Años reprobados( se representa entre 1 y 11)
#Y hay una salida el cual es como el porcentaje (en decimales) de deserción

#El porcentaje de veracidad de la red neuronal es apenas 16%, despues me encargo de mejorar eso

def sexoEdadAñosReprobados():
    datosPracticaEntrada=np.array([[1,7,10],[0,32,0],[0,1,0],[1,10,11],[1,23,5],[0,13,9]],"float32") 
    #hombre-mujer,departamento(1-32), añosReprobados(0-11)
    datosPracticaSalida=np.array([[0.95],[0.1],[0.05],[1],[0.5],[0.7]], "float32")
    return entrenandoMaquina(datosPracticaEntrada,datosPracticaSalida)

def entrenandoMaquina(datos,datosVerdad):
    n_entrada=len(datos[0]) #entran 3 datos 
    n_salida=1              #sale 1 dato
    n_nodos=50

    model=Sequential()
    model.add(Dense(n_nodos, input_dim=n_entrada, activation="relu"))
    model.add(Dense(n_salida, activation="sigmoid"))

    model.compile(loss='mean_squared_error',
                    optimizer='adam',
                    metrics=['binary_accuracy'])

    model.fit(datos, datosVerdad, epochs=2000, verbose=0)
    print("Modelo entrenado")
    scores = model.evaluate(datos, datosVerdad, verbose=0)
    print(f'Metrica del modelo: {model.metrics_names[1]}, con un valor de: {scores[1]*100}')


    #datosReales=np.array([[0,1,0],[1,32,10]], "float32")

    #resultado=model.predict(datosReales, verbose=0)
    #model.summary()
    #print(f' para la entrada: {datosReales[0]} -> {resultado[0]}')
    #print(f' para la entrada: {datosReales[1]} -> {resultado[1]}')
