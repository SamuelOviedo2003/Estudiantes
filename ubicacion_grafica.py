#En esta parte de hace una agrupacion por listas para cada departamento
#se pasa como argumento la lista con los registros ultilizados

def agrupacion_dep(lista):
    Santander = []
    Boyaca = []
    casanare = [] 
    Cudinamarca= []
    Huila= []
    Sucre = []
    NorteDeSantander = []
    Caldas = []
    Tolima = []
    Meta= []
    Risaralda = [] 
    Cesar = []
    Quindio= []
    Atlantico= []
    Cordoba = []
    Arauca = []
    Cauca = []
    Antioquia = []
    Narino = [] 
    Bolivar = []
    ValleDelCauca  = [] 
    Magdalena  = []
    Putumayo = []
    Caqueta  = []
    Choco= []
    LaGuajira  = []
    Amazonas = [] 
    Guania  = []
    Guaviare  = []
    Vichada  = []
    Vaupes  = []
    SanAndresProvidenciaYSantaCatalina = []
    for item in lista:
        if item["departamento"] == "Santander":
            Santander.append(item)
        elif item["departamento"] == "Boyacá":
            Boyaca.append(item)
        elif item["departamento"] == "Casanare":
            casanare.append(item)
        elif item["departamento"] == "Cundinamarca":
            Cudinamarca.append(item)
        elif item["departamento"] == "Huila":
            Huila.append(item)
        elif item["departamento"] == "Sucre":
            Sucre.append(item)
        elif item["departamento"] == "Norte de Santander":
            NorteDeSantander.append(item)
        elif item["departamento"] == "Caldas":
            Caldas.append(item)
        elif item["departamento"] == "Tolima":
            Tolima.append(item)
        elif item["departamento"] == "Meta":
            Meta.append(item)
        elif item["departamento"] == "Risaralda":
            Risaralda.append(item)
        elif item["departamento"] == "Cesar":
            Cesar.append(item)
        elif item["departamento"] == "Quindío":
            Quindio.append(item)
        elif item["departamento"] == "Atlántico":
            Atlantico.append(item)
        elif item["departamento"] == "Córdoba":
            Cordoba.append(item)
        elif item["departamento"] == "Arauca":
            Arauca.append(item)
        elif item["departamento"] == "Cauca":
            Cauca.append(item)
        elif item["departamento"] == "Antioquia":
            Antioquia.append(item)
        elif item["departamento"] == "Nariño":
            Narino.append(item)
        elif item["departamento"] == "Bolívar":
            Bolivar.append(item)
        elif item["departamento"] == "Valle del Cauca":
            ValleDelCauca.append(item)
        elif item["departamento"] == "Magdalena":
            Magdalena.append(item)
        elif item["departamento"] == "Putumayo":
            Putumayo.append(item)
        elif item["departamento"] == "Caquetá":
            Caqueta.append(item)
        elif item["departamento"] == "Chocó":
            Choco.append(item)
        elif item["departamento"] == "La Guajira":
            LaGuajira.append(item)
        elif item["departamento"] == "Amazonas":
            Amazonas.append(item)
        elif item["departamento"] == "Guanía":
            Guania.append(item)
        elif item["departamento"] == "Guaviare":
            Guaviare.append(item)
        elif item["departamento"] == "Vichada":
            Vichada.append(item)
        elif item["departamento"] == "Vaupés":
            Vaupes.append(item)
        elif item["departamento"] == "San Andrés,Providencia y Santa Catalina":
            SanAndresProvidenciaYSantaCatalina.append(item)
    
    return ([
    Santander,
    Boyaca ,
    casanare,
    Cudinamarca,
    Huila ,
    Sucre,
    NorteDeSantander,
    Caldas ,
    Tolima ,
    Meta,
    Risaralda , 
    Cesar ,
    Quindio,
    Atlantico,
    Cordoba ,
    Arauca ,
    Cauca ,
    Antioquia ,
    Narino,
    Bolivar ,
    ValleDelCauca  , 
    Magdalena  ,
    Putumayo ,
    Caqueta  ,
    Choco,
    LaGuajira  ,
    Amazonas , 
    Guania  ,
    Guaviare  ,
    Vichada  ,
    Vaupes  ,
    SanAndresProvidenciaYSantaCatalina
    ])
    #---------------------------

#Aqui se selecciona la lista que se valla a utilizar para proceder con la grafica de acuerdo con la seleccion del departamento escogida por el usuario

def retorno_lista(dep,  lista):
    
    if dep == 'Sanatader':
        return lista[0]
    elif dep == 'Boyaca':
        return lista[1]
    elif dep == 'casanare':
        return lista[2]
    elif dep == 'Cundinamarca':
        return lista[3]
    elif dep == 'Huila':
        return lista[4]
    elif dep == 'Sucre':
        return lista[5]
    elif dep == 'Norte de Santander':
        return lista[6]
    elif dep == 'Caldas':
        return lista[7]
    elif dep == 'Tolima':
        return lista[8]
    elif dep == 'Meta':
        return lista[9]
    elif dep == 'Risaralda':
        return lista[10]
    elif dep == 'Cesar':
        return lista[11]
    elif dep == 'Quindio':
        return lista[12]
    elif dep == 'Atlantico':
        return lista[13]
    elif dep == 'Cordoba':
        return lista[14]
    elif dep == 'Arauca':
        return lista[15]
    elif dep == 'Cauca':
        return lista[16]
    elif dep == 'Antioquia':
        return lista[17]
    elif dep == 'Nariño':
        return lista[18]
    elif dep == 'Bolivar':
        return lista[19]
    elif dep == 'Valle del cauca':
        return lista[20]
    elif dep == 'Magdalena':
        return lista[21]
    elif dep == 'Putumayo':
        return lista[22]
    elif dep == 'Caqueta':
        return lista[23]
    elif dep == 'Choco':
        return lista[24]
    elif dep == 'La Guajira':
        return lista[25]
    elif dep == 'Amazonas':
        return lista[26]    
    elif dep == 'Guania':
        return lista[27]
    elif dep == 'Guaviare':
        return lista[28]
    elif dep == 'Vichada':
        return lista[29]
    elif dep == 'Vaupes':
        return lista[30]
    elif dep == 'San Andrés,Providencia y Santa Catalina':
        return lista[31]
    else:
        return None
