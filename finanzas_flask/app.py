from flask import Flask, render_template, request, redirect, url_for, flash
from database import *

app = Flask(__name__)
app.secret_key = 'string_Secreto'

@app.route('/')
def index():
    ingresos, gastos = calcular_balance()
    return render_template('index.html', ingresos = ingresos, gastos = gastos)


@app.route('/transacciones')
def transacciones():
    datos = obtener_transacciones()
    return render_template('transacciones.html', transacciones = datos)

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        monto = float(request.form['monto'])
        fecha = request.form['fecha']
        tipo = request.form['tipo']
        categoria_id = int(request.form['categoria_id'])
        registrar_transaccion(descripcion, monto, fecha, tipo, categoria_id)
        flash('Transacción registrada correctamente', 'success')
        return redirect(url_for('transacciones'))
    
    categorias = obtener_categorias()
    return render_template('registrar.html', categorias = categorias)

@app.route('/categorias', methods=['GET', 'POST'])
def categorias():
    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        registrar_categoria(nombre, tipo)
        flash('Categoría registrada correctamente', 'success')
        return redirect(url_for('categorias'))

    categorias = obtener_categorias()
    return render_template('categorias.html', categorias=categorias)

if __name__ == '__main__':
    app.run(debug=True)