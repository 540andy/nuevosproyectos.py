import random # Importa la biblioteca random, que se utiliza para generar números aleatorios.

minimo = 1 # se refiere al nùmero minimo de intentos para adivinar el nùmero escondido !

maximo = 10 # nùmero maximos de intentos para adivinar.

numero_azar = random.randint(minimo, maximo) # Esta línea genera un número entero aleatorio entre los valores 
#de minimo y maximo (inclusive) y lo guarda en la variable numero_azar.

# utilizaremos un bucle while

while True: # ejecutar bloques de còdigo de manera repetitiva 
    intento_de_usuario = int(input("Ingrese un nùmero: ")) #Pide al usuario ingrese un nùmero

    # Esta línea compara si el número aleatorio (numero_azar) es diferente (!=) al número que ingresó el usuario 
    if numero_azar != intento_de_usuario: 
        print("Te has pasado!! El nùmero es mas pequeño que " + str (intento_de_usuario)) 

    elif intento_de_usuario < numero_azar: 
        print("Has fallado!! El nùmero es mas grande que " + str (intento_de_usuario)) 
        

    else : # es una forma de decir (si, no)

        print("Has acertado !!")
        break # salida del bloque (donde se detiene la ejecución de ese bloque de código)






