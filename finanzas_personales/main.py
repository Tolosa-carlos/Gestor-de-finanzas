from database import conectar

conexion = conectar()
print("Conexion exitosa")
conexion.close()