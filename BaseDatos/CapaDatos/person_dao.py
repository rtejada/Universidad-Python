from person import Person
from connection import Connection
from logger_base import logger

class PersonDao:
    '''
    DAO (DATA ACCESS OBJECT)
    CRUD: Create-Read-Update-Delete, entity Person
    '''
    __SELECT = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERT = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
    __UPDATE = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    __DELETE = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def select(cls):
        cursor = Connection.get_cursor()
        logger.debug(cursor.mogrify(cls.__SELECT))
        cursor.execute(cls.__SELECT)
        registers = cursor.fetchall()
        people = []
        for register in registers:
            person = Person(register[0], register[1], register[2], register[3])
            people.append(person)
        Connection.close()
        return people

    @classmethod
    def insert(cls, person):
        try:
            connection = Connection.get_connected()
            cursor = Connection.get_cursor()
            logger.debug(cursor.mogrify(cls.__INSERT))
            logger.debug(f'Person to insert: {person}')
            values = (person.first_name, person.last_name, person.email)
            cursor.execute(cls.__INSERT, values)
            connection.commit()

            return cursor.rowcount

        except Exception as e:
            connection.rollback()
            logger.error(f'Exception to insert person: {e}')

        finally:
            Connection.close()

    @classmethod
    def update(cls, person):
        try:
            connection = Connection.get_connected()
            cursor = Connection.get_cursor()
            logger.debug(cursor.mogrify(cls.__UPDATE))
            logger.debug(f'Person to insert: {person}')
            values = (person.first_name, person.last_name, person.email, person.id_person)
            cursor.execute(cls.__UPDATE, values)
            connection.commit()
            return cursor.rowcount

        except Exception as e:
            connection.rollback()
            logger.error(f'Exception to insert person: {e}')

        finally:
            Connection.close()

    @classmethod
    def delete(cls, person):
        try:
            connection = Connection.get_connected()
            cursor = Connection.get_cursor()
            logger.debug(cursor.mogrify(cls.__DELETE))
            logger.debug(f'Person to delete: {person}')
            value = (person.id_person,)
            cursor.execute(cls.__DELETE, value)
            connection.commit()
            return cursor.rowcount

        except Exception as e:
            connection.rollback()
            logger.error(f'Exception to delete person: {e}')

        finally:
            Connection.close()


if __name__ == '__main__':

    #people = PersonDao.select()
    #for person in people:
        #logger.debug(person)
        #logger.debug(person.id_person)

    #person = Person(first_name='Jose', last_name='Castillo', email='jcastillo@mail.com')
    #persons_inserted = PersonDao.insert(person)
    #logger.debug(f'Persons Inserted: {persons_inserted}')

    #person = Person(first_name='Diego', last_name='Suarez', email='dsuarez@mail.com', id_person=18)
    #persons_inserted = PersonDao.update(person)
    #logger.debug(f'Persons Inserted: {persons_inserted}')

    person = Person(id_person=18)
    person_delete = PersonDao.update(person)
    logger.debug(f'Persons Delete: {person_delete}')

    


