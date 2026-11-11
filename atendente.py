import sqlite3
from cliente import cadastrar_cliente, consultar_clientes, atualizar_cliente
from produto import cadastrar_produto, listar_produtos
from venda import registrar_venda, consultar_historico_compras

def cadastrar_atendente():
    conexao = sqlite3.connect('farma_aura.db')
    cursor = conexao.cursor()
    
    nome_atendente = input("Digite seu nome ATENDENTE: ")
    cursor.execute("INSERT INTO atendente(nome_atendente) VALUES (?)",(nome_atendente,))
    conexao.commit()
    print("Atendente cadastrado com sucesso!")

def menu_atendente():
    while True:
        print("\n--- MENU ATENDENTE ---")
        print("1. Nome do Atendente")
        print("2. Cadastrar Cliente")
        print("3. Consultar Clientes")
        print("4. Atualizar Cliente")
        print("5. Cadastrar Produto")
        print("6. Listar Produtos")
        print("7. Registrar Venda")
        print("8. Histórico de Compras")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                cadastrar_atendente()
            case "2":
                cadastrar_cliente()
            case "3":
                consultar_clientes()
            case "4":
                atualizar_cliente()
            case "5":
                cadastrar_produto()
            case "6":
                listar_produtos()
            case "7":
                registrar_venda()
            case "8":
                consultar_historico_compras()
            case "9":
                print("Saindo do menu do atendente!")
                break
            case _:
                print("Opção inválida!")
