# Primer proyecto de mi portafolio profecional

import json #Libreria para el manejo de datos

conocimiento = {
    "que es un agujero negro": "Un agujero negro es como un remolino mágico en el espacio que tiene una fuerza tan fuerte que ni siquiera la luz puede escapar. ¡Es como un aspiradora cósmica gigante!",
    "cuantos planetas hay en el sistema solar": "¡En nuestro vecindario espacial, el sistema solar, hay ocho planetas! Son como ocho canicas gigantes que dan vueltas alrededor del Sol: Mercurio, Venus, la Tierra (¡donde vivimos!), Marte, Júpiter, Saturno, Urano y Neptuno.",
    "de que color es marte": "¡Marte es de color rojo! Por eso le dicen el 'Planeta Rojo'. Parece como si estuviera cubierto de arena mágica de color óxido.",
    "como es un eclipse": "Un eclipse es cuando la Luna o la Tierra juegan a taparle el ojo al Sol o a la Luna. ¡Es como un juego de las escondidas en el cielo!",
    "cuanta agua hay en la tierra": "¡Hay muchísima agua en la Tierra! Tanta que llena todos los océanos, ríos y lagos. ¡Es como si la Tierra fuera una gran bola azul de agua!",
    "nos impactara un asteroide": "¡No te preocupes! Los científicos con sus telescopios están vigilando el cielo para que no nos golpeen rocas espaciales grandes. A veces caen algunas chiquitas, ¡pero no son peligrosas!",
    "hace frio en el espacio": "¡Sí, mucho frío! Como no hay aire como aquí, el calor del Sol no se queda cerca. Pero si te pones al sol en el espacio, ¡te puedes calentar mucho! Es un frío diferente.",
    "existen los alienigenas": "¡Es una pregunta muy emocionante! No lo sabemos con seguridad, pero los científicos están buscando señales de vida en otros planetas. ¡Quizás algún día encontremos amigos espaciales!",
    "hay vida en saturno": "Saturno es un planeta gigante hecho de gas, ¡no tiene suelo firme como la Tierra! Hace mucho frío y los vientos son muy fuertes. Pero algunas de sus lunas tienen lugares secretos donde podría haber algo interesante.",
    "por que marte no es un planeta": "¡Claro que Marte es un planeta! Es el cuarto planeta desde el Sol y es de color rojo. Quizás lo confundes con Plutón, que ahora es un planeta enano, ¡un planeta chiquito!",
    # Aquí puedes seguir añadiendo más preguntas y respuestas para niños...
}

def saludar(): #Funcion para devolver un saludo al usuario
    print("¡Hola, pequeño explorador del espacio! ¡Estoy aquí para contarte cosas asombrosas sobre el universo!")

def responder_pregunta(pregunta):
    pregunta_normalizada = pregunta.lower() # se utiliza para convertir una cadena de texto a minúsculas. 
    if pregunta_normalizada in conocimiento:
        return conocimiento[pregunta_normalizada]
    else:
        return "¡Uy! Parece que esa pregunta aún no la conozco. ¿Hay algo más que te cause curiosidad?"

def main():
    saludar()

    while True:
        print("\nAquí tienes una lista de temas espaciales que te puedo contar:")
        lista_de_preguntas = list(conocimiento.keys())
        for i, pregunta in enumerate(lista_de_preguntas):
            print(f"{i + 1}. {pregunta.capitalize()}?")

        print("\nEscribe el número del tema que te interese o escribe 'otra' para preguntar algo más, o 'adiós' para terminar.")
        opcion = input("> ").lower()

        if opcion == "adiós":
            print("¡Fue genial explorar el espacio contigo! ¡Hasta la próxima aventura!")
            break
        elif opcion == "otra":
            pregunta_usuario = input("¿Qué otra cosa te gustaría saber del espacio? ")
            respuesta = responder_pregunta(pregunta_usuario)
            print(respuesta)
        elif opcion.isdigit():
            try:
                indice_seleccionado = int(opcion) - 1
                if 0 <= indice_seleccionado < len(lista_de_preguntas):
                    pregunta_seleccionada = lista_de_preguntas[indice_seleccionado]
                    respuesta = responder_pregunta(pregunta_seleccionada)
                    print(f"\n{pregunta_seleccionada.capitalize()}:")
                    print(respuesta)
                else:
                    print("¡Ups! Esa opción no está en la lista. Elige un número de la lista, 'otra' o 'adiós'.")
            except ValueError:
                print("¡Eso no parece un número! Escribe un número de la lista, 'otra' o 'adiós'.")
        else:
            print("No entendí qué quieres hacer. Escribe un número de la lista, 'otra' o 'adiós'.")

if __name__ == "__main__": # Indica que el código dentro de ese bloque solo se ejecutará si el archivo se está ejecutando directamente (por ejemplo, al ejecutarlo desde la terminal). 
    #Si el archivo se importa como un módulo en otro script, ese bloque no se ejecutará.
    main()


