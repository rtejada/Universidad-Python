from figura_geometrica import FiguraGeometrica
from color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        # hace referencia a FiguraGeometrica por la prioridad
        # super().__init__(lado, lado)
        Color.__init__(self, color)

    def area_cuadrado(self):

        return FiguraGeometrica.__str__(self)

    def color(self):

        return Color.__str__(self)



