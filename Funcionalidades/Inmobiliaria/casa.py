from inmueble import *

class Casa(Inmueble):
    garaje_valido = ("anexo", "separado", "ninguno")
    jardin_valido = ("si", "no")

    def __init__(self, num_pisos='',
            garaje='', jardin='', **kwargs):
        super().__init__(**kwargs)
        self.garaje = garaje
        self.jardin = jardin
        self.num_pisos = num_pisos

    def mostrar(self):
        super().mostrar()
        print("DETALLES CASA")
        print("# de pisos: {}".format(self.num_pisos))
        print("garaje: {}".format(self.garaje))
        print("jardin: {}".format(self.jardin))

    def prompt_init():
        parent_init = Inmueble.prompt_init()
        jardin = obtener_input_valido("¿La casa tiene Jardín? ",
                    Casa.jardin_valido)
        garaje = obtener_input_valido("¿Hay un garaje? ",
                Casa.garaje_valido)
        num_pisos = input("¿Cuantos pisos? ")

        parent_init.update({
            "jardin": jardin,
            "garaje": garaje,
            "num_pisos": num_pisos
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)
