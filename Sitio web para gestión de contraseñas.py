from flask import Flask, request, redirect, render_template_string
import sqlite3
import hashlib

# Crear la base de datos SQLite
def crear_base_datos():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Insertar usuarios (nombres de los integrantes + contraseña)
def insertar_usuario(nombre, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    try:
        with sqlite3.connect('usuarios.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)', (nombre, password_hash))
            conn.commit()
    except sqlite3.IntegrityError:
        print(f"El usuario '{nombre}' ya existe.")


# Validar credenciales
def validar_usuario(nombre, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE nombre = ? AND password_hash = ?', (nombre, password_hash))
        usuario = cursor.fetchone()
    return usuario is not None


# Crear la base y añadir usuarios (integrantes del examen)
crear_base_datos()
# Cambia los nombres y contraseñas según los integrantes reales:
insertar_usuario("benjamin", "clave123")
insertar_usuario("lucila", "secreto456")
insertar_usuario("Charmayne", "password789")

# Crear la app Flask
app = Flask(__name__)

# HTML sencillo de inicio de sesión
login_html = '''
<!DOCTYPE html>
<html>
<head><title>Login de Usuarios</title></head>
<body>
    <h2>Inicio de Sesión</h2>
    <form method="POST">
        Nombre: <input type="text" name="nombre"><br>
        Contraseña: <input type="password" name="password"><br>
        <button type="submit">Ingresar</button>
    </form>
    {% if mensaje %}
    <p>{{ mensaje }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        if validar_usuario(nombre, password):
            mensaje = f'¡Bienvenido, {nombre}!'
        else:
            mensaje = 'Credenciales incorrectas.'
    return render_template_string(login_html, mensaje=mensaje)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800, debug=True)
