from banco import criar_tabelas
from cliente import cadastrar_cliente, consultar_clientes, atualizar_cliente, deletar_cliente
from produto import cadastrar_produto, listar_produtos, alterar_produto, deletar_produto
from venda import registrar_venda, consultar_historico_compras, gerar_relatorios

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