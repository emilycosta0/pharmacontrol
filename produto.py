import sqlite3


def cadastrar_produto():
    conexao = sqlite3.connect("farmacia_nova.db")
    cursor = conexao.cursor()

    try:
        nome = input("Digite o nome do medicamento: ")
        preco = float(input("Digite o preço: "))
        estoque = int(input("Digite a quantidade em estoque: "))

        cursor.execute( "INSERT INTO produto (nome, preco, estoque) VALUES (?, ?, ?)", (nome, preco, estoque))

        conexao.commit()
        print("Produto cadastrado com sucesso!")

        if estoque <= 5:
            print("ALERTA: Estoque baixo!")

    finally:
        conexao.close()


def listar_produtos():
    conexao = sqlite3.connect("farmacia_nova.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM produto")
        produtos = cursor.fetchall()

        for produto in produtos:
            print( "ID:", produto[0],"| Nome:", produto[1],"| Preço: R$", produto[2],"| Estoque:", produto[3])

    finally:
        conexao.close()


def alterar_produto():
    conexao = sqlite3.connect("farmacia_nova.db")
    cursor = conexao.cursor()

    try:
        id_produto = int(input("Digite o ID do produto: "))
        novo_nome = input("Digite o novo nome do produto: ")

        cursor.execute("UPDATE produto SET nome = ? WHERE id = ?",(novo_nome, id_produto))

        conexao.commit()
        print("Produto alterado com sucesso!")

    finally:
        conexao.close()


def atualizar_estoque():
    conexao = sqlite3.connect("farmacia_nova.db")
    cursor = conexao.cursor()

    try:
        id_produto = int(input("Digite o ID do produto: "))
        nova_quantidade = int(input("Digite a nova quantidade: "))

        cursor.execute("UPDATE produto SET estoque = ? WHERE id = ?",(nova_quantidade, id_produto))

        conexao.commit()
        print("Estoque atualizado!")

        if nova_quantidade <= 5:
            print("ALERTA: Estoque baixo!")

    finally:
        conexao.close()


def alterar_preco():
    conexao = sqlite3.connect("farmacia_nova.db")
    cursor = conexao.cursor()

    try:
        id_produto = int(input("Digite o ID do produto: "))
        novo_preco = float(input("Digite o novo preço: "))

        cursor.execute(
            "UPDATE produto SET preco = ? WHERE id = ?",
            (novo_preco, id_produto)
        )

        conexao.commit()
        print("Preço alterado com sucesso!")

    finally:
        conexao.close()


def deletar_produto():
    conexao = sqlite3.connect("farmacia_nova.db")
    cursor = conexao.cursor()

    try:
        id_produto = int(input("Digite o ID do produto que deseja excluir: "))

        cursor.execute("DELETE FROM produto WHERE id = ?",(id_produto,))

        conexao.commit()
        print("Produto excluído com sucesso!")

    finally:
        conexao.close()