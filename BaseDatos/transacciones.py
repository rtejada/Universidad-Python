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


try:
    #conexion.autocommit = True
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Roxana', 'Esparza', 'resparza@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan', 'Perez', 'jperez3@mail.com', 1)
    cursor.execute(sentencia, valores)

    #guardamos la información en la base de datos
    conexion.commit()
    print('Concluyó con éxito la transacción')

except Exception as e:
    #rollback da marcha atras a todas las operaciones pendientes
    conexion.rollback()
    print(f'Ocurrió un error en la transacción: {e}')

finally:
    cursor.close()
    conexion.close()
