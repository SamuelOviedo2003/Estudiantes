import random
import datos_Nombres
import datos_Ubicacion
import generar_Edad_Grado_Ano as gega


def generarDato():
    sexo = random.choice(['Masculino', 'Femenino'])
    if sexo == 'Masculino':
        nombre = random.choice(datos_Nombres.nombreHombre)
    else:
        nombre = random.choice(datos_Nombres.nombreMujer)
    reprobados= gega.reprobados()    
    desercion=gega.desercion()   
    edad = gega.edad(reprobados,desercion)
    grados=gega.grados(edad, reprobados)
    anos_Estudio=gega.anos_Estudio(edad)
    departamento = random.choice(list(datos_Ubicacion.departamentos.keys()))
    random_municipio = random.randint(0, len(datos_Ubicacion.departamentos[departamento])-1)
    municipio = datos_Ubicacion.departamentos[departamento][random_municipio]
    apellido1 = random.choice(datos_Nombres.apellidos)
    apellido2 = random.choice(datos_Nombres.apellidos)

    
    return {'nombre': nombre+" "+apellido1+" "+apellido2,   #[sexo,departamento,añosReprobados]
            'sexo': sexo,    #0 hombre, 1 Mujer
            'edad': edad,
            "departamento": departamento,
            "municipio": municipio,
            "grados_Academico": grados,
            "anos_Estudio":anos_Estudio,
            "desercion":desercion,
            "anos_Reprobados":reprobados,
            "porcentaje":0} #0-11
            


def generarDatos(cantidad):
    muestra = []
    if cantidad > 0:
        for item in range(cantidad):
            muestra.append(generarDato())
    return muestra




