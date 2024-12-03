# Criando produtos
produto1 = Produto(id_produto=1, nome="Notebook Dell", quantidade=10, preco=4500.00)
produto2 = Produto(id_produto=2, nome="Mouse Logitech", quantidade=50, preco=150.00)
produto3 = Produto(id_produto=3, nome="Teclado Mecânico", quantidade=30, preco=300.00)

# Criando clientes
cliente1 = Cliente(id_cliente=1, nome="João Silva")
cliente2 = Cliente(id_cliente=2, nome="Maria Oliveira")

# Criando vendedores
vendedor1 = Vendedor(id_vendedor=1, nome="Lucas Pereira")
vendedor2 = Vendedor(id_vendedor=2, nome="Ana Costa")

# Criando fornecedores
fornecedor1 = Fornecedor(id_fornecedor=1, nome="Tech Distribuidora")
fornecedor2 = Fornecedor(id_fornecedor=2, nome="Office Supplies")

# Criando vendas
venda1 = Venda(
    id_venda=1,
    cliente=cliente1,
    vendedor=vendedor1,
    produto=produto1,
    quantidade=2
)

venda2 = Venda(
    id_venda=2,
    cliente=cliente2,
    vendedor=vendedor2,
    produto=produto2,
    quantidade=5
)

venda3 = Venda(
    id_venda=3,
    cliente=cliente1,
    vendedor=vendedor2,
    produto=produto3,
    quantidade=1
)

# Criando instância do CRM e adicionando objetos
crm = CRM()

# Adicionando produtos
crm.adicionar_produto(produto1)
crm.adicionar_produto(produto2)
crm.adicionar_produto(produto3)

# Adicionando clientes
crm.adicionar_cliente(cliente1)
crm.adicionar_cliente(cliente2)

# Adicionando vendedores
crm.adicionar_vendedor(vendedor1)
crm.adicionar_vendedor(vendedor2)

# Adicionando fornecedores
crm.adicionar_fornecedor(fornecedor1)
crm.adicionar_fornecedor(fornecedor2)

# Registrando vendas
crm.registrar_venda(venda1)
crm.registrar_venda(venda2)
crm.registrar_venda(venda3)

# Listando produtos e vendas
print("Produtos no estoque:")
crm.listar_produtos()

print("\nVendas registradas:")
crm.listar_vendas()