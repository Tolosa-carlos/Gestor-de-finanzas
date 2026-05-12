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