from nota import Nota

class Cuaderno:

    '''Representa una coleccion de notas que pueden ser ertiquetadas,
        modificadas, y se pueden buscar'''
    def __init__(self):
        '''Inicializa un cuader con una lista vacia'''

        self.notas = []

    def nueva_nota(self, memo, tags=''):
        '''Crea una nueva nota y la añade a lista notas'''

        self.notas.append(Nota(memo, tags))

    def modificar_memo(self, nota_id, memo):
        '''Encuentra la nota con la id dada y cambia
            su memo al valor dado.'''
        nota = self._encontrar_nota(nota_id)
        if nota:
            nota.memo = memo
            return True
        return False

    def modificar_tags(self, nota_id, tags):
        '''Encuentra la nota con la id dada y cambia
            sus tags al valor dado'''

        nota = self._encontrar_nota(nota_id)
        if nota:
            nota.tags = tags
            return True
        return False

        #self._encontrar_nota(nota_id).tags = tags

    def search(self, filter):
        '''Encuentra todas las notas que concuerdan con el
            filtro string dado'''

        return [nota for nota in self.notas if nota.match(filter)]

    def _encontrar_nota(self, nota_id):
        '''Localiza la nota con la id dada.'''

        for nota in self.notas:
            if str(nota.id) == str(nota_id):
                return nota

        return None

'''
c = Cuaderno()

c.nueva_nota('Primera Nota')
c.nueva_nota('Segunda Nota')
print(c.notas)
print(c.notas[0].id)
print(c.notas[1].id)
print(c.notas[0].memo)
print(c.notas[1].memo)
print(c.search('Nota'))
print(c.modificar_memo(1, 'Tercera Nota'))
print(c.notas[0].memo)'''
















