# Ciclo for
# Sirve para iterar sobre una secuencia de datos
# Podemos reperir una secuencia de datos usando una variable y una condicion

# El for va a repetir la sentencia hasta que se cumpla la condicion, name es la variable 
# que va a contener el valor de cada iteracion, range es la cantidad de iteraciones que va a hacer
# en este caso va a repetir 100 veces

for name in range(100):
    print("Adams" + str(name))

# Si queremos imprimir los valores de una variable en un rango de valores
#  Tenemos que declarar la varibale y luego asignarle el valor


# Aqui le indicanmos que colores tiene el arreglos de todos los colores, color sera la varible
# que va a usar el for
colores = ["rojo", "azul", "verde"]
for color in colores:
    print(color)

# Si queremos que imprima los valores de cada caracter de una cadena
#  Tenemos que declarar la varibale y luego asignarle el valor

for caracter in "Hola Mundo":
    print(caracter);

name = "Ada"

for caracter in name:
    print(caracter) 

# Si queremos hacer u incremento de una variable usamos for y la funcion range e indicamos de donde a donde contara
# Ejemplo

for num  in range (1, 100):
    print(num)
    
# Si queremos indicar que cuente de cada numero en numero usamos otro numero dentro del rango

for numero in range (0, 101, 5):
    print(numero)

# Si queremos hacer un bucle y queremos interrumpir en alguna parte predeterminda lo que tenemos que hacer
# Es usar la condicional if y dentro del if mandamos la funcion break

for nmx in range (0, 101, 2):
    if (nmx >= 30 ):
        break
    print(nmx)  

# Aqui es importante tomar en cuenta la identacion de print que se encuentra en paralelo con el if
# Y no dentro de el, asi el imprimira todos los numeros y para cuando se cumpla la condicion.

# Si queremos imprimir algunos valores y otros no, lo que debemos hacer es usar la funcion continue
# Esta funcion nos permite saltar una iteracion y continuar con la siguiente iteracion
# ejemplo

for num in range (0, 101, 2):
    if (num >= 30 ):
        continue
    print(num)

# Tambien podemos usar el or dentro del if para que vuelve dichos valores 
# Aqui le decimos que no imprima los numeros del 30 al 40
for num in range (0, 101, 2):
    if (num >= 30 or num <= 40):
        continue
    print(num)


