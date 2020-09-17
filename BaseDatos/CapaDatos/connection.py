from logger_base import logger
import psycopg2 as db
from dotenv import load_dotenv
import os
import sys


class Connection:

    load_dotenv(os.getcwd() + "/../../.env.conection_postgresql")
    user = os.getenv('SERVER')
    password = os.getenv('PASSWORD')
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    database = os.getenv('DATABASE')
    __DATABASE = database
    __USERNAME = user
    __PASSWORD = password
    __DB_PORT = port
    __HOST = host
    __connection = None
    __cursor = None

    @classmethod
    def get_connected(cls):

        if cls.__connection is None:
            try:
                cls.__connection = db.connect(host=cls.__HOST,
                                              user=cls.__USERNAME,
                                              password=cls.__PASSWORD,
                                              port=cls.__DB_PORT,
                                              database=cls.__DATABASE)
                logger.debug(f'successful connection: {cls.__connection}')
                return cls.__connection
            except Exception as e:
                logger.error(f'error when connecting to the DB: {e}')
                sys.exit()
        else:
            return cls.__connection

    @classmethod
    def get_cursor(cls):

        if cls.__cursor is None:
            try:
                cls.__cursor = cls.get_connected().cursor()
                logger.debug(f'the cursor was successfully opened: {cls.__cursor}')
                return cls.__cursor
            except Exception as e:
                logger.error(f'error when get to the Cursor: {e}')
                sys.exit()
        else:
            return cls.__cursor

    @classmethod
    def close(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            except Exception as e:
                logger.error(f'Error to the close Cursor: {e}')

        if cls.__connection is not None:
            try:
                cls.__connection.close()
            except Exception as e:
                logger.error(f'Error to the close Connection: {e}')
        logger.debug('the connection and cursor objects have been closed')


if __name__ == '__main__':
    logger.info(Connection.get_cursor())
    Connection.close()






