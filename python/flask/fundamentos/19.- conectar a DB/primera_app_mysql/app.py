# ==========================================================
# SERVIDOR FLASK + MYSQL
# ==========================================================
from flask import Flask, render_template
from mascota import Mascota
from usuario import Usuario

app = Flask(__name__)

# ==========================================================
# RUTAS DE MASCOTAS
# ==========================================================
@app.route("/")
def index():
    """
    Lista todas las mascotas.
    """
    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas)

@app.route("/mascota/<int:id>")
def detalle_mascota(id):
    """
    Muestra el detalle de una mascota específica (Desafío).
    """
    mascota = Mascota.get_by_id(id)
    return render_template("detalle_mascota.html", mascota=mascota)

# ==========================================================
# RUTAS DE USUARIOS
# ==========================================================
@app.route("/usuarios")
def lista_usuarios():
    """
    Lista todos los usuarios (Ejercicio de consolidación).
    """
    usuarios = Usuario.get_all()
    return render_template("usuarios.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)