
class SoloPares(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Sólo pueden añadirse enteros")
        if integer % 2:
            raise ValueError("Sólo pueden añadirse números pares")
        super().append(integer)

def no_devolver():
    print("Estoy a punto de lanzar una excepción")
    raise Exception("Esto siempre será lanzado")
    print("Esta línea nunca se ejecutará")
    return "Esto no será devuelto."

def llamar_excepcion():
    print("llamar_excepcion empieza aquí...")
    no_devolver()
    print("una excepción ha sido lanzada...")
    print("...por tanto esta línea no se ejecuta")

lista = [5,2,-3,4]

pares = SoloPares(lista)
#print(pares.append('esto es un texto'))
#print(pares.append(lista[0]))

print(llamar_excepcion())




