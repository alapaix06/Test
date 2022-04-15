# El doble == es para comparar dos valores
# Para saber si son distintos, usamos !=
# Para saber si son iguales, usamos ==
#
a= 10
b = 5

print("Son iguales " +  str(a==b))
print("Son diferentes " + str(a!=b))

# solo usamos < y > para saber si es menor o mayor
print("Es mayor " + str(a>b))
print("Es menor " + str(a<b))

# Si queremos decir si es mayor o igual, usamos <=
print("Es mayor o igual " + str(a>=b))
print("Es menor o igual " + str(a<=b))

# Operadores logicos and y or

# Podemos usar and para hacer dos comparaciones, como tambien podemos usar & por and
print("Si a es menor que b y a es igual o menor que b " + str( a<b & a<=b))
print("Si a es mayor que b o a es igual a b " + str( a>b and a==b))

# Tambien podemos comparar con la funcion or 

print("Si es mayor que : " + str(a<b or a>b))