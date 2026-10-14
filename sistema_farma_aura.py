import sqlite3 

def criar_tabela():
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()

        conexao.execute("PRAGMA foreign_keys = ON;")
        

        cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade TEXT NOT NULL,
            CPF TEXT NOT NULL
            )''')
        
        cursor.execute(''' CREATE TABLE IF NOT EXISTS produto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco INTEGER NOT NULL,
            estoque INTEGER NOT NULL
            )''')

        cursor.execute(''' CREATE TABLE IF NOT EXISTS vendas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
            )''')

        conexao.commit()
    
    except sqlite3.IntegrityError as e:
        print("ERROR: Algo que não existe: ",e)
    except ValueError as e:
        print("ERROR: Tentativa de inventer numero para texto ou virse versa: ",e)
    except sqlite3.Error as e:
        print("ERROR: No SQL: ",e)
    finally:
        conexao.close()

def cadastrar_cliente():
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()

        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite o seu CPF: ")
        
        cursor.execute(''' INSERT INTO clientes(nome, idade, CPF) VALUES (?, ?, ?)''', (nome, idade, cpf))
        
        if idade < 20:
            print("Menor de idade não tem permissão para comprar medicamentos!")
            return

        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Cliente já cadastrado (CPF duplicado).")
    conexao.close()
    print("Cliente cadastrado com SUCESSO!!!")

def listar_cliente():
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        print("\n--- LISTA DE CLIENTES ---")
        for c in clientes:
            print(f"ID: {c[0]} | Nome: {c[1]} | Idade: {c[2]} | CPF: {c[3]}")
    
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Cliente já está na lista.") 
        conexao.close()

def atualizar_cliente():
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()

        id_cliente = int(input("Digite o ID do cliente para ser alterado: "))
        novo_nome = input("Digite o novo nome do cliente: ")
        
        cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", (novo_nome, id_cliente))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Cliente já está na lista.") 
        print("Cliente atualizado!")
        conexao.close()
def deletar_cliente():
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()

        id_cliente = int(input("Digite o ID do cliente a ser deletado: "))
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Cliente já está na lista.") 
        print("Cliente excluído!")
        conexao.close()

def cadastrar_produto():
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()
    
        nome = input("Digite o nome do medicamento: ")
        preco = int(input("Digite o preço de cada medicamento: "))
        estoque = int(input("Informe a quantidade em estoque: "))

        cursor.execute(''' INSERT INTO produto (nome, preco, estoque) VALUES (?,?,?) ''', (nome, preco, estoque))

        if estoque >= 100:
            print("ESTOQUE CHEIO!")
        if estoque <= 5:
            print("ALERTA! ESTOQUE BAIXO")
        conexao.commit()

    except ValueError as e:
        print("ERROR: Tentativa de inventer numero para texto ou virse versa: ",e)
    conexao.close()
    print("Produto cadastrado com sucesso")

def listar_produto():
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM produto")
        produtos = cursor.fetchall()
        print("\n--- LISTA DE PRODUTOS ---")
        for p in produtos:
            print(f"ID: {p[0]} | Nome: {p[1]} | Preço: {p[2]}")

        conexao.commit()
    except ValueError as e:
        print("ERROR: Tentativa de inventer numero para texto ou virse versa: ",e)
        print("Produto listado com SUCESSO!")
        conexao.close()

def alterar_produto():
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()

        id_produto = int(input("Digite o ID  do medicamento que queira alterar: "))
        novo_produto = input("Digite o novo nome do produto: ")

        cursor.execute("UPDATE produto SET produto = ? WHERE id = ?",(novo_produto, id_produto))    

        conexao.commit()

    except ValueError as e:
        print("ERROR: Tentativa de inventer numero para texto ou virse versa: ",e)
        print("Produto alterado com SUCESSO!")
        conexao.close()

def deletar_produto():
    try:
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()

        id_produto = int(input("Digite o ID do produto que deseja deletar: "))
        cursor.execute("DELETE FROM produto WHERE = ?",(id_produto))
        
        conexao.commit()

    except ValueError as e:
        print("ERROR: Tentativa de inventer numero para texto ou virse versa: ",e)
        print("Produto deletado com SUCESSO!")
        conexao.close()






if __name__ == "__main__":
    # Crie as tabelas primeiro para o banco existir
    criar_tabela()
    cadastrar_cliente()
    listar_cliente()
    atualizar_cliente()
    deletar_cliente()
    cadastrar_produto()
    listar_produto()
    alterar_produto()
    deletar_produto()