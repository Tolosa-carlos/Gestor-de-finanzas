# 💰 Gestor de Finanzas Personales

Aplicación para registrar y gestionar ingresos y gastos personales. Disponible en dos versiones: una interfaz web moderna y una aplicación de consola.

Desarrollado con Python y MySQL como base de datos.

---

## 📦 Versiones

| Versión | Descripción | Carpeta |
|---|---|---|
| 🌐 Web | Interfaz en el navegador con Flask y Bootstrap | `finanzas_flask/` |
| 🖥️ Consola | Menú interactivo en terminal con gráficos | `finanzas_personales/` |

---

## 🛠️ Tecnologías

**Versión Web**
- Python 3.x
- Flask
- Bootstrap 5
- MySQL (XAMPP)
- mysql-connector-python

**Versión Consola**
- Python 3.x
- MySQL (XAMPP)
- mysql-connector-python
- matplotlib

---

## ⚙️ Requisitos previos

- [Python 3.x](https://www.python.org/downloads/)
- [XAMPP](https://www.apachefriends.org/) con MySQL activo
- [MySQL Workbench](https://www.mysql.com/products/workbench/) (opcional)

---

## 🗄️ Configuración de la base de datos

Ejecutá el siguiente script en MySQL Workbench antes de correr cualquiera de las dos versiones:

```sql
CREATE DATABASE IF NOT EXISTS finanzas_personales
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE finanzas_personales;

CREATE TABLE categorias (
    id     INT          NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(50)  NOT NULL UNIQUE,
    tipo   ENUM('ingreso','gasto','ambos') NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE transacciones (
    id           INT            NOT NULL AUTO_INCREMENT,
    descripcion  VARCHAR(100)   NOT NULL,
    monto        DECIMAL(10,2)  NOT NULL CHECK (monto > 0),
    fecha        DATE           NOT NULL,
    tipo         ENUM('ingreso','gasto') NOT NULL,
    categoria_id INT            NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);
```

---

## 🚀 Instalación y uso

### 🌐 Versión Web

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/Tolosa-carlos/Gestor-de-finanzas.git
   cd Gestor-de-finanzas/finanzas_flask
   ```

2. Instalá las dependencias:
   ```bash
   pip install flask mysql-connector-python
   ```

3. Asegurate de tener XAMPP corriendo con MySQL activo.

4. Ejecutá la aplicación:
   ```bash
   python app.py
   ```

5. Abrí el navegador en `http://localhost:5000`

---

### 🖥️ Versión Consola

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/Tolosa-carlos/Gestor-de-finanzas.git
   cd Gestor-de-finanzas/finanzas_personales
   ```

2. Instalá las dependencias:
   ```bash
   pip install mysql-connector-python matplotlib
   ```

3. Asegurate de tener XAMPP corriendo con MySQL activo.

4. Ejecutá la aplicación:
   ```bash
   python main.py
   ```

---

## ✨ Funcionalidades

### Transacciones
- Registrar ingresos y gastos con descripción, monto, fecha, tipo y categoría.
- Listar todas las transacciones.
- Editar una transacción existente.
- Eliminar una transacción.
- Filtrar transacciones por categoría.
- Exportar transacciones a CSV *(consola)*

### Categorías
- Listar categorías con su tipo (ingreso / gasto / ambos).
- Agregar nuevas categorías.
- Editar una categoría existente.
- Eliminar categorías con validación — no se puede eliminar si tiene transacciones asociadas.

### Dashboard / Balance
- Resumen del saldo actual, ingresos y gastos totales. 

### Gráficos *(consola)*
Visualización de gastos por categoría en 4 formatos:
- Torta.
- Barras verticales.
- Barras horizontales.
- Líneas.

---

## 📁 Estructura del proyecto

```
Gestor-de-finanzas/
│
├── finanzas_flask/                    # Versión web
│   ├── app.py                         # Rutas y lógica Flask
│   ├── database.py                    # Conexión y consultas a MySQL
│   └── templates/
│       ├── base.html                  # Template base con navbar
│       ├── index.html                 # Dashboard con balance
│       ├── transacciones.html         # Lista de transacciones
│       ├── registrar.html             # Formulario de registro
│       ├── editar_transaccion.html    # Formulario para editar una transaccion
│       ├── categorias.html            # Lista y alta de categorías
│       └── editar_categoria.html      # Formulario para editar una categoría
│
└── finanzas_personales/               # Versión consola
    ├── main.py                        # Menú interactivo
    └── database.py                    # Conexión y consultas a MySQL
```

---

## 👤 Autor

**Carlos Walker Tolosa Fernandez Stoll**  
Estudiante de Ingeniería en Sistemas de Información — UTN FRBA  
[LinkedIn](www.linkedin.com/in/carlos-walker-tolosa-fernandez-stoll) · [GitHub](https://github.com/Tolosa-carlos)
