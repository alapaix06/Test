# Las funciones en python se nombran por def, hay funciones con argumentos y funciones donde le decimos
# Los parametros, la valores que agregamos dentro del parametro son variables que en lo adelante se le asignara
# Un valor

def suma ():
    print("Funcion sin argumentos")

suma ()

# Tenemos funciones con varibles que estas tendran uso al asignarle el valor al llamar la funcion

def sumando(a,b):
    resultado = a + b
    print("Esto es una suma: "+ str(resultado) )

sumando(12,1)

# Podemos crear funcion donde no tengamos predefinido la cantidad de variables que hay, asi decimos que 
# se pueden usar n cantidad de variables, para eso usamos *args, decimos que use un for

def test(*args):
    valorinicial = 0
    for variable in args:
        valorinicial = valorinicial + variable
    print("Esto es el resultado: "+ str(valorinicial))

test(4,2,8)