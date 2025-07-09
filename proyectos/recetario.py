
recetario = {}

def agregar_receta(nombre, ingredientes, instrucciones): #Lo que se encuentra dentro del parentesis, corresponden a
    # los agurmentos de la funciòn, 
#
  """Agrega una nueva receta al recetario."""
  recetario[nombre] = {
      'ingredientes': ingredientes,
      'instrucciones': instrucciones
  }
  
