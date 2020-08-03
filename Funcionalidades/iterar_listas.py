'''Iterar una lista de 0 a 10 e imprimir sólo los números divisibles entre 3'''

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:

    if number % 3 == 0:
        print(number)
