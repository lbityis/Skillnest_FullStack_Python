# ==========================================================
# SERVIDOR FLASK
# ==========================================================
from flask import Flask, render_template
from mascota import Mascota

# ==========================================================
# CREAR APLICACIÓN
# ==========================================================
app = Flask(__name__)

# ==========================================================
# RUTA PRINCIPAL (TODAS LAS MASCOTAS)
# ==========================================================
@app.route("/")
def index():
    """
    Consulta todas las mascotas y las envía
    hacia la plantilla index.html.
    """
    mascotas = Mascota.get_all()
    print(mascotas)
    return render_template("index.html", todas_mascotas=mascotas)

# ==========================================================
# RUTA FILTRADA (DESAFÍO: SOLO PERROS)
# ==========================================================
@app.route("/mascotas/perros")
def ver_perros():
    """
    Consulta únicamente las mascotas de tipo 'Perro'
    y las envía hacia la plantilla index.html.
    """
    perros = Mascota.get_by_tipo("Perro")
    return render_template("index.html", todas_mascotas=perros)

# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================
if __name__ == "__main__":
    app.run(debug=True)