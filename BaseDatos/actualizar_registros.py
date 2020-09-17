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
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'

valores = (
    ('Juan', 'Perez', 'jperez@mail.com', 1),
    ('Karla1', 'Gomez2', 'kgomez3@mail.com', 2)
)

cursor.executemany(sentencia, valores)
# guardamos la información en la base de datos

conexion.commit()

registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')

cursor.close()
conexion.close()