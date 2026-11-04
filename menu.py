from banco import criar_tabelas
from atendente import menu_atendente
from gerente import menu_gerente


criar_tabelas()

print("\n--- PHARMACONTROL ---")
print("1. Entrar como Atendente")
print("2. Entrar como Gerente")
print("3. Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    menu_atendente()
elif opcao == "2":
    menu_gerente()
elif opcao == "3":
    print("Saindo do sistema. Até logo!")
else:
    print("Opção inválida!")