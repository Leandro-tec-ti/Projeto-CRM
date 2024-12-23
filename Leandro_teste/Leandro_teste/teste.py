from flask import Flask, make_response, jsonify
from bd import usuarios #<<<--- puxando a simulaçao do banco de dados na pasta (db.py)

app = Flask(__name__)  # <<--- Criando uma variação para Flask " APP"

@app.route("/usuarios", methods=["GET", 'POST']) #<<-- Aqui estou dando o caminho do que eu quero de informação do banco
def get_usuario(): #<<<definindo uma função
    return make_response (jsonify(usuarios))#<<<--- aqui esta retornando o que solicitei

app.run() # Aqui é para dá start e deixar servidor no ar  