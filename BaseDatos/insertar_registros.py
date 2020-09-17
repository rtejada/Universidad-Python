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

cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
valores = (
    ('Marcos', 'Cantu', 'macantu@mail.com'),
    ('Angel', 'Quintana', 'aquintana@mail.com'),
    ('Maria', 'Gonzalez', 'mgonazalez@mail.com')
)
cursor.executemany(sentencia, valores) #executemany inserta varios registros

#guardamos la información en la base de datos
conexion.commit()

registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

cursor.close()
conexion.close()