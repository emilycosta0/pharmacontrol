import sqlite3

class Produto:
    def cadastrar_produto():
        conexao = sqlite3.connect('sistema_farmacia.db')
        cursor = conexao.cursor()
        try:
            nome = input("Nome do medicamento: ")
            preco = float(input("Preço (R$): "))
            estoque = int(input("Quantidade em estoque: "))
        
            cursor.execute("INSERT INTO produto (nome, preco, estoque) VALUES (?, ?, ?)", (nome, preco, estoque))
            conexao.commit()
            print("Produto cadastrado!")
            if estoque <= 5:
                print("ALERTA: Estoque baixo (<= 5 unidades)!")
        finally:
            conexao.close()

    def atualizar_estoque():
        conexao = sqlite3.connect('sistema_farmacia.db')
        cursor = conexao.cursor()
        id_prod = int(input("ID do produto: "))
        nova_qtd = int(input("Nova quantidade em estoque: "))
        cursor.execute("UPDATE produto SET estoque = ? WHERE id = ?", (nova_qtd, id_prod))
        conexao.commit()
        conexao.close()
        print("Estoque atualizado!")
        if nova_qtd <= 5:
            print("ALERTA: Estoque baixo!")

    def alterar_preco():
        conexao = sqlite3.connect('sistema_farmacia.db')
        cursor = conexao.cursor()
        id_prod = int(input("ID do produto: "))
        novo_preco = float(input("Novo preço (R$): "))
        cursor.execute("UPDATE produto SET preco = ? WHERE id = ?", (novo_preco, id_prod))
        conexao.commit()
        conexao.close()
        print("Preço alterado com sucesso!")

    def excluir_item_estoque():
        conexao = sqlite3.connect('sistema_farmacia.db')
        cursor = conexao.cursor()
        id_prod = int(input("ID do produto para excluir: "))
        cursor.execute("DELETE FROM produto WHERE id = ?", (id_prod,))
        conexao.commit()
        conexao.close()
        print("Item excluído do estoque!")

    def listar_produtos():
        conexao = sqlite3.connect('sistema_farmacia.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produto")
        for p in cursor.fetchall():
            print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]:.2f} | Estoque: {p[3]}")
        conexao.close()

    def alterar_produto():
        try:
            conexao = sqlite3.connect('sistema_farmacia.db')
            cursor = conexao.cursor()

            id_produto = int(input("Digite o ID do medicamento que queira alterar: "))
            novo_produto = input("Digite o novo nome do produto: ")

            cursor.execute("UPDATE produto SET nome = ? WHERE id = ?", (novo_produto, id_produto))    

            conexao.commit()
            print("Produto alterado com SUCESSO!")

        except ValueError as e:
            print("ERROR: Tentativa de inverter número para texto ou vice-versa: ", e)
        finally:
            conexao.close()

    def deletar_produto():
        try:
            conexao = sqlite3.connect('sistema_farmacia.db')
            cursor = conexao.cursor()

            id_produto = int(input("Digite o ID do produto que deseja deletar: "))
        # Corrigido para 'WHERE id = ?' e adicionada a vírgula na tupla (id_produto,)
            cursor.execute("DELETE FROM produto WHERE id = ?", (id_produto,))
        
            conexao.commit()
            print("Produto deletado com SUCESSO!")

        except ValueError as e:
            print("ERROR: Tentativa de inverter número para texto ou vice-versa: ", e)
        finally:
            conexao.close()