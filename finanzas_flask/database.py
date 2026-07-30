import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "finanzas_personales"
    )
    return conexion

def obtener_categorias():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, tipo FROM categorias")
    categorias = cursor.fetchall()
    cursor.close()
    conexion.close()
    return categorias

def registrar_transaccion(descripcion, monto, fecha, tipo, categoria_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO transacciones (descripcion, monto, fecha, tipo, categoria_id) VALUES (%s, %s, %s, %s, %s)", (descripcion, monto, fecha, tipo, categoria_id))
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_transacciones():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT transacciones.descripcion, categorias.nombre, transacciones.fecha, transacciones.monto, transacciones.tipo, categorias.id " \
    "FROM transacciones " \
    "JOIN categorias ON transacciones.categoria_id = categorias.id")
    transacciones = cursor.fetchall()
    cursor.close()
    conexion.close()
    return transacciones

def calcular_balance():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT tipo, SUM(monto) FROM transacciones GROUP BY tipo")
    totales = cursor.fetchall()
    total_ingresos, total_gastos = 0, 0
    for total in totales:
        if total[0] == "ingreso":
            total_ingresos = total[1]
        elif total[0] == "gasto":
            total_gastos = total[1]
    cursor.close()
    conexion.close()
    return total_ingresos, total_gastos    

def obtener_transacciones_por_categoria(categoria):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT transacciones.descripcion, categorias.nombre, transacciones.fecha, transacciones.monto " \
    "FROM transacciones " \
    "JOIN categorias ON categoria_id = categorias.id " \
    "WHERE categoria_id = %s", (categoria,))
    transacciones = cursor.fetchall()
    cursor.close()
    conexion.close()
    return transacciones

def obtener_gastos_por_categoria():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT categorias.nombre, " \
    "SUM(monto) " \
    "FROM transacciones " \
    "JOIN categorias " \
    "ON transacciones.categoria_id = categorias.id " \
    "WHERE transacciones.tipo = 'gasto' "
    "GROUP BY categorias.nombre")
    gastos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return gastos

def registrar_categoria(nombre, tipo):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO categorias (nombre, tipo) VALUES (%s, %s)", (nombre, tipo))
    conexion.commit()
    cursor.close()
    conexion.close()

