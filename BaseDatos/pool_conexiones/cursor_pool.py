from connection import Connection
from logger_base import logger


class CursorPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    #Inicio de With
    def __enter__(self):
        logger.debug(f'Init the With, method __enter__')
        self.__conn = Connection.get_connected()
        self.__cursor = self.__conn.cursor()
        return self.__cursor

    #Fin del bloque With
    def __exit__(self, exception_type, exception_value, exception_traceback):
        logger.debug(f'The method is executed __exit__()')
        #if exception_value is not None:
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'An exception occurred: {exception_value}')
        else:
            self.__conn.commit()
            logger.debug('Commit to the Transaction')

        #Cerramos el cursor
        self.__cursor.close()

        #Regresar conexion al Pool
        Connection.free_connection(self.__conn)


if __name__ == '__main__':
    # Obtenemos un cursor  a partir de la conexión del pool
    # with se ejecuta __enter__ y termina con __exit__
    with CursorPool() as cursor:
        cursor.execute('SELECT * FROM persona')
        logger.debug('List Persons')
        logger.debug(cursor.fetchall())






