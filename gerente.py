import sqlite3
from cliente import cadastrar_cliente, consultar_clientes, atualizar_cliente, deletar_cliente
from produto import cadastrar_produto, listar_produtos, verificar_vencidos, alterar_produto, deletar_produto
from venda import registrar_venda, consultar_historico_compras, gerar_relatorios
from venda import consultar_historico_compras, gerar_relatorios, registrar_venda

def cadastrar_gerente():
    conexao = sqlite3.connect('farma_aura.db')
    cursor = conexao.cursor()
    
    nome_gerente = input("Digite seu nome GERENTE: ")
    cursor.execute("INSERT INTO gerente(nome_gerente) VALUES (?)",(nome_gerente,))
    conexao.commit()
    print("Gerente cadastrado com sucesso!")

def menu_gerente():
    while True:
        print("\n--- MENU GERENTE ---")
        print("1. Nome do Gerente")
        print("2. Cadastrar Cliente")
        print("3. Consultar Clientes")
        print("4. Atualizar Cliente")
        print("5. Deletar Cliente")
        print("6. Cadastrar Produto")
        print("7. Listar Produtos")
        print("8. Atualizar Produto")
        print("9. Deletar Produto")
        print("10. Registrar Venda")
        print("11. Histórico de Compras")
        print("12. Relatório Financeiro")
        print("13. Verificar vencimento")
        print("14. Sair")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                cadastrar_gerente()
            case "2":
                cadastrar_cliente()
            case "3":
                consultar_clientes()
            case "4":
                atualizar_cliente()
            case "5":
                deletar_cliente()
            case "6":
                cadastrar_produto()
            case "7":
                listar_produtos()
            case "8":
                alterar_produto()
            case "9":
                deletar_produto()
            case "10":
                registrar_venda()
            case "11":
                consultar_historico_compras()
            case "12":
                gerar_relatorios()
            case "13":
                verificar_vencidos()
            case "14":
                print("Saindo do menu do gerente!")
                break
            case _:
                print("Opção inválida!")
