# importacion del modulo
import psycopg2

#conexion a base de datos
conexion=psycopg2.connect(user='postgres',
                          password='140423',  
                          host='localhost',
                          port='5432',
                          database='python')

                          

# utilizar cursor
cursor=conexion.cursor()

# crear sentencia sql
sql='INSERT INTO persona (pers_nombre,pers_apellido,pers_edad) VALUES(%s,%s,%s)'

# solicitud de datos al usuario
pers_nombre=input('ingrese el nombre: ')
pers_apellido=input('ingrese el apellido: ')
pers_edad=input('ingrese la edad: ')

# recoleccion de datos
datos=(pers_nombre,pers_apellido,pers_edad)

# hacer uso del metodo execute
cursor.execute(sql,datos)

# guardar registro
conexion.commit()

# registro insertados
registros=cursor.rowcount

# mostrar mensaje
print(f'registro insertado: {registros}')

# cerrar conexiones
cursor.close()
conexion.close()
