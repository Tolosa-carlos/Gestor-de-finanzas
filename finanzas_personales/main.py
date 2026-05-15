from database import *

conexion = conectar()
print("Conexion exitosa")
conexion.close()

print("--- LISTA DE CATEGORIAS ---")
categorias = obtener_categorias()
for categoria in categorias:
    print(f"{categoria[0]} - {categoria[1]} ({categoria[2]})")
print("\n")

print("--- LISTA DE TRANSACCIONES ---")
transacciones = obtener_transacciones()
for transaccion in transacciones:
    print(f"{transaccion[2]} - {transaccion[1]} - ${transaccion[3]} - {transaccion[4]} - {transaccion[0]}")
print("\n")

ingresos, gastos = calcular_balance()
print(f"Ingresos: ${ingresos}")
print(f"Gastos: ${gastos}")
print(f"Balance: ${ingresos-gastos}\n")

resultados = obtener_transacciones_por_categoria(3)
for resultado in resultados:
    print(f"{resultado[1]} - {resultado[0]} - {resultado[2]} - {resultado[3]}")
print("\n")



