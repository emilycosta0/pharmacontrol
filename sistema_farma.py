import sqlite3

def conectar():
    return sqlite3.connect('sistema_farmacia.db')

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()
    conexao.execute("PRAGMA foreign_keys = ON;")

    cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        CPF TEXT UNIQUE NOT NULL
    )''')
    
    cursor.execute(''' CREATE TABLE IF NOT EXISTS produto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    )''')

    cursor.execute(''' CREATE TABLE IF NOT EXISTS vendas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        produto_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        total REAL NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id),
        FOREIGN KEY (produto_id) REFERENCES produto(id)
    )''')
    conexao.commit()
    conexao.close()

# --- CLIENTES ---
def cadastrar_cliente():
    conexao = conectar()
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
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    for c in cursor.fetchall():
        print(f"ID: {c[0]} | Nome: {c[1]} | Idade: {c[2]} | CPF: {c[3]}")
    conexao.close()


# --- CRUD DE CLIENTES ---
def atualizar_cliente(): # UPDATE
    conexao = conectar()
    cursor = conexao.cursor()
    id_cliente = input("ID do cliente que deseja atualizar: ")
    novo_nome = input("Novo nome: ")
    cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", (novo_nome, id_cliente))
    conexao.commit()
    print("Cliente atualizado!")
    conexao.close()

def deletar_cliente(): # DELETE
    conexao = conectar()
    cursor = conexao.cursor()
    id_cliente = input("ID do cliente que deseja excluir: ")
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    print("Cliente excluído!")
    conexao.close()

# --- PRODUTOS & ESTOQUE ---
def cadastrar_produto():
    conexao = conectar()
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
    conexao = conectar()
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
    conexao = conectar()
    cursor = conexao.cursor()
    id_prod = int(input("ID do produto: "))
    novo_preco = float(input("Novo preço (R$): "))
    cursor.execute("UPDATE produto SET preco = ? WHERE id = ?", (novo_preco, id_prod))
    conexao.commit()
    conexao.close()
    print("Preço alterado com sucesso!")

def excluir_item_estoque():
    conexao = conectar()
    cursor = conexao.cursor()
    id_prod = int(input("ID do produto para excluir: "))
    cursor.execute("DELETE FROM produto WHERE id = ?", (id_prod,))
    conexao.commit()
    conexao.close()
    print("Item excluído do estoque!")

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto")
    for p in cursor.fetchall():
        print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R$ {p[2]:.2f} | Estoque: {p[3]}")
    conexao.close()

def alterar_produto():
    try:
        conexao = conectar()
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
        conexao = conectar()
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

# --- PDV / VENDAS ---
def registrar_venda():
    conexao = conectar()
    cursor = conexao.cursor()
    
    consultar_clientes()
    cliente_id = int(input("Digite o ID do cliente: "))
    
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
    produto_id = int(input("Digite o ID do produto: "))
    quantidade = int(input("Quantidade desejada: "))
    
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
    
    # Aplicar descontos/promoções opcionais
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

# --- RELATÓRIOS ---
def consultar_historico_compras():
    conexao = conectar()
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
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT SUM(total) FROM vendas")
    faturamento = cursor.fetchone()[0] or 0.0
    print(f"\n Faturamento Total do Sistema: R$ {faturamento:.2f}")
    conexao.close()

if __name__ == "__main__":
    criar_tabelas()
    print("Sistema pronto para uso!")

while True:
    print("\n--- MENU FARMÁCIA ---")
    print("1. Cadastrar Cliente")
    print("2. Consultar Clientes")
    print("3. Atualizar Cliente")
    print("4. Deletar Cliente")
    print("5. Cadastrar Produto")
    print("6. Listar Produtos")
    print("7. Atualizar Produto")
    print("8. Deletar Produto")
    print("9. Registrar Venda (PDV)")
    print("10. Histórico de Compras")
    print("11. Relatório Financeiro")
    print("12. Sair")
        
    opcao = input("Escolha uma opção: ")
        
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        consultar_clientes()
    elif opcao == "3":
        atualizar_cliente()
    elif opcao == "4":
        deletar_cliente()
    elif opcao == "5":
        cadastrar_produto()
    elif opcao == "6":
        listar_produtos()
    elif opcao == "7":
        alterar_produto()
    elif opcao == "8":
        deletar_produto()
    elif opcao == "9":
        registrar_venda()
    elif opcao == "10":
        consultar_historico_compras()
    elif opcao == "11":
        gerar_relatorios()
    elif opcao == "12":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida! Escolha de 1 a 12.")