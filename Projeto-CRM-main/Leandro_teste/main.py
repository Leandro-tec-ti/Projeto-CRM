from flask import Flask, render_template, redirect, request, flash, url_for
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "LEANDRO"

@app.route('/')   #<<--- rota para direcionar pagina de entrada do site "('/')"
def home():
    return render_template('Lirioshome.html')

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
            if usuario == 'admin' and senha == '000':
                return render_template('usuarioadmin.html')
            
            elif usuario != 'admin' and senha != 000:
                return render_template('login_cliente.html')
            
            elif usuario['nome'] == nome and usuario['senha'] == senha:
                return render_template('usuario.html', nome)
            
        flash('USUÁRIO INVÁLIDO')
        return redirect(url_for('login_cliente'))
    
@app.route('/usuarioadmin', methods=['POST'])
def login_admin():  # Changed function name to avoid duplicate
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    
    with open('usuarioadmin.json') as usuariotemp:
        usuarios = json.load(usuariotemp)
        
        for usuario in usuarios:
            if usuario['nome'] == nome and usuario['senha'] == senha:
                return render_template('usuarioadmin.html', nome=nome)  # Fixed template variable passing
        
        flash('USUÁRIO INVÁLIDO')
        return redirect(url_for('usuarioadmin'))

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

@app.route('/Lirioshome.html')
def Lirioshome():
    return render_template('Lirioshome.html')

if __name__ == '__main__' :
    app.run(debug=True)