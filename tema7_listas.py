## Listas

lista1 = [1, 2, 3, 4, 5]
lista2 = ["Pedro", "Maria", "Juan", "Luis", "Carlos"]
lista3 = [6.3, 7.4, 8.5, 9.6, 10.7]
lista4 = [True, False, True, False, True]
lista5 = ["Pedro", 23, True, False, 10.7]

print(type(lista1))

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

print(lista1[0])
print(len(lista1))

## Agrgar elementos
lista1.append(6)
lista1.append(7)
lista1.append(8)

print(lista1)

## Eliminar elementos
lista1.pop(0)
print(lista1)

##Ordenar listas
print(lista2)
lista2.sort()
print(lista2)