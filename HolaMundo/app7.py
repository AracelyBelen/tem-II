# listas
frutas = ["manzana","fresa","naranjas","pera","maracuya"]
#print(frutas)
#print(frutas[0])
#print(frutas[4])
#print(frutas[-2])
#print(frutas[1:4])

# metodos de listas
numeros = [1,2,3,4,5]
# adicionar elementos a una lista
numeros.append(6)
print(numeros)
numeros.insert(0,-1)
numeros.insert(1,0)
print(numeros)
# elimina un elemento en su primera aparicion
numeros.remove(0)
print(numeros)
# verificar si un elemento se encuentra en la lista
print(4 in numeros)
# tamaño de la lista
print(len(numeros))
# elimina el contenido de la lista
numeros.clear()
print(numeros)
