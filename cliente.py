import sqlite3


def cadastrar_cliente():
    conexao = sqlite3.connect('farma_aura.db')
    cursor = conexao.cursor()

    try:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        cpf = input("Digite o CPF: ")

        cursor.execute("INSERT INTO clientes (nome, idade, CPF) VALUES (?, ?, ?)",(nome, idade, cpf))

        conexao.commit()
        print("Cliente cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado.")

    except ValueError:
        print("Erro: Digite os dados corretamente.")

    finally:
        conexao.close()


def consultar_clientes():
    conexao = sqlite3.connect('farma_aura.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()

        for cliente in clientes:
            print("ID:", cliente[0],"| Nome:", cliente[1],"| Idade:", cliente[2],"| CPF:", cliente[3])

    finally:
        conexao.close()


def atualizar_cliente():
    conexao = sqlite3.connect('farma_aura.db')
    cursor = conexao.cursor()

    try:
        id_cliente = input("Digite o ID do cliente: ")
        novo_nome = input("Digite o novo nome: ")

        cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?",(novo_nome, id_cliente))

        conexao.commit()
        print("Cliente atualizado com sucesso!")

    finally:
        conexao.close()


def deletar_cliente():
    conexao = sqlite3.connect('farma_aura.db')
    cursor = conexao.cursor()

    try:
        id_cliente = input("Digite o ID do cliente que deseja excluir: ")

        cursor.execute("DELETE FROM clientes WHERE id = ?",(id_cliente,))

        conexao.commit()
        print("Cliente excluído com sucesso!")

    finally:
        conexao.close()