import sqlite3
from cliente import consultar_clientes
from produto import listar_produtos


def registrar_venda():
    conexao = sqlite3.connect('farmacia_med.db')
    cursor = conexao.cursor()

    try:
        consultar_clientes()
        cliente_id = int(input("Digite o ID do cliente: "))

        cursor.execute("SELECT idade FROM clientes WHERE id = ?", (cliente_id,))
        cliente = cursor.fetchone()

        if cliente is None:
            print("Cliente não encontrado!")
            return

        listar_produtos()
        produto_id = int(input("Digite o ID do produto: "))
        quantidade = int(input("Digite a quantidade desejada: "))

        cursor.execute("SELECT preco, estoque FROM produto WHERE id = ?", (produto_id,))
        produto = cursor.fetchone()

        if produto is None:
            print("Produto não encontrado!")
            return

        preco = produto[0]
        estoque = produto[1]

        if quantidade > estoque:
            print("Estoque insuficiente!")
            return

        total = preco * quantidade

        desconto = input("Aplicar desconto de 10%? (s/n): ")

        if desconto == "s":
            total = total * 0.90
            print("Desconto aplicado!")

        novo_estoque = estoque - quantidade

        cursor.execute(
            "UPDATE produto SET estoque = ? WHERE id = ?",
            (novo_estoque, produto_id)
        )

        cursor.execute(
            "INSERT INTO vendas (cliente_id, produto_id, quantidade, total) VALUES (?, ?, ?, ?)",
            (cliente_id, produto_id, quantidade, total)
        )

        conexao.commit()

        print("Venda registrada com sucesso! Total: R$", total)

    except ValueError:
        print("Erro: Digite os dados corretamente.")

    finally:
        conexao.close()


def consultar_historico_compras():
    conexao = sqlite3.connect('farmacia_med.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT v.id, c.nome, p.nome, v.quantidade, v.total
            FROM vendas v
            JOIN clientes c ON v.cliente_id = c.id
            JOIN produto p ON v.produto_id = p.id
        """)

        vendas = cursor.fetchall()

        print("\n--- HISTÓRICO DE COMPRAS ---")

        for venda in vendas:
            print(
                "Venda ID:", venda[0],
                "| Cliente:", venda[1],
                "| Produto:", venda[2],
                "| Quantidade:", venda[3],
                "| Total: R$", venda[4]
            )

    finally:
        conexao.close()


def gerar_relatorios():
    conexao = sqlite3.connect('farmacia_med.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT total FROM vendas")
        vendas = cursor.fetchall()

        faturamento = 0

        for venda in vendas:
            faturamento = faturamento + venda[0]

        print("Faturamento total: R$", faturamento)

    finally:
        conexao.close()