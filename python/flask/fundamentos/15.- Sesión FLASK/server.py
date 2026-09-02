# ==========================================
# IMPORTACIONES
# ==========================================
from flask import Flask, render_template, request, redirect, session


# ==========================================
# CREAR APLICACIÓN Y CONFIGURACIÓN
# ==========================================
app = Flask(__name__)

# Clave secreta para firmar las cookies de sesión
app.secret_key = "una-clave-secreta-para-desarrollo"


# ==========================================
# RUTAS DE LA APLICACIÓN
# ==========================================

@app.route("/")
def index():
    """Muestra el formulario principal."""
    return render_template("index.html")


@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    """
    Recibe el formulario (Nombre, Email, Ciudad) mediante POST
    y guarda los datos en la sesión antes de redirigir.
    """
    # 1. Obtener datos de la solicitud actual
    nombre = request.form["nombre"]
    email = request.form["email"]
    ciudad = request.form["ciudad"]

    # 2. Guardar datos en la sesión para persistencia entre HTTP requests
    session["nombre_usuario"] = nombre
    session["email_usuario"] = email
    session["ciudad_usuario"] = ciudad

    # 3. Redirección para evitar el reenvío de formulario al recargar (Patrón POST-Redirect-GET)
    return redirect("/mostrar_usuario")


@app.route("/mostrar_usuario")
def mostrar_usuario():
    """
    Ruta a la que llega el usuario tras la redirección.
    Lee de la sesión y renderiza la plantilla de confirmación.
    """
    return render_template("mostrar.html")


@app.route("/perfil")
def perfil():
    """
    Desafío adicional: Ruta que muestra una tarjeta de perfil
    obteniendo la información exclusivamente desde 'session'.
    """
    return render_template("perfil.html")


# ==========================================
# EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)