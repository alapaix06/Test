# condicionales if
# Las condicionales if se usan para decidir si una sentencia se ejecuta o no.
# Se colocan las condiciones entre parentsis ().
# Si la condicion se cumple, se ejecuta la sentencia.

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

if (a > b):
    print("El numero mayor es: " + str(a))
else:
    print("El numero mayor es: " + str(b))


# Ejemplo 2
if (a <= b):
    print("{} es menor o igual que {}".format(a, b))
else:
    print("{} es mayor que {}".format(a, b))


# ejemplo 3
if (a == b):
    print("{} es igual que {}".format(a, b))
else:
    print("{} es diferente que {}".format(a, b))

# ejemplo 4

if (a != b):
    print("{} es diferente que {}".format(a, b))
else:
    print("{} es igual que {}".format(a, b))

#  Podemos pedir que se cumplan varias condiciones usando el operador and y 
# tambien or al igual que && y ||
ab = 20
ba = 40
ac = 60

if (ab != ba & ba <= ac):
    print("{} es diferente de {}, y {} es menor o igual a {}".format(ab,ba,ba,ac))
else:
    print("Su resultado no es el esprado")

# Tambien podemos usar el and
if (ab != ba and ba <= ac):
    print("{} es diferente de {}, y {} es menor o igual a {}".format(ab,ba,ba,ac))
else:
    print("Su resultado no es el esprado")
# Tambien podemos usar el |
if (ab != ba | ba <= ac):
    print("{} es diferente de {}, y {} es menor o igual a {}".format(ab,ba,ba,ac))
else:
    print("Su resultado no es el esprado")

# Uso del or
if (ab == ba or ba <= ac):
    print("{} es diferente de {}, y {} es menor o igual a {}".format(ab,ba,ba,ac))
else:
    print("Su resultado no es el esprado")

# uso del elif es como el else if, sirve para hacer multiples condiciones dentro del programa
# Se usa elif para tener varias condiciones, luego al final terminamos con un else que no tendra 
# Nigun condicional si no mas bien un resultado.


if (ab > ba):
    print ("{} o es mayor que {}".format(ab,ba))
elif (ba > ab):
    print("{} es mayor que {}".format(ba,ab))
elif (ac > ab):
    print("{} es mayor que {}".format(ac,ab))
else:
    print("Su resultado no es el esperado")

# Uso del or

if (ab > ba or ba > ab):
    print ("{} o es mayor que {}".format(ab,ba))
elif (ac > ab):
    print("{} es mayor que {}".format(ac,ab))
else:
    print("Su resultado no es el esperado")

