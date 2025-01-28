from flask import Flask, render_template, redirect, request, flash, url_for
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "LEANDRO"

@app.route('/')   #<<--- rota para direcionar pagina de entrada do site "('/')"
def home():
    return render_template('rotavendas.html')

@app.route('/cadastro.html')   #<<--- rota para direcionar para a página de cadastro
def cadastro_page():
    return render_template('cadastro.html')

@app.route('/login_cliente.html')   #<<--- rota para direcionar para a página de login do cliente
def login_cliente_page():
    return render_template('login_cliente.html')

@app.route('/usuario', methods=['POST'])   #<<--- rota para direcionar para a página de login do cliente
def login_home_usuario():
    return render_template('usuario.html')

@app.route('/usuario', methods=['POST']) #<<--- aqui é uma rota para pagina para fazer o login "('/login')"
def login_cliente():
    nome = request.form.get('nome')#  ATENÇÃO É APARTIR DAQUI QUE VAI SER A ALTERAÇÃO  <<<<<<<<<<<<<<<<<<<<<<<<<<-------------------------
    senha = request.form.get('senha')

    with open('usuario.json') as usuariotemp :# "whith open" para mostrar o caminho para achar a lista do banco de dados
        usuarios = json.load(usuariotemp)
        
        # Validando as login e senha do usuário
        for usuario in usuarios:
            if usuario['nome'] == nome and usuario['senha'] == senha:
                return render_template('usuario.html', nome)
            
        flash('USUÁRIO INVÁLIDO')
        return redirect(url_for('login_cliente'))

@app.route('/cadastro', methods=['POST']) #<<--- aqui é uma rota para pagina para fazer o login "('/cadastro')"
def cadastro():
    user = []
    nome = request.form.get('nome')
    sobrenome = request.form.get('sobrenome')
    nascimento = request.form.get('nascimento')
    cpf = request.form.get('cpf')
    email = request.form.get('email')
    senha = request.form.get('senha')
    user = [
            {
                "nome": nome,
                "sobrenome": sobrenome,
                "nascimento": nascimento,
                "cpf": cpf,
                "email": email,
                "senha": senha
            }
        ]
    with open('usuario.json') as usuariotemp :# "whith open" para mostrar o caminho para achar a lista do banco de dados
        usuarios = json.load(usuariotemp)

    usuario_novo = user + usuarios

    with open('usuario.json', 'w') as gravartemp :# "whith open" para mostrar o caminho para achar a lista do banco de dados
        json.dump(usuario_novo, gravartemp, indent=9)

    flash('Cadastro realizado com sucesso!')
    return redirect('/login_cliente.html')

@app.route('/rotavendas.html')
def rotavendas():
    return render_template('rotavendas.html')

if __name__ == '__main__' :
    app.run(debug=True)