from logger_base import logger
from psycopg2 import pool
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
    __MIN_CONN = 1
    __MAX_CONN = 5
    __pool = None

    @classmethod
    def get_pool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(cls.__MIN_CONN,
                                                       cls.__MAX_CONN,
                                                       host=cls.__HOST,
                                                       user=cls.__USERNAME,
                                                       password=cls.__PASSWORD,
                                                       port=cls.__DB_PORT,
                                                       database=cls.__DATABASE
                                                       )
                logger.debug(f'Successful pool creation: {cls.__pool}')
                return cls.__pool

            except Exception as e:
                logger.error(f'Error when creating connection pool')
                sys.exit()
        else:
            return cls.__pool

    @classmethod
    def get_connected(cls):
        #obtener conexion del pool
        connection = cls.get_pool().getconn() #getconn asigna las conexiones
        logger.debug(f'Connection obtained from the pool: {connection}')
        return connection

    @classmethod
    def free_connection(cls, connection):
        #Regresar el objeto conexion al pool
        cls.get_pool().putconn(connection)
        logger.debug(f'Return connection to the pool')
        logger.debug(f'Status to the Pool: {cls.__pool}')

    @classmethod
    def close_connection(cls):
        #Cerrar el pool y otas sus conexiones
        cls.get_pool().closeall()
        logger.debug(f'we close all pool connections: {cls.__pool}')


if __name__ == '__main__':

    #Obtener una conexion a partir del pool
    connection = Connection.get_connected()
    connection1 = Connection.get_connected()
    #Regresar conexiones al pool
    Connection.free_connection(connection)
    Connection.free_connection(connection1)
    #Cerramos el pool
    Connection.close_connection()
    





