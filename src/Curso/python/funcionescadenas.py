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
