import requests
import json

print('Olá Seja Bem-vindo ')

usuario = str(input('Você é um Representante ou Cliente? ')).upper().strip()

#Dados do Representante
if usuario == "REPRESENTANTE":
    nome_rep = str(input('Digite seu nome completo: '))
    cpf_rep = int(input('Dgite seu CPF: '))
    idade_rep = str(input('Digite sua idade: '))
    razao_rep = str(input('Digite a Razão Social da sua Empresa: '))
    cnpj_rep = str(input('Digite seu CNPJ: '))
    tel_rep = str(input('Digite seu Telefone: '))
    email_rep = str(input('Digite seu Email: '))
    cep_rep = str(input("Digite seu CEP: ")) 
    url = f"https://viacep.com.br/ws/{cep_rep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        endereco = json.loads(resposta.content)
        print("CEP: ", endereco["cep"])
        print("Bairro: ", endereco["bairro"])
        print("Rua: ", endereco["logradouro"])
        num_rua = str(input("Digite o número: "))
        complemento = str(input('Complemento: '))
    else:
        print('Não foi possível obter informações com CEP informado.')

# Dados do Cliente    
elif usuario == "CLIENTE":
    nome_cliente = str(input('Digite seu nome completo: '))
    cpf_cliente = int(input('Dgite seu CPF: '))
    idade_cliente = str(input('Digite sua idade: '))
    razao_cliente = str(input('Digite a Razão Social da sua Empresa: '))
    cnpj_cliente = str(input('Digite seu CNPJ: '))
    tel_cliente = str(input('Digite seu Telefone: '))
    email_cliente = str(input('Digite seu Email: '))
    cep_cliente = str(input("Digite seu CEP: ")) 
    url = f"https://viacep.com.br/ws/{cep_cliente}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        endereco = json.loads(resposta.content)
        print("CEP: ", endereco["cep"])
        print("Bairro: ", endereco["bairro"])
        print("Rua: ", endereco["logradouro"])
        num_rua = str(input("Digite o número: "))
        complemento = str(input('Complemento: '))
    else:
        print('Não foi possível obter informações com CEP informado.')