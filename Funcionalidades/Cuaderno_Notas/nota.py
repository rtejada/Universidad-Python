import datetime

class Nota:
    '''representa una nota em el cuaderno. se compara con un string
    en las busquedas y las etiquetas para cada nota'''

    ult_id = 0

    def __init__(self, memo, tags=''):
        '''inicializa una nota con memo y opcional tags
            separado por comas, Automaticamente configura la fecha
            de creacion de la nota y unica id'''
        Nota.ult_id += 1
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        self.id = Nota.ult_id

    def match(self, filter):
        '''Determina si esta nota concuenda con el filtro
            de texto. Devuelve Tru si concuerda, en otro caso False.
            Busqueda es case sensitive y compara con tanto con text como
            con tags'''
        return filter in self.memo or filter in self.tags
