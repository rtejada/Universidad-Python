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
sql = 'SELECT * FROM persona ORDER BY id_persona'

cursor.execute(sql)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()

