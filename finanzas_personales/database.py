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
