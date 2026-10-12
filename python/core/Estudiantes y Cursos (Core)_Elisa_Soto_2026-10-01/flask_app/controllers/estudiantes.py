from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/estudiantes/nuevo")
def formulario_estudiante():
    # Cargar todos los cursos para la lista desplegable
    lista_cursos = Curso.obtener_todos()
    return render_template("nuevo_estudiante.html", cursos=lista_cursos)

@app.route("/estudiantes/crear", methods=["POST"])
def guardar_estudiante():
    nombre = request.form.get("nombre", "").strip()
    apellido = request.form.get("apellido", "").strip()
    edad = request.form.get("edad", "").strip()
    curso_id = request.form.get("curso_id", "").strip()

    # Validaciones basicas antes de guardar
    if nombre and apellido and edad and curso_id:
        datos = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": int(edad),
            "curso_id": int(curso_id)
        }
        Estudiante.guardar(datos)

    return redirect(url_for("ver_cursos"))