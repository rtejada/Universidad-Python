#Tuplas son ordenadas e inmutables (no se pueden modificar = inmutable)
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)
#largo de una tupla
print(len(frutas))
#accediendo a un elemento
print( frutas[0] )
#Navegación inversa
print( frutas[-1] )
#accediendo a un rango
print(frutas[0:1])
#cambiar un valor
frutasLista = list(frutas)
frutasLista[1]="Platanito"
frutas = tuple(frutasLista)
print(frutas)
#iterar una tupla
for fruta in frutas:
    print(fruta, end =", ")
#no podemos agregar ni remover elementos
#remover completamente la tupla
del frutas
print(frutas)    