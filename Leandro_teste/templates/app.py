from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'chave_flask_super_secreta'  # Necessário para usar session

@app.route('/') #<<<--- Definindo uma rota, um caminho a ser seguido pelo programa
def index(): #<<<--- Executando quando a rota for acessada
    return render_template('index.html') #<<<--- renderizando HTML, pegando um arquivo HTML e convertendo para o navegador exibir.


                                                    #GET= envia dados para URL para fins de consulta, não altera dados
@app.route('/cadastro', methods=['GET', 'POST'])    #POST= usadpo para enviar dados criando e alterando
def cadastro():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        print(f"o email é: {usuario}")
        print(f'a senha é: {senha}')

        return redirect(url_for('index'))


if __name__ == '__main__' :
    app.run(debug=True)