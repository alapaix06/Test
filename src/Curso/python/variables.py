# # #Las variables en python se almacenan sin declarar el tipo de varibale que es,
# # # por lo tanto, se puede asignar cualquier tipo de dato.

# # # Ejemplo:

a=5
b=6
c=a+b
d=a-b
e=a*b
f=a/b

# Si queremos usar una varible e imprimirla en pantalla, debemos usar la funcion print()
# si queremos concatenarla con un string debemos indicar que el texto sera un string en parentesis

print("El resultado de la suma es: " + str(c))
print("El resultado de la resta es: " + str(d))
print("El resultado de la multiplicacion es: " + str(e))
print("El resultado de la division es: " + str(f))

# # # Tenemos variables de string
# # # str significa string

name = input(str("Ingrese su nombre: "))
apellido = input(str("Ingrese su apellido: "))
print("Hola " + name + " " + apellido)

# # Para inprimir el tipo de dato de una variable debemos usar la funcion type()

print(type(name))

# # # Conversiones

# # Las conversiones son operaciones que nos permiten convertir un tipo de dato a otro,
# # por ejemplo, convertir un numero a string, o un string a numero, etc.
# # Para hacer estas conversiones podemos realizarlas de la siguiente manera:

test = "5"
test = int(test)
print(type(test))

print("Ahora el tipo de datos es:  " + str(type(test)))

# Si se suman dos string no dara una operacion matematica, por lo tanto,
# debemos convertir los datos a tipo de dato numerico para poder realizar la operacion
# Lo que pasara es que los strings serian concatenados y no se realizara una operacion matematica

# Ejemplo:

numero1 = "5"
numero2 = "6"

# para realizar la conversion de string a numero debemos usar la funcion int()
# ejemplo:

numero1 = int(numero1)
numero2 = int(numero2)
suma = numero1 + numero2
print(type(suma))

# En python podemos usar las cadenas de textos como arreglos,
# por ejemplo:

nameinput = input(str("Ingrese su nombre: "))
apellidoinput = input(str("Ingrese su apellido: "))
print ("Sus inciales son: " + nameinput[0] + apellidoinput[0])

# Luego de llamar la variable le indicamos que queremos que se imprima en pantalla
# y que se imprima el valor de la posicion 0 del arreglo, es decir, la primera letra
# Si queremos imprimir un rango de letras, debemos indicar el rango de letras que queremos imprimir
# ejemplo:

nameinput = input(str("Ingrese su nombre: "))
apellidoinput = input(str("Ingrese su apellido: "))
print ("Sus inciales son: " + nameinput[0:5] + apellidoinput[0])

# Si queremos imprimir que inicie desde un punto al final, debemos dejar los : vacios

nameinput = input(str("Ingrese su nombre: "))
apellidoinput = input(str("Ingrese su apellido: "))
print ("Sus inciales son: " + nameinput[5:] + apellidoinput[0])

# Para realizarlo a la inversa debemos utilizar el operador -1

nameinput = input(str("Ingrese su nombre: "))
apellidoinput = input(str("Ingrese su apellido: "))
print ("Sus inciales son: " + nameinput[-5:] + apellidoinput[0])

    