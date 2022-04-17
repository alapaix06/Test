# # El ciclo while se usa para contar mientras que la condicion se cumpla
# # En while usamos el valor de una variable  y una condicion que puede ser otra varable o una funcion
# # Es importante saber que en el while debemos decir que la variable que va a contrar debe ser igual 
# # mas 1 
# #ejemplo

inicio = 0
fin = 11


while (inicio <= 5):
    print(inicio)
    inicio = inicio + 1

# # tambien podemos decir que while se alimentara con otra variable hasta que cumpla su condicion
# # El numero en name = name significa en la cantidad que queremos que incremente

# # Tambien podemos usar el break dentro del while 

while (inicio <= fin):
    print(inicio)
    inicio = inicio + 1
    if (inicio == 5):
        break

# # Al igual podemos utilizar el continue dentro del while para que se vuele un numero en especifico
# # Es importante saber que el print va depues del if y fuera del if


while inicio <= fin:
    inicio = inicio + 1
    if (inicio == 5):
        continue
    print(inicio)
    
# Si queremos usar un if y elif, debemos colocar el print despues del elif y fuera

while (inicio <= fin):
    inicio = inicio + 2
    if (inicio ==4):
        continue
    elif (inicio == 8):
        break
    print(inicio)

    