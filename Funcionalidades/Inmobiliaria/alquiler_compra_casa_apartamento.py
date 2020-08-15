from compra_alquiler import Compra, Alquiler
from casa import Casa
from apartamento import Apartamento


class CasaAlquiler(Alquiler, Casa):
    def prompt_init():
        init = Casa.prompt_init()
        init.update(Alquiler.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartamentoAlquiler(Alquiler, Apartamento):
    def prompt_init():
        init = Apartamento.prompt_init()
        init.update(Alquiler.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartamentoCompra(Compra, Apartamento):
    def prompt_init():
        init = Apartamento.prompt_init()
        init.update(Compra.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class CasaCompra(Compra, Casa):
    def prompt_init():
        init = Casa.prompt_init()
        init.update(Compra.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)