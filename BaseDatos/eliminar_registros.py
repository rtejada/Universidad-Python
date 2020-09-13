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
sentencia = 'DELETE FROM persona WHERE id_persona IN %s'

entrada = input("Proporciona las pk a eliminar (separado por comas): ")
tupla = tuple(entrada.split(','))
valores = (tupla,)

cursor.execute(sentencia, valores)
#guardamos la información en la base de datos
conexion.commit()

registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')

cursor.close()
conexion.close()
