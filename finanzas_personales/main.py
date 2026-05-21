import csv
import matplotlib.pyplot as plt
from database import *

def menu():
    print("\n=== FINANZAS PERSONALES ===\n" \
    "1. Registrar transacción.\n" \
    "2. Ver transacciones.\n" \
    "3. Ver balance.\n" \
    "4. Filtrar por categoría\n" \
    "5. Exportar transacciones a CSV\n" \
    "6. Mostrar gráfico de gastos\n" \
    "7. Salir\n")

def menu_graficos():
    print("\n === GRÁFICO DE GASTOS ===\n" \
    "1. Gráfico de torta.\n" \
    "2. Gráfico de barras verticales.\n" \
    "3. Gráfico de barras horizontales.\n" \
    "4. Gráfico de líneas.\n" \
    "5. Volver al menú principal.\n")

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

def mostrar_grafico_gastos():
    gastos = obtener_gastos_por_categoria()
    nombres = []
    montos = []
    for fila in gastos:
        nombres.append(fila[0])
        montos.append(fila[1])

    while True:
        menu_graficos()

        while True:
            try:
                opc_grafico = int(input("Seleccione una opción: "))

                if opc_grafico in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                print("La opción debe ser un número. Intente nuevamente.")

        if opc_grafico == 1:
            plt.pie(montos, labels=nombres, autopct='%1.1f%%')
            plt.title('Gastos por Categoría')
            plt.show()
            break
        
        elif opc_grafico == 2:
            plt.bar(nombres, montos, color=['steelblue', 'orange'])
            plt.title('Gastos por Categoría')
            plt.xlabel('Categoría')
            plt.ylabel('Monto')
            plt.show()
            break

        elif opc_grafico == 3:
            plt.barh(nombres, montos, color=['steelblue', 'orange'])
            plt.title('Gastos por Categoría')
            plt.xlabel('Monto')
            plt.ylabel('Categoría')
            plt.show()
            break
        
        elif opc_grafico == 4:
            plt.plot(nombres, montos, marker='o', color='steelblue')
            plt.title('Gastos por Categoría')
            plt.xlabel('Categoría')
            plt.ylabel('Monto')
            plt.show()
            break

        elif opc_grafico == 5:
            break

    

conexion = conectar()
print("Conexion exitosa")
conexion.close()

while True:
    menu()

    while True:
        try:
            opc = int(input("Seleccione una opción: "))
            if opc in [1, 2, 3, 4, 5, 6, 7]:
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
        mostrar_grafico_gastos()

    elif opc == 7:
        print("\nSaliendo del programa...")
        break


