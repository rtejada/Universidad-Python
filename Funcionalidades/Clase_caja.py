class Caja:

    def __init__(self, largo, ancho, alto):

        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def volumen(self):
        return self.largo * self.ancho * self.alto


print('Calcularemos el Volumen de un CAJA')

largo = int(input('Inserta el largo: '))
ancho = int(input('Inserta el ancho: '))
alto = int(input('Inserta el alto: '))

vol_caja = Caja(largo, ancho, alto)
print('El volumen de la Caja es:', vol_caja.volumen(), 'm³')
