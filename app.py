from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de consultas
consultas = []

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para exibir todas as consultas
@app.route('/consultas')
def listar_consultas():
    return render_template('consultas.html', consultas=consultas)

# Rota para agendar uma nova consulta
@app.route('/agendar', methods=['GET', 'POST'])
def agendar_consulta():
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['data']
        horario = request.form['horario']
        consulta = {'nome': nome, 'data': data, 'horario': horario}
        consultas.append(consulta)
        return redirect('/consultas')
    return render_template('agendar.html')

# Rota para editar uma consulta existente
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_consulta(id):
    consulta = consultas[id]
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['data']
        horario = request.form['horario']
        consulta['nome'] = nome
        consulta['data'] = data
        consulta['horario'] = horario
        return redirect('/consultas')
    return render_template('editar.html', consulta=consulta)

# Rota para cancelar uma consulta existente
@app.route('/cancelar/<int:id>')
def cancelar_consulta(id):
    consultas.pop(id)
    return redirect('/consultas')

if __name__ == '__main__':
    app.run(debug=True)
