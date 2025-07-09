print("Hola, bienvenido a este menu de emergencia")
sentimiento = (input("¿Còmo te sientes hoy ?:     ") )

print(f"Entiendo que te sientes: {sentimiento}") # Mostramos lo que ingresó el usuario

def menu(): 
  
  print("\n--- Elige dentro de las siguientes opciones ---") # Separamos las opciones del menú

  print("1. ¡Triste!")
  print("2. ¡Feliz!")
  print("3. No lo puedo explicar....")




def triste(): 
  print("Te puedo recomendar una película de terror, así estarás asustado y no triste!! ")


def Feliz():
    print("Me alegra rotundamente!! ")


def Nolopuedoexplicar():
     print("Entiendo!! ")
menu()

opcion = input("Selecciona una opción (1-3): ") # Obtenemos la elección del usuario

if opcion == '1':
    triste() # Llamamos a la función si eligió 1
elif opcion == '2':
    Feliz()  # Llamamos a la función si eligió 2
elif opcion == '3':
    Nolopuedoexplicar() # Llamamos a la función si eligió 3
else:
    print("Opción inválida. Por favor, elige una opción del 1 al 3.") # Manejamos opciones incorrectas

