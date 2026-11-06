from cliente import cadastrar_cliente, consultar_clientes, atualizar_cliente
from produto import cadastrar_produto, listar_produtos
from venda import registrar_venda, consultar_historico_compras


def menu_atendente():
    while True:
        print("\n--- MENU ATENDENTE ---")
        print("1. Cadastrar Cliente")
        print("2. Consultar Clientes")
        print("3. Atualizar Cliente")
        print("4. Cadastrar Produto")
        print("5. Listar Produtos")
        print("6. Registrar Venda")
        print("7. Histórico de Compras")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")
        match opcao:
        
            case "1":
                cadastrar_cliente()
            case "2":
                consultar_clientes()
            case "3":
                atualizar_cliente()
            case "4":
                cadastrar_produto()
            case "5":
                listar_produtos()
            case "6":
                registrar_venda()
            case "7":
                consultar_historico_compras()
            case "8":
                print("Saindo do menu do atendente!")
                break
            case _:
                print("Opção inválida!")
