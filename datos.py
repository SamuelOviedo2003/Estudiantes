from dato import *

def anadirDatos(muestra):
  lista = []
  ObjetoDato = Dato(muestra)
  print(ObjetoDato.__str__())
  lista.append(ObjetoDato.__str__())
  return lista

