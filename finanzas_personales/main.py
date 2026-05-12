from database import conectar, obtener_categorias

conexion = conectar()
print("Conexion exitosa")
conexion.close()

categorias = obtener_categorias()
for categoria in categorias:
    print(f"{categoria[0]} - {categoria[1]} ({categoria[2]})")
