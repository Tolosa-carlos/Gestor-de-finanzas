from flask import Flask, render_template
from database import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola desde Flask!'


@app.route('/transacciones')
def transacciones():
    datos = obtener_transacciones()
    return render_template('transacciones.html', transacciones = datos)

if __name__ == '__main__':
    app.run(debug=True)