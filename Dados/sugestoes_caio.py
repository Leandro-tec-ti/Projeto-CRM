 while resposta.status_code != 200:
            print('Não foi possível obter informações com CEP informado.')
            cep_cliente = str(input("Digite seu CEP: ")) 
            url = f"https://viacep.com.br/ws/{cep_cliente}/json/"
            resposta = requests.get(url)
            endereco = json.loads(resposta.content)
            print("CEP: ", endereco["cep"])
            print("Bairro: ", endereco["bairro"])
            print("Rua: ", endereco["logradouro"])
            num_rua = str(input("Digite o número: "))
            complemento = str(input('Complemento: '))