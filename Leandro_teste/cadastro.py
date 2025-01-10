import requests
import json
from validate_docbr import CPF
from validate_docbr import CNPJ  # Corrigido para CNPJ

print('Olá, Seja Bem-vindo!')

usuario = str(input('Você é um  Cliente? [S/N] ')).upper().strip()

# Dados do Cliente
if usuario == "S":
    nome_cliente = str(input('Digite seu nome: '))
    sobrenome_cliente = str(input('Seu sobrenome: '))
    nascimento_cliente = str(input('Digite sua Data de nascimento: (DIA/MÊS/ANO) '))
    cpf_cliente = str(input('Digite seu CPF: '))
    cnpj_cliente = str(input('Digite seu CNPJ: '))
    email_cliente = str(input('Digite seu Email: '))
    senha_cliente = str(input("Digite seu senha: ")) 
    


print("Cadastro Feito com Sucesso.")
