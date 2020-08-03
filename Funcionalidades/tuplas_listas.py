'''Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for:'''

tupla = (13, 1, 8, 3, 2, 5, 8)

lista = []

for i in tupla:
    if i < 5:
        lista.append(i)

print('Lista: ', end='')
for i in lista:
    print(i, end=' ')

