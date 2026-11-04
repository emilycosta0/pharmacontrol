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

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            consultar_clientes()
        elif opcao == "3":
            atualizar_cliente()
        elif opcao == "4":
            cadastrar_produto()
        elif opcao == "5":
            listar_produtos()
        elif opcao == "6":
            registrar_venda()
        elif opcao == "7":
            consultar_historico_compras()
        elif opcao == "8":
            print("Saindo do menu do atendente!")
            break
        else:
            print("Opção inválida!")
