class Produto:
    def __init__(self, id_produto, nome, quantidade, preco):
        """Representa um produto no estoque."""
        self.id_produto = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.nome} (ID: {self.id_produto}) - {self.quantidade} em estoque - R${self.preco:.2f}"


class Cliente:
    def __init__(self, id_cliente, nome):
        """Representa um cliente."""
        self.id_cliente = id_cliente
        self.nome = nome

    def __str__(self):
        return f"Cliente ID: {self.id_cliente} - Nome: {self.nome}"


class Vendedor:
    def __init__(self, id_vendedor, nome):
        """Representa um vendedor."""
        self.id_vendedor = id_vendedor
        self.nome = nome

    def __str__(self):
        return f"Vendedor ID: {self.id_vendedor} - Nome: {self.nome}"


class Fornecedor:
    def __init__(self, id_fornecedor, nome):
        """Representa um fornecedor."""
        self.id_fornecedor = id_fornecedor
        self.nome = nome

    def __str__(self):
        return f"Fornecedor ID: {self.id_fornecedor} - Nome: {self.nome}"


class Venda:
    def __init__(self, id_venda, cliente, vendedor, produto, quantidade):
        """
        Representa uma venda realizada.
        Calcula o total com base no preço do produto e quantidade.
        """
        self.id_venda = id_venda
        self.cliente = cliente
        self.vendedor = vendedor
        self.produto = produto
        self.quantidade = quantidade
        self.total = produto.preco * quantidade

    def __str__(self):
        return (f"Venda ID: {self.id_venda} - Cliente: {self.cliente.nome} - "
                f"Vendedor: {self.vendedor.nome} - Produto: {self.produto.nome} - "
                f"Quantidade: {self.quantidade} - Total: R${self.total:.2f}")


class CRM:
    def __init__(self):
        """Sistema CRM para gerenciar produtos, clientes, vendedores e vendas."""
        self.produtos = {}
        self.clientes = {}
        self.vendedores = {}
        self.fornecedores = {}
        self.vendas = {}

    def adicionar_produto(self, produto):
        """Adiciona um produto ao estoque."""
        self.produtos[produto.id_produto] = produto

    def adicionar_cliente(self, cliente):
        """Adiciona um cliente ao sistema."""
        self.clientes[cliente.id_cliente] = cliente

    def adicionar_vendedor(self, vendedor):
        """Adiciona um vendedor ao sistema."""
        self.vendedores[vendedor.id_vendedor] = vendedor

    def adicionar_fornecedor(self, fornecedor):
        """Adiciona um fornecedor ao sistema."""
        self.fornecedores[fornecedor.id_fornecedor] = fornecedor

    def registrar_venda(self, venda):
        """
        Registra uma venda, verifica se o produto está em estoque
        e atualiza a quantidade disponível.
        """
        if venda.produto.id_produto in self.produtos:
            produto = self.produtos[venda.produto.id_produto]
            if produto.quantidade >= venda.quantidade:
                produto.quantidade -= venda.quantidade
                self.vendas[venda.id_venda] = venda
            else:
                print(f"Estoque insuficiente para o produto '{produto.nome}'!")
        else:
            print(f"Produto com ID {venda.produto.id_produto} não encontrado!")

    def listar_produtos(self):
        """Lista todos os produtos cadastrados no estoque."""
        for produto in self.produtos.values():
            print(produto)

    def listar_vendas(self):
        """Lista todas as vendas registradas."""
        for venda in self.vendas.values():
            print(venda)