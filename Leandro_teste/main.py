from flask import Flask, render_template, redirect, request, flash
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "LEANDRO"

@app.route('/')   #<<--- rota para direcionar pagina de entrada do site "('/')"
def home():

    return render_template ('login_cliente.html')

@app.route('/login_cliente', methods=['POST']) #<<--- aqui é uma rota para pagina para fazer o login "('/login')"
def login():
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    with open('usuario.json') as usuariotemp :# "whith open" para mostrar o caminho para achar a lista do banco de dados
        usuarios = json.load(usuariotemp)
        
        # Validando as login e senha do usuário
        for usuario in usuarios:
            if usuario['nome'] == nome and usuario['senha'] == senha:

                return render_template('home.html')
            
        flash('USUÁRIO INVÁLIDO')
        return redirect('/')

if __name__ == '__main__' :
    app.run(debug=True)