from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.curso import Curso

@app.route("/")
def home():
    return redirect(url_for("ver_cursos"))

@app.route("/cursos")
def ver_cursos():
    lista_cursos = Curso.obtener_todos()
    return render_template("cursos.html", cursos=lista_cursos)

@app.route("/cursos/crear", methods=["POST"])
def crear_nuevo_curso():
    nombre = request.form.get("nombre", "").strip()
    
    if nombre:
        Curso.guardar({"nombre": nombre})
        
    return redirect(url_for("ver_cursos"))

@app.route("/cursos/<int:id>")
def detalle_curso(id):
    curso_info = Curso.obtener_con_estudiantes(id)
    if not curso_info:
        return redirect(url_for("ver_cursos"))
    return render_template("mostrar_curso.html", curso=curso_info)