from generar import *

class Dato:
    def __init__(self):
        dato = generarDato()
        self.nombre = dato['nombre']
        self.sexo = dato['sexo']
        self.edad = dato['edad']
        self.departamento= dato['departamento']
        self.municipio = dato['municipio']
        self.grados_Academico = dato['grados_Academico']
        self.desercion = dato['desercion']
        self.anos_Estudio = dato['anos_Estudio']
        self.ano_Reprobados = dato['ano_Reprobados']

#==
    def __eq__ (self, __o: object) -> bool:
        return (self.edad == __o.edad) #and (self.sexo == __o.sexo)

#<
    def __lt__ (self, __o: object) -> bool:
        return (self.edad< __o.edad) #and (self.sexo == __o.sexo)

#<=
    def __le__ (self, __o: object) -> bool:
        return (self.edad <= __o.edad) #and (self.sexo == __o.sexo)

#>
    def __gt__ (self, __o: object) -> bool:
        return (self.edad > __o.edad) #and (self.sexo == __o.sexo)

#>=
    def __ge__ (self, __o: object) -> bool:
        return (self.edad >= __o.edad) #and (self.sexo == __o.sexo)

#!=
    def __ne__ (self, __o: object) -> bool:
        return (self.edad != __o.edad) #or (self.sexo != __o.sexo)

    def __str__(self):
        return f'Objeto Dato=[nombre: {self.nombre}, edad: {self.edad}, sexo:{self.sexo},departamento:{self.departamento},municipio:{self.municipio},nivel_Educativo:{self.nivel_Educativo},desertor:{self.desertor}]'
