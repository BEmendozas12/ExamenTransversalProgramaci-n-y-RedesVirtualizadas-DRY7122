from flask import Flask, request, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)
DB = 'usuarios.db'

# Crear la base de datos y la tabla usuarios si no existen
def crear_base_datos():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        conn.commit()

# Insertar usuario con contraseña hasheada
def insertar_usuario(nombre, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    try:
        with sqlite3.connect(DB) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)", (nombre, password_hash))
            conn.commit()
    except sqlite3.IntegrityError:
        print(f"El usuario '{nombre}' ya existe.")

# Validar usuario y contraseña
def validar_usuario(nombre, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND password_hash = ?", (nombre, password_hash))
        return cursor.fetchone() is not None

# Crear base de datos y agregar usuarios (modifica con los nombres y contraseñas que quieran)
crear_base_datos()
insertar_usuario("Charmayne", "clave1")
insertar_usuario("Lucila", "clave2")
insertar_usuario("Benjamin", "clave3")
insertar_usuario("Alejandra", "clave4")

# HTML básico para login
login_html = '''
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Ingreso de Usuarios</h2>
    <form method="POST">
        Nombre: <input type="text" name="nombre" required><br>
        Contraseña: <input type="password" name="password" required><br>
        <button type="submit">Ingresar</button>
    </form>
    {% if mensaje %}
    <p style="color:red;">{{ mensaje }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ""
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        if validar_usuario(nombre, password):
            mensaje = f"¡Bienvenido, {nombre}!"
        else:
            mensaje = "Usuario o contraseña incorrectos."
    return render_template_string(login_html, mensaje=mensaje)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800)
