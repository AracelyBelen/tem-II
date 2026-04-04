# tuplas (inmutables)
#numeros = (1,2,5,4,5,6)
# imprime un elemento
#print(numeros[3])
# ocurrencia
#print(numeros.count(5))
#print(numeros.index(5))

# diccionarios -> almacena pares de clave-valor
mi_diccionario = {'nombre':'brumo diaz','edad':25,'ciudad':'la paz'}
print(mi_diccionario)
# acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['ciudad'])
# agregar elementos
mi_diccionario['profecion'] = 'ingeniero'
print(mi_diccionario)
# eliminar un elemento
del mi_diccionario['ciudad']
print(mi_diccionario)
# obtener claves del diccionario
print(mi_diccionario.keys())
# obtener valores del diccionario
print(mi_diccionario.values())
# verificar si una clave existe
if 'edad' in mi_diccionario:
    print('clave encontrada')
# recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print('[clave: ]',clave,'[valor: ]',valor)