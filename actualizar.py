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
sql='UPDATE persona SET pers_nombre=%s,pers_apellido=%s,pers_edad=%s WHERE pers_id=%s'

# consulta de datos a usuario
pers_id=input('ingrese id de la persona a editar: ')
pers_nombre=input('ingrese nombre: ')
pers_apellido=input('ingrese apellido: ')
pers_edad=input('ingrese edad: ')

#recoleccion de datos
datos=(pers_nombre,pers_apellido,pers_edad,pers_id)

# utilizar el metodo execute
cursor.execute(sql,datos)

# guardar modificacion
conexion.commit()

#contar el numero de cambios
actualizacion=cursor.rowcount

# mostrar mensaje al usuraio
print(f'registro actualizado: {actualizacion}')

# cerrar conexiones
cursor.close()
conexion.close()