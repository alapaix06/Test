# Podemos utlizar la función len() para saber cuantos caracteres tiene una cadena.
# Podemos utilizar la función str() para convertir un número en cadena.
# Podemos utilizar la función int() para convertir una cadena en número.
# Podemos utilizar la función ord() para obtener el valor numérico de un caracter.
# Podemos utilizar la función chr() para obtener el caracter de un valor numérico.
# Podemos utilizar la función split() para dividir una cadena en subcadenas.

from turtle import clear


nombre = "Juan"
# Para usar el upper y lower, debemos importar la función, lo que debemos hacer es usar la varible 
# nombre y luego usar la función.

print(nombre.upper())
print(nombre.lower())

# La funcion capitalize() sirve para poner la primera letra en mayúscula.

print(nombre.capitalize())

# Si tenemos una cadena con multiples palabras, podemos utilizar la función split() para separarlas o
# dividirlas en subcadenas. 

arreglo = "Python, Java, C++, PHP, Ruby, Javascript"
print(arreglo.split())

# La función join() sirve para unir una lista de cadenas en una sola cadena.
print("".join(arreglo.split()))

print(len(arreglo))


# La función replace() sirve para reemplazar una cadena por otra.
# Primero coloca la cadena que quieres reemplazar, luego la cadena que quieres poner.
print(arreglo.replace("Python", "Java"))

# Se puede usar la funcion format para insertar una cadena en una cadena.
# cada vez que abramos llaves indicaremos que ahi va la variable que queremos insertar.

print("{} es un lenguaje de programación".format("Python"))
print("El nombre tu es: {} Tu appellido es {}".format(nombre, "Lapaix"))

# Pedir valores con input()
# input() sirve para pedir datos al usuario, tambien podemos indicar el tipo de datos  que queremos utilizar .

inputName = input(str("Ingresa tu nombre: "))
print("Hola {}".format(inputName))


# Para trabajar con operaciones de entero y convertilas para que luego sean operadas
# Tenemos que imprimir el mandato, luego hacemos el input, luego convertimos.

print("Ingresa un numero:")
a = input()
a = int(a)

print("Ingresa otro numero:")
b = input()
b = int(b)

suma = a + b
print("La suma de {} y {} es {}".format(a, b, suma))


