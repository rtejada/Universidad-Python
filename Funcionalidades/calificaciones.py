'''El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un value entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro value debe imprimir: value desconocido
'''

value = int(input('Proporciona un value entre 0 y 10: '))
note = None


if value >= 9 and value <= 10:
    note = 'A'

elif value >= 8 and value < 9:
    note = 'B'

elif value >= 7 and value < 8:
    note = 'C'

elif value >= 6 and value < 7:
    note = 'D'

elif value >= 0 and value < 6:
    note = 'F'

else:
    note = 'Valor Desconocido'


print('Nota: ', note)