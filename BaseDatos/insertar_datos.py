import psycopg2 as db
from dotenv import load_dotenv
import os

load_dotenv(os.getcwd() + "/../.env.conection_postgresql")
user = os.getenv('SERVER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DATABASE')

conexion = db.connect(user=user,
                      password=password,
                      host=host,
                      port=port,
                      database=database)
'''
conexion = db.connect(user='postgres',
                 password='roxana',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')
'''

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
valores = ('Carlos', 'Lara', 'clara@mail.com')
cursor.execute(sentencia, valores)

#guardamos la información en la base de datos
conexion.commit()

#muestra la cantidad de registros insertados
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

cursor.close()
conexion.close()