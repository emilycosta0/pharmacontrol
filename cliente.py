import sqlite3

def cadastrar_cliente():
    conexao = sqlite3.connect('farmacia_nova.db')
    cursor = conexao.cursor()
    try:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        cpf = input("CPF: ")
        
        cursor.execute("INSERT INTO clientes (nome, idade, CPF) VALUES (?, ?, ?)", (nome, idade, cpf))
        conexao.commit()
        print("Cliente cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado.")
    except ValueError:
        print("Erro nos dados digitados.")
    finally:
        conexao.close()

def consultar_clientes():
    conexao = sqlite3.connect('farmacia_nova.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    for c in cursor.fetchall():
        print(f"ID: {c[0]} | Nome: {c[1]} | Idade: {c[2]} | CPF: {c[3]}")
    conexao.close()


# --- CRUD DE CLIENTES ---
def atualizar_cliente():
    try:
        conexao = sqlite3.connect('farmacia_nova.db')
        cursor = conexao.cursor()

        id_cliente = input("ID do cliente que deseja atualizar: ")
        novo_nome = input("Novo nome: ")

        cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", (novo_nome, id_cliente))
        
        if cursor.rowcount == 0:
            raise ValueError("ID de cliente não encontrado.")
            
        conexao.commit()
        print("Cliente atualizado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")
    finally:
        conexao.close()

def deletar_cliente(): # DELETE
    conexao = sqlite3.connect('farmacia_nova.db')
    cursor = conexao.cursor()
    id_cliente = input("ID do cliente que deseja excluir: ")
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    print("Cliente excluído!")
    conexao.close()