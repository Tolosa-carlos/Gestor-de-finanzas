from database import *

def menu():
    print("=== FINANZAS PERSONALES ===\n" \
    "1. Registrar transacción.\n" \
    "2. Ver transacciones.\n" \
    "3. Ver balance.\n" \
    "4. Filtrar por categoría\n" \
    "5. Salir\n")

def lista_transacciones():
    print("=== LISTA DE TRANSACCIONES ===")
    transacciones = obtener_transacciones()
    for transaccion in transacciones:
        print(f"{transaccion[2]} - {transaccion[1]} - ${transaccion[3]} - {transaccion[4]} - {transaccion[0]}")
    print("\n")

def mostrar_categorias():
    print("--- LISTA DE CATEGORIAS ---")
    categorias = obtener_categorias()
    for categoria in categorias:
        print(f"{categoria[0]} - {categoria[1]} ({categoria[2]})")
    print("\n")




conexion = conectar()
print("Conexion exitosa")
conexion.close()

while True:
    menu()
    opc = int(input("Seleccione una opción: "))
    if opc == 1:
        descripcion = input("\nDescripción: ")
        monto = float(input("\nMonto: "))
        fecha = input("\nFecha (YYYY-MM-DD): ")
        tipo = input("\nTipo de transacción (ingreso/gasto): ")
        mostrar_categorias()
        categoria_id = int(input("\nCategoría (ID): "))
        registrar_transaccion(descripcion, monto, fecha, tipo,categoria_id)

    elif opc == 2:
        lista_transacciones()

    elif opc == 3:
        ingresos, gastos = calcular_balance()
        print(f"Ingresos: ${ingresos}")
        print(f"Gastos: ${gastos}")
        print(f"Balance: ${ingresos-gastos}\n")

    elif opc == 4:
        mostrar_categorias()
        categoria_a_buscar = int(input("\nIngrese el ID de la categoría a filtrar: "))
        resultados = obtener_transacciones_por_categoria(categoria_a_buscar)
        for resultado in resultados:
            print(f"{resultado[1]} - {resultado[0]} - {resultado[2]} - {resultado[3]}")
        print("\n")

    elif opc == 5:
        print("Saliendo del programa...")
        break


