from logger_base import logger


class Person:
    def __init__(self, id_person=None, first_name=None, last_name=None, email=None):
        self.__id_person = id_person
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    def __str__(self):
        return (
            f'ID: {self.__id_person}, '
            f'FIRST_NAME: {self.__first_name}, '
            f'LAST_NAME: {self.__last_name}, '
            f'EMAIL: {self.__email}'
        )

    @property
    def id_person(self):
        return self.__id_person

    @id_person.setter
    def id_person(self, id_person):
        self.__id_person = id_person

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email


if __name__ == '__main__':
    persona1 = Person(1, 'Juan', 'Perez', 'email')
    logger.debug(persona1)
    # simulando un objeto a insertar de tipo persona
    persona2 = Person(first_name='Karla', last_name='Gomez', email='kgomez@mail.com')
    logger.debug(persona2)
    # simular el caso de eliminar un objeto de tipo persona
    persona3 = Person(id_person=3)
    logger.debug(persona3)
