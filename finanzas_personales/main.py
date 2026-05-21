import csv
from database import *

def menu():
    print("\n=== FINANZAS PERSONALES ===\n" \
    "1. Registrar transacción.\n" \
    "2. Ver transacciones.\n" \
    "3. Ver balance.\n" \
    "4. Filtrar por categoría\n" \
    "5. Exportar transacciones a CSV\n" \
    "6. Salir\n")

def lista_transacciones():
    print("\n=== LISTA DE TRANSACCIONES ===")
    transacciones = obtener_transacciones()
    for transaccion in transacciones:
        print(f"{transaccion[2]} - {transaccion[1]} - ${transaccion[3]} - {transaccion[4]} - {transaccion[0]}")
    print("\n")

def mostrar_categorias():
    print("\n=== LISTA DE CATEGORIAS ===")
    categorias = obtener_categorias()
    for categoria in categorias:
        print(f"{categoria[0]} - {categoria[1]} ({categoria[2]})")
    print("\n")

def exportar_csv():
    transacciones = obtener_transacciones()
    with open('transacciones.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Descripción", "Categoría", "Fecha", "Monto", "Tipo", "ID"])
        for transaccion in transacciones:
            writer.writerow(transaccion)


conexion = conectar()
print("Conexion exitosa")
conexion.close()

while True:
    menu()

    while True:
        try:
            opc = int(input("Seleccione una opción: "))
            if opc in [1, 2, 3, 4, 5, 6]:
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("La opción debe ser un número. Intente nuevamente.")

    if opc == 1:
        descripcion = input("\nDescripción: ")

        while True:
            try:
                monto = float(input("\nMonto: $"))
                break
            except ValueError:
                print("El monto debe ser un número. Intente nuevamente.")
        
        fecha = input("\nFecha (YYYY-MM-DD): ")
        tipo = input("\nTipo de transacción (ingreso/gasto): ")
        mostrar_categorias()

        while True:
            try:
                categoria_id = int(input("\nCategoría (ID): "))
                break
            except ValueError:
                print("El ID de la categoría debe ser un número. Intente nuevamente.")  

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

        while True:
            try:
                categoria_a_buscar = int(input("\nIngrese el ID de la categoría a filtrar: "))
                break
            except ValueError:
                print("El ID de la categoría debe ser un número. Intente nuevamente.")

        resultados = obtener_transacciones_por_categoria(categoria_a_buscar)
        for resultado in resultados:
            print(f"{resultado[1]} - {resultado[0]} - {resultado[2]} - {resultado[3]}")
        print("\n")

    elif opc == 5:
        exportar_csv()

    elif opc == 6:
        print("\nSaliendo del programa...")
        break


