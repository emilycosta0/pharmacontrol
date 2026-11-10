import sqlite3
from datetime import datetime, timedelta


def cadastrar_produto():
    conexao = sqlite3.connect('farmacia_med.db')
    cursor = conexao.cursor()

    try:
        nome = input("Digite o nome do medicamento: ")
        preco = float(input("Digite o preço: "))
        estoque = int(input("Digite a quantidade em estoque: "))
        data_vencimento = (datetime.now() + timedelta(days=30)).strftime("%d-%m-%Y")
        print(f"Data de vencimento gerada automaticamente: {data_vencimento}")

        cursor.execute( "INSERT INTO produto (nome, preco, estoque, data_vencimento) VALUES (?, ?, ?, ?)", (nome, preco, estoque, data_vencimento))

        conexao.commit()
        print("Produto cadastrado com sucesso!")

        if estoque <= 5:
            print("ALERTA: Estoque baixo!")

    finally:
        conexao.close()


def listar_produtos():
    conexao = sqlite3.connect('farmacia_med.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM produto")
        produtos = cursor.fetchall()

        for produto in produtos:
            print( "ID:", produto[0],"| Nome:", produto[1],"| Preço: R$", produto[2],"| Estoque:", produto[3], "| Data_Vencimento:", produto[4])

    finally:
        conexao.close()

def verificar_vencidos():
    
    conexao = sqlite3.connect("farmacia_nova.db")
    cursor = conexao.cursor()

    data_atual = datetime.now().strftime("%d-%m-%Y")
    limite = (datetime.now() + timedelta(days=30)).strftime("%d-%m-%Y")
    try:
        cursor.execute(
            """
            SELECT id, nome, data_vencimento, estoque 
            FROM produto 
            WHERE data_vencimento <= ?
            ORDER BY data_vencimento ASC
        """,
            (limite,),
        )

        produtos = cursor.fetchall()

        print("\n--- ALERTA DE VENCIMENTO (Próximos 30 dias ou Vencidos) ---")
        if not produtos:
            print("Nenhum produto prestes a vencer ou vencido.")
        else:
            for p in produtos:
                status = "VENCIDO!" if p[2] < data_atual else "Próximo do vencimento"
                print(
                    f"[{status}] ID: {p[0]} | Nome: {p[1]} | Validade: {p[2]} | Estoque: {p[3]}"
                )

    finally:
        conexao.close()


def alterar_produto():
    conexao = sqlite3.connect('farmacia_med.db')
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
    conexao = sqlite3.connect('farmacia_med.db')
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
    conexao = sqlite3.connect('farmacia_med.db')
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
    conexao = sqlite3.connect('farmacia_med.db')
    cursor = conexao.cursor()

    try:
        id_produto = int(input("Digite o ID do produto que deseja excluir: "))

        cursor.execute("DELETE FROM produto WHERE id = ?",(id_produto,))

        conexao.commit()
        print("Produto excluído com sucesso!")

    finally:
        conexao.close()