# Podemos trabajar con listas en la cual podemos modificar, agregar, eliminar, etc.

lenguajes = ["Python", "Java", "C++", "PHP", "Ruby", "Javascript"]

# Si queremos decirle que nos imprima uno que otro dentro del arreglo se lo especificamos con la posicion
print(lenguajes[0])

# Si queremos cambiar uno en especifico, lo podemos hacer con la posicion
lenguajes[0] = "JavaScript"

print(lenguajes[0])

# Si queremos agregar otros elementos al arreglo, podemos hacerlo con append()

lenguajes.append("C#")
print(lenguajes)

# Si queremos eliminar un elemento del arreglo, podemos hacerlo con pop() o con remove() 
# pop() elimina el ultimo elemento del arreglo
# remove() elimina el elemento que le indiquemos

lenguajes.pop()
print(lenguajes)

lenguajes.remove("C++")
print(lenguajes)
