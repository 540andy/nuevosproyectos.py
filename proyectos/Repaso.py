#Ejercicio: Calculadora de Descuento de Tienda Online

#Crea una variable llamada precio_producto y asígnale un valor numérico (por ejemplo, 50). 

precio_producto = 50

#Definimos el porcentaje de descuento que se va aplicar.

porcentaje_descuento = 15
# Calculamos el precio con descuento

precio_final = precio_producto * (1 - porcentaje_descuento / 100)

#Explicasiòn de lo anterior 
# Esta fórmula calcula directamente el precio final. Si tienes un 15% de descuento, significa que pagas el 85% del 
# precio original (100% - 15% = 85%). (1 - porcentaje_descuento / 100)
#  calcula ese "porcentaje que queda por pagar" en formato decimal (ej., 1 - 0.15 = 0.85).

#Aplicamos una condición para envío gratis:
 
 

if precio_final >= 50:
    print("Tienes envio gratis.")
else:
    print("El precio final es :", precio_final)
    print("Agrega un producto màs para envio gratis!")

#Funcion para calcular el promedio de una lista de numeros 

def promedio(lista):
    return sum(lista) /  len (lista)
    
resultado = promedio ([4, 8, 10, 12, 14])
print(resultado)
