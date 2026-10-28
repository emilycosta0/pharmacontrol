import sqlite3
from cliente import consultar_clientes
from produto import listar_produtos

def registrar_venda():
    conexao = sqlite3.connect('farmacia_nova.db')
    cursor = conexao.cursor()
    
    consultar_clientes()
    try:
        cliente_id = int(input("Digite o ID do cliente: "))
    except ValueError:
        print("ID inválido!")
        conexao.close()
        return
    
    cursor.execute("SELECT idade FROM clientes WHERE id = ?", (cliente_id,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente não encontrado!")
        conexao.close()
        return
    if cliente[0] < 20:
        print("Menor de 20 anos não tem permissão para comprar medicamentos!")
        conexao.close()
        return

    listar_produtos()
    try:
        produto_id = int(input("Digite o ID do produto: "))
        quantidade = int(input("Quantidade desejada: "))
    except ValueError:
        print("Dados inválidos!")
        conexao.close()
        return
    
    cursor.execute("SELECT preco, estoque FROM produto WHERE id = ?", (produto_id,))
    prod = cursor.fetchone()
    if not prod:
        print("Produto não encontrado!")
        conexao.close()
        return
    
    preco, estoque = prod[0], prod[1]
    if quantidade > estoque:
        print(f"Estoque insuficiente! Restam apenas {estoque} unidades.")
        conexao.close()
        return

    subtotal = preco * quantidade
    tem_desconto = input("Aplicar desconto de 10%? (s/n): ").lower()
    if tem_desconto == 's':
        subtotal *= 0.90
        print("Desconto aplicado!")

    novo_estoque = estoque - quantidade
    cursor.execute("UPDATE produto SET estoque = ? WHERE id = ?", (novo_estoque, produto_id))
    cursor.execute("INSERT INTO vendas (cliente_id, produto_id, quantidade, total) VALUES (?, ?, ?, ?)", 
                   (cliente_id, produto_id, quantidade, subtotal))
    conexao.commit()
    conexao.close()
    print(f"Venda registrada com sucesso! Total: R$ {subtotal:.2f}")

def consultar_historico_compras():
    conexao = sqlite3.connect('farmacia_nova.db')
    cursor = conexao.cursor()
    cursor.execute(''' SELECT v.id, c.nome, p.nome, v.quantidade, v.total 
                       FROM vendas v 
                       JOIN clientes c ON v.cliente_id = c.id 
                       JOIN produto p ON v.produto_id = p.id ''')
    print("\n--- HISTÓRICO DE COMPRAS ---")
    for h in cursor.fetchall():
        print(f"Venda ID: {h[0]} | Cliente: {h[1]} | Produto: {h[2]} | Qtd: {h[3]} | Total: R$ {h[4]:.2f}")
    conexao.close()

def gerar_relatorios():
    conexao = sqlite3.connect('farmacia_nova.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT SUM(total) FROM vendas")
    resultado = cursor.fetchone()[0]
    faturamento = resultado if resultado else 0.0
    print(f"\nFaturamento Total do Sistema: R$ {faturamento:.2f}")
    conexao.close()
