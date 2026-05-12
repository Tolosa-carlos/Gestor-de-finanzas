from database import conectar, obtener_categorias, registrar_transaccion

conexion = conectar()
print("Conexion exitosa")
conexion.close()

categorias = obtener_categorias()
for categoria in categorias:
    print(f"{categoria[0]} - {categoria[1]} ({categoria[2]})")

registrar_transaccion("Regalo", 2000, "2026-05-12", "gasto", 1)
