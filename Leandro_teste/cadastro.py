
import requests
import json
from validate_docbr import CPF
from pycpfcnpj import cnpj

cpf = CPF()

print('Olá, Seja Bem-vindo!')

usuario = str(input('Você é um Representante ou Cliente? ')).upper().strip()

# Dados do Representante
if usuario == "REPRESENTANTE":
    nome_rep = str(input('Digite seu nome: '))
    sobrenome_rep = str(input('Seu sobrenome: '))
    nascimento_rep = str(input('Digite sua Data de nascimento: (DIA/MÊS/ANO) '))

    # Validação de CPF
    while True:
        cpf_rep = str(input('Digite seu CPF: '))
        
        if cpf.validate(cpf_rep):  # Verifica se o CPF é válido
            print("CPF válido!")
            break  # Sai do loop se o CPF for válido
        else:
            print("CPF inválido! Por favor, tente novamente.")

    # Validação de CNPJ
    while True:
        cnpj_rep = str(input('Digite seu CNPJ: '))
        
        if cnpj.validate(cnpj_rep):  # Verifica se o CNPJ é válido
            print("CNPJ válido!")
            # Requisição para a API da Receita Federal para obter informações do CNPJ
            url = f"https://receitaws.com.br/v1/cnpj/{cnpj_rep}"
            querystring = {"token": 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', "plugin": 'RF'}
            response = requests.get(url, params=querystring)
            
            if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida
                resp = json.loads(response.text)
                print("Nome:", resp.get("nome", "Informação não disponível"))
                print("Fantasia:", resp.get("fantasia"))
                print("CEP:", resp.get("cep", "Informação não disponível"))
                print("Estado:", resp.get("uf"))
                print("Município:", resp.get("municipio"))
                print("Bairro:", resp.get("bairro", "Informação não disponível"))
                print("Rua:", resp.get("logradouro", "Informação não disponível"))
                print("Número:", resp.get("numero",))
                print("Telefone:", resp.get("telefone"))
                print("E-mail:", resp.get("email"))
                senha_rep = str(input("Crie uma senha: "))

            else:
                print("Erro ao consultar o CNPJ. Verifique o número do CNPJ ou a conexão.")
            break  # Sai do loop se o CNPJ for válido
        # Dados da Empresa
        else:
            print("Digite seu CNPJ manualmente ")
            cnpj_rep = str(input('Digite seu CNPJ: '))
            razao_rep = str(input('Digite a Razão Social da sua Empresa: '))
            tel_rep = str(input('Digite seu Telefone: '))
            
            cep_rep = str(input("Digite seu CEP: ")) 
            url = f"https://viacep.com.br/ws/{cep_rep}/json/"
            resposta = requests.get(url)
            # Buscando endereço Automaticamente
            if resposta.status_code == 200:
                endereco = json.loads(resposta.content)
                print("CEP: ", endereco["cep"])
                print("Bairro: ", endereco["bairro"])
                print("Rua: ", endereco["logradouro"])
                num_rua = str(input("Digite o número: "))
                complemento = str(input('Complemento: '))
            # Buscando endereço Manualmente
            if resposta.status_code != 200:
                    print('Não foi possível obter informações com CEP informado.')
                    cidade_rep = str(input("Digite a Cidade: "))
                    estado_rep = str(input("Digite seu Estado: "))
                    cep_rep = str(input("Digite seu CEP: ")) 
                    bairro_rep = str(input("Bairro: "))
                    rua_rep = str(input("Rua: "))
                    num_rua_rep = int(input("Digite o número: "))
                    complemento_rep = str(input('Complemento: '))          
        email_rep = str(input('Digite seu Email: '))
        senha_rep = str(input("Crie uma senha: "))
        break
        # Dados do Cliente
if usuario == "CLIENTE":
    nome_cliente = str(input('Digite seu nome: '))
    sobrenome_cliente = str(input('Seu sobrenome: '))
    nascimento_cliente = str(input('Digite sua Data de nascimento: (DIA/MÊS/ANO) '))

    # Validação de CPF
    while True:
        cpf_cliente = str(input('Digite seu CPF: '))
        
        if cpf.validate(cpf_cliente):  # Verifica se o CPF é válido
            print("CPF válido!")
            break  # Sai do loop se o CPF for válido
        else:
            print("CPF inválido! Por favor, tente novamente.")

    # Validação de CNPJ
    while True:
        cnpj_cliente = str(input('Digite seu CNPJ: '))
        
        if cnpj.validate(cnpj_cliente):  # Verifica se o CNPJ é válido
            print("CNPJ válido!")
            # Requisição para a API da Receita Federal para obter informações do CNPJ
            url = f"https://receitaws.com.br/v1/cnpj/{cnpj_cliente}"
            querystring = {"token": 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX', "plugin": 'RF'}
            response = requests.get(url, params=querystring)
            
            if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida
                resp = json.loads(response.text)
                print("Nome:", resp.get("nome", "Informação não disponível"))
                print("Fantasia:", resp.get("fantasia"))
                print("CEP:", resp.get("cep", "Informação não disponível"))
                print("Estado:", resp.get("uf"))
                print("Município:", resp.get("municipio"))
                print("Bairro:", resp.get("bairro", "Informação não disponível"))
                print("Rua:", resp.get("logradouro", "Informação não disponível"))
                print("Número:", resp.get("numero",))
                print("Telefone:", resp.get("telefone"))
                print("E-mail:", resp.get("email"))

            else:
                print("Erro ao consultar o CNPJ. Verifique o número do CNPJ ou a conexão.")
            break  # Sai do loop se o CNPJ for válido
        # Dados da Empresa
        else:
            print("Digite seu CNPJ manualmente ")
            cnpj_cliente = str(input('Digite seu CNPJ: '))
            razao_cliente = str(input('Digite a Razão Social da sua Empresa: '))
            tel_cliente = str(input('Digite seu Telefone: '))
            email_cliente = str(input('Digite seu Email: '))
            cep_cliente = str(input("Digite seu CEP: ")) 
            url = f"https://viacep.com.br/ws/{cep_cliente}/json/"
            resposta = requests.get(url)
            # Buscando endereço Automaticamente
            if resposta.status_code == 200:
                endereco = json.loads(resposta.content)
                print("CEP: ", endereco["cep"])
                print("Bairro: ", endereco["bairro"])
                print("Rua: ", endereco["logradouro"])
                num_rua = str(input("Digite o número: "))
                complemento = str(input('Complemento: '))
            # Buscando endereço Manualmente
            if resposta.status_code != 200:
                    print('Não foi possível obter informações com CEP informado.')
                    cidade_cliente = str(input("Digite a Cidade: "))
                    estado_clienterep = str(input("Digite seu Estado: "))
                    cep_cliente = str(input("Digite seu CEP: ")) 
                    bairro_cliente = str(input("Bairro: "))
                    rua_cliente = str(input("Rua: "))
                    num_rua_cliente = int(input("Digite o número: "))
                    complemento_cliente = str(input('Complemento: '))
                    break

print("Cadastro Feito com Sucesso.")