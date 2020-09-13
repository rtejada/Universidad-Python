import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='roxana',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

cursor = conexion.cursor()
sql = 'SELECT * FROM persona WHERE id_persona IN %s'
entrada = input('Propocipnar las PK a buscar(separados por comas): ')
tupla = tuple(entrada.split(','))
llaves_primarias = (tupla,)
cursor.execute(sql, llaves_primarias)
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close()
conexion.close()