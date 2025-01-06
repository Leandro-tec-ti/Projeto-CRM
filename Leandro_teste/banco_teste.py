# Simulação de banco de dados com 5 usuários
usuarios = [
    {
        "usuario": "REPRESENTANTE",
        "nome": "João",
        "sobrenome": "Silva",
        "nascimento": "15/05/1985",
        "cpf": "12345678901",
        "cnpj": "12345678000190",
        "empresa": {
            "razao_social": "João Silva Representações",
            "telefone": "11987654321",
            "email": "joao@empresa.com",
            "endereco": {
                "cep": "01001000",
                "bairro": "Centro",
                "rua": "Rua A",
                "numero": "123",
                "complemento": "Sala 1",
                "senha": "1234"
            }
        }
    },
    {
        "usuario": "REPRESENTANTE",
        "nome": "Maria",
        "sobrenome": "Oliveira",
        "nascimento": "22/03/1990",
        "cpf": "98765432109",
        "cnpj": "98765432000191",
        "empresa": {
            "razao_social": "Oliveira Consultoria",
            "telefone": "21976543210",
            "email": "maria@oliveira.com",
            "endereco": {
                "cep": "22041001",
                "bairro": "Copacabana",
                "rua": "Rua B",
                "numero": "456",
                "complemento": "Apartamento 12",
                "senha": "1234"
            }
        }
    },
    {
        "usuario": "CLIENTE",
        "nome": "Carlos",
        "sobrenome": "Almeida",
        "nascimento": "10/07/1980",
        "cpf": "45612378909",
        "cnpj": "45612378000199",
        "empresa": {
            "razao_social": "Almeida Comércio",
            "telefone": "31987654321",
            "email": "carlos@almeida.com",
            "endereco": {
                "cep": "30130010",
                "bairro": "Savassi",
                "rua": "Rua C",
                "numero": "789",
                "complemento": "Loja 5",
                "senha": "1234"
            }
        }
    },
    {
        "usuario": "CLIENTE",
        "nome": "Ana",
        "sobrenome": "Santos",
        "nascimento": "05/12/1995",
        "cpf": "78912345600",
        "cnpj": "78912345000180",
        "empresa": {
            "razao_social": "Santos Distribuidora",
            "telefone": "11987651234",
            "email": "ana@santos.com",
            "endereco": {
                "cep": "04547001",
                "bairro": "Itaim Bibi",
                "rua": "Rua D",
                "numero": "321",
                "complemento": "Conjunto 20",
                "senha": "1234"
            }
        }
    },
    {
        "usuario": "REPRESENTANTE",
        "nome": "Pedro",
        "sobrenome": "Lima",
        "nascimento": "08/11/1975",
        "cpf": "32165498701",
        "cnpj": "32165498000199",
        "empresa": {
            "razao_social": "Lima e Associados",
            "telefone": "21987650987",
            "email": "pedro@lima.com",
            "endereco": {
                "cep": "50010010",
                "bairro": "Boa Vista",
                "rua": "Rua E",
                "numero": "654",
                "complemento": "Andar 3",
                "senha": "1234"
            }
        }
    }
]

# Exemplo de como acessar os dados
for usuario in usuarios:
    print(f"Nome completo: {usuario['nome']} {usuario['sobrenome']}")
    print(f"Tipo de usuário: {usuario['usuario']}")
    print(f"CPF: {usuario['cpf']}")
    print(f"CNPJ: {usuario['cnpj']}")
    print(f"Empresa: {usuario['empresa']['razao_social']}")
    print(f"Telefone: {usuario['empresa']['telefone']}")
    print(f"Endereço: {usuario['empresa']['endereco']['rua']}, {usuario['empresa']['endereco']['numero']}")
    print("-" * 50)
