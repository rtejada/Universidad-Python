from lista_contactos import ListaContactos


class Contacto:
    list_contactos = ListaContactos()

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        Contacto.list_contactos.append(self)


class EnviarEmail:

    def enviar_email(self, mensaje):

        print('enviando mensaje a ' + self.email)


class EnvioEmailContactos(Contacto, EnviarEmail):
    pass





lista = ListaContactos()
c = Contacto('Juan', 'prueba@gmail.com')

