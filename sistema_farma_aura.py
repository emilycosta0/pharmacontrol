import sqlite3 

def criar_tabela():
    try:
        conexao = sqlite3.connect('sistema_farmacia.db')
        cursor = conexao.cursor()

        conexao.execute("PRAGMA foreign_keys = ON;")

        produto_id = int(input("Digite o ID do medicamento: "))
        quantidade = int(input("Digite a quantidade que será vendido: "))
        
        cursor.execute(''' CREATE TABLE IF NOT EXISTS cliente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade TEXT NOT NULL,
            CPF TEXT NOT NULL,
            )''')
        
        cursor.execute(''' CREATE TABLE IF NOT EXISTS produto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NO NULL,
            estoque INTEGER NOT NULL,
            preco REAL NOT NULL,
            )''')

         cursor.execute(''' CREATE TABLE IF NOT EXISTS vendas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id))''')

        conexao.commit()
    
      except sqlite3.IntegrityError as e:
        print("ERROR: Algo que não existe: ",e)
    except ValueError as e:
        print("ERROR: Tentativa de inventer numero para texto ou virse versa: ",e)
    except sqlite3.Error as e:
        print("ERROR: No SQL: ",e)
    finally:
        conexao.close()

def criar_cliente():
    try:
        conexao = sqlite3.connect('sistema_farmacia.db')
        cursor = conexao.cursor()

        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite o seu CPF: ")
        
        cursor.execute(''' INSERT INTO cliente(
            nome, idade, cpf) VALUES (?, ?, ?)''', (nome, idade, cpf))
        
        if idade < 20:
            print("Menor de idade não tem permissão para comprar medicamentos!")
            return

        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Cliente já cadastrado (CPF duplicado).")
    conexao.close()
    print("Cliente cadastrado com SUCESSO!!!")

def criar_produto()
    try:
        conexao = sqlite3.connect('sistema_farmacia.db')
        cursor = conexao.cursor()

          nome_produtos = ["Glifage": 19.00,"Neosoro": 15.00,"Losartana Potássica": 21.05,
          "Dipirona Sódica": 30.05,"Dorflex": 10.00,"Sinvastatina": 5.15, "Omeprazol": 45.90,
          "Puran T4": 50.55,"Tylenol": 35.00,"Ibuprofeno": 25.15,"Cataflam": 42.90,"Estomazil": 60.00]
        
        total_gasto = 0.0

        print("\n--- CATÁLOGO E PREÇOS ---")
        for med, preco in catalogo.items():
            print(f" {med} - R$ {preco:.2f}")

        print("\n --- Registrar Compras ---")

        while True:
            nome_desejado = input(" nome do medicamento (ou fim): ")
            if nome_desejado == "fim":
                break
            
       
        
        
            
        


        nome = input("Nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque = int(input("Informe sobre o estoque: "))

        cursor.execute('''INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", 
                          (nome, preco, estoque)''')

      

                          
        if estoque > 6:
            print("TUDO BEM!")
            return

        elif estoque <= 5:
            print("ALERTA!! ESTOQUE BAIXO. CANCELAMENTO DE VENDAS!!!!!!!") 
            return
        conexao.commit()
    except ValueError as e:
        print("ERROR: Tentativa de inventer numero para texto ou virse versa: ",e)
    conexao.close()
    print("Produto cadastrado com sucesso")

def criar_vendas():
    try:
        conexao = sqlite3.connect('sistema_farmacia.db')
        cursor = conexao.cursor()

        cliente_id = int(input("Digite o ID do cliente: "))
        produto_id = int(input("Digite o ID do produto: "))
        quantidade = int(input("Digite a quantidade vendida: "))


    

