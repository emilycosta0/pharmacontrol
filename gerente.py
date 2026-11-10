from cliente import cadastrar_cliente, consultar_clientes, atualizar_cliente, deletar_cliente
from produto import cadastrar_produto, listar_produtos, verificar_vencidos, alterar_produto, deletar_produto
from venda import registrar_venda, consultar_historico_compras, gerar_relatorios
from venda import consultar_historico_compras, gerar_relatorios, registrar_venda




def menu_gerente():
    while True:
        print("\n--- MENU GERENTE ---")
        print("1. Cadastrar Cliente")
        print("2. Consultar Clientes")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Cadastrar Produto")
        print("6. Listar Produtos")
        print("7. Atualizar Produto")
        print("8. Deletar Produto")
        print("9. Registrar Venda")
        print("10. Histórico de Compras")
        print("11. Relatório Financeiro")
        print("12. Verificar vencimento")
        print("13. Sair")

        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                cadastrar_cliente()
            case "2":
                consultar_clientes()
            case "3":
                atualizar_cliente()
            case "4":
                deletar_cliente()
            case "5":
                cadastrar_produto()
            case "6":
                listar_produtos()
            case "7":
                alterar_produto()
            case "8":
                deletar_produto()
            case "9":
                registrar_venda()
            case "10":
                consultar_historico_compras()
            case "11":
                gerar_relatorios()
            case "12":
                verificar_vencidos()
            case "13":
                print("Saindo do menu do gerente!")
                break
            case _:
                print("Opção inválida!")
