from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bienvenidooooooooooooooooo"

@app.route("/nosotros")
def nosotros():
    return "¡conócenos un poco más!"

@app.route("/color/<nombre>/<color>")
def color(nombre, color):
    return f"Hola {nombre}, tu color favorito es {color}"

@app.route("/saludo/<nombre>/<int:veces>")
def repetir(nombre, veces):
    return f"¡Hola {nombre}!" * veces

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return "<h2>Lo sentimos, esta ruta no existe. ¡Vuelve al inicio!</h2>", 404

if __name__ == "__main__":
    app.run(debug=True)

"""
1. Código HTTP 500: El código 500 significa que la página web se rompió por un problema
 interno en su propio servidor. Es un error genérico: algo falló adentro (como el código
 o la base de datos), pero el servidor no te dice exactamente qué pasó.
2. Diferencia entre 401 y 403: El error 401 significa que el sistema no sabe quién eres,
 así que primero debes iniciar sesión. El error 403 significa que el sistema ya sabe quién
 eres, pero tu usuario no tiene permiso para entrar a esa sección.
3. Código HTTP en Flask: Cuando una página carga con éxito, Flask devuelve automáticamente el 
código 200 OK. No hace falta que escribas nada en tu código; si la página funciona bien,
 Flask envía este número por defecto para avisar que todo está correcto."""