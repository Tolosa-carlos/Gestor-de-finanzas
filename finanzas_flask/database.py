import mysql.connector
from dotenv import load_dotenv
import os
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

def conectar():
    conexion = mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DB_NAME'),
        use_pure=True
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

def obtener_transacciones(usuario_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT transacciones.id, transacciones.descripcion, categorias.nombre, transacciones.fecha, transacciones.monto, transacciones.tipo " \
    "FROM transacciones " \
    "JOIN categorias ON transacciones.categoria_id = categorias.id " \
    "WHERE transacciones.usuario_id = %s " \
    "ORDER BY transacciones.fecha DESC", (usuario_id,))
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

def eliminar_categoria(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM categorias WHERE id = %s", (id,))
    conexion.commit()
    cursor.close()
    conexion.close()

def categoria_tiene_transacciones(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM transacciones WHERE categoria_id = %s", (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()
    return resultado[0]

def obtener_categoria(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, tipo FROM categorias WHERE id = %s", (id,))
    categoria = cursor.fetchone()
    cursor.close()
    conexion.close()
    return categoria

def actualizar_categoria(id, tipo, nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE categorias SET nombre = %s, tipo = %s WHERE id = %s", (nombre, tipo, id))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_transaccion(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM transacciones WHERE id = %s", (id,))
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_transaccion(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT fecha, categoria_id, descripcion, monto, tipo FROM transacciones WHERE id = %s", (id,))
    transaccion = cursor.fetchone()
    cursor.close()
    conexion.close()
    return transaccion

def actualizar_transaccion(id, fecha, categoria, descripcion, monto, tipo):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE transacciones SET fecha = %s, categoria_id = %s, descripcion = %s, monto = %s, tipo = %s WHERE id = %s" , (fecha, categoria, descripcion, monto, tipo, id))
    conexion.commit()
    cursor.close()
    conexion.close()

def registrar_usuario(usuario, contrasena):
    conexion = conectar()
    cursor = conexion.cursor()
    password_hash = generate_password_hash(contrasena)
    cursor.execute("INSERT INTO usuarios(username, password) VALUES (%s, %s)", (usuario, password_hash))
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_usuario(usuario):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, username, password FROM usuarios WHERE username = %s", (usuario, ))
    user = cursor.fetchone()
    cursor.close()
    conexion.close()
    return user