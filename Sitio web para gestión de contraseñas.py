# servidor_web.py
from flask import Flask, request
import hashlib, sqlite3

app = Flask(__name__)

# Crear o conectar base de datos
conexion = sqlite3.connect('usuarios.db', check_same_thread=False)
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, clave_hash TEXT)")

# Crear usuarios
usuarios = {"Lucila": "Duoc2025", "Charmayne": "Duoc2025", "Alejandra": "Duoc2025", "Benjamin": "Duoc2025"}
for nombre, clave in usuarios.items():
    clave_hash = hashlib.sha256(clave.encode()).hexdigest()
    cursor.execute("INSERT INTO usuarios VALUES (?, ?)", (nombre, clave_hash))
conexion.commit()

# Ruta para validar acceso
@app.route('/login', methods=['POST'])
def login():
    datos = request.json
    nombre = datos['usuario']
    clave_hash = hashlib.sha256(datos['clave'].encode()).hexdigest()
    cursor.execute("SELECT * FROM usuarios WHERE nombre=? AND clave_hash=?", (nombre, clave_hash))
    if cursor.fetchone():
        return {"estado": "Acceso permitido"}
    else:
        return {"estado": "Acceso denegado"}

app.run(port=7500)
