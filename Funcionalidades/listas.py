#Declarar una lista
#Indices:
#0-Juan
#1-Karla
#2-Ricardo
#3-María
nombres = ["Juan", "Karla", "Ricardo", "María"]
#imprimir la lista
print(nombres)
#Acceder a los elementos de una lista
print(nombres[0]) #imprime el primer elemento
print(nombres[1]) #imprime el segundo elemento
#Navegacion inversa
print(nombres[-1]) #imprime el último elemento)
#Imprime un rango
print(nombres[0:2])#sin incluir el indice 2
#ir del inicio al indice indicado
print(nombres[:3])#sin incluir el indice 3
#ir del índice indicado al final
print(nombres[1:])
#cambiar un valor de la lista
nombres[3] = "Ivone"
print(nombres)
#Iterar una lista
for nombre in nombres:
    print(nombre)
#revisar si existe un elemento en la lista
if "Carla" in nombres:
    print("Karla si existe en la lista de nombres")
else:
    print("No existe en la lista de nombres")
#preguntar el largo de una lista
print(len(nombres))
#agregar un elemento
nombres.append("Lorenzo")
print(nombres)
#insertar un elemento en el índice indicada
nombres.insert(1, "Octavio")
print(nombres)
#remover el elemento proporcionado
nombres.remove("Octavio")
print(nombres)
#remover el último elemento agregado
nombres.pop()
print(nombres)
#remueve el indice indicado
del nombres[0]
print(nombres)
#limpiar la lista
nombres.clear()
print(nombres)
#borrar la lista por completo
del nombres
print(nombres)