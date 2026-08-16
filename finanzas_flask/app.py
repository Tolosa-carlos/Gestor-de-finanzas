from flask import Flask, render_template, request, redirect, url_for, flash
from database import *
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Necesitas iniciar sesion para acceder'
login_manager.login_message_category = 'warning'
class Usuario(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def cargar_usuario(usuario_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, username FROM usuarios WHERE id = %s", (usuario_id, ))
    usuario = cursor.fetchone()
    cursor.close()
    conexion.close()
    if usuario:
        return Usuario(usuario[0], usuario[1])
    return None

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usuario = obtener_usuario(username)
        if usuario and check_password_hash(usuario[2], password):
            user_obj = Usuario(usuario[0], usuario[1])
            login_user(user_obj)
            return redirect(url_for('index'))
        flash('Usuario o contraseña incorrectas', 'danger')
    return render_template('login.html')

@app.route('/registro', methods = ['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        registrar_usuario(username, password)
        flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('login'))
    return render_template('registro.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    print(f"Usuario autenticado: {current_user.is_authenticated}")
    ingresos, gastos = calcular_balance()
    return render_template('index.html', ingresos = ingresos, gastos = gastos)

@app.route('/transacciones')
@login_required
def transacciones():
    print(f"ID del usuario actual: {current_user.id}")
    datos = obtener_transacciones(current_user.id)
    return render_template('transacciones.html', transacciones = datos)

@app.route('/registrar', methods=['GET', 'POST'])
@login_required
def registrar():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        monto = float(request.form['monto'])
        fecha = request.form['fecha']
        tipo = request.form['tipo']
        categoria_id = int(request.form['categoria_id'])
        registrar_transaccion(descripcion, monto, fecha, tipo, categoria_id, current_user.id)
        flash('Transacción registrada correctamente', 'success')
        return redirect(url_for('transacciones'))
    
    categorias = obtener_categorias(current_user.id)
    return render_template('registrar.html', categorias = categorias)

@app.route('/categorias', methods=['GET', 'POST'])
@login_required
def categorias():
    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        registrar_categoria(nombre, tipo, current_user.id)
        flash('Categoría registrada correctamente', 'success')
        return redirect(url_for('categorias'))

    categorias = obtener_categorias(current_user.id)
    return render_template('categorias.html', categorias=categorias)

@app.route('/categorias/eliminar/<int:id>', methods=['POST'])
def eliminar_cat(id):
    if categoria_tiene_transacciones(id) > 0:
        flash('No se puede eliminar. La categoría tiene transacciones asociadas.', 'danger')
    else:
        eliminar_categoria(id)
        flash('Categoría eliminada correctamente', 'success')
    return redirect(url_for('categorias'))

@app.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
def editar_categoria(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        tipo = request.form['tipo']
        actualizar_categoria(id, tipo, nombre)
        flash('Categoría actualizada correctamente', 'success')
        return redirect(url_for('categorias'))

    categoria = obtener_categoria(id)
    return render_template('editar_categoria.html', categoria=categoria, id=id)

@app.route('/transacciones/eliminar/<int:id>', methods=['POST'])
def eliminar_trans(id):
    eliminar_transaccion(id)
    flash('Transacción eliminada correctamente', 'success')
    return redirect(url_for('transacciones'))

@app.route('/transacciones/editar/<int:id>', methods=['GET', 'POST'])
def editar_transaccion(id):
    if request.method == 'POST':
        fecha = request.form['fecha']
        categoria = request.form['categoria_id']
        descripcion = request.form['descripcion']
        monto = request.form['monto']
        tipo = request.form['tipo']
        actualizar_transaccion(id, fecha, categoria, descripcion, monto, tipo)
        flash('Transacción actualizada correctamente', 'success')
        return redirect(url_for('transacciones'))

    transaccion = obtener_transaccion(id)
    categorias = obtener_categorias(current_user.id)
    return render_template('editar_transaccion.html', transaccion=transaccion, categorias=categorias, id=id)

if __name__ == '__main__':
    app.run(debug=True)