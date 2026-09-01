from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secreto"

@app.route('/')
def index():
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 1

    if 'reinicios' not in session:
        session['reinicios'] = 0

    return render_template('index.html')

@app.route('/sumar2', methods=['POST'])
def sumar2():
    if 'visitas' in session:
        session['visitas'] += 1
    else:
        session['visitas'] = 2
    return redirect('/')

@app.route('/sumar_num', methods=['POST'])
def sumar_num():
    if 'visitas' in session:
        num = int(request.form['cantidad'])
        session['visitas'] += (num - 1)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['visitas'] = -1
    
    if 'reinicios' in session:
        session['reinicios'] += 1
    else:
        session['reinicios'] = 1
        
    return redirect('/')

@app.route('/destruir_sesion')
def destruir_sesion():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)