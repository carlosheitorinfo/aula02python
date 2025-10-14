qtd = int(input("Qual a quantidade de produtos iniciais do seu estoque? "))
print(f"Estoque inicial: {qtd} produtos.")
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar produtos ao estoque")
    print("2. Registrar vendas")
    print("3. sair")    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        adicionar = int(input("Quantos produtos deseja adicionar? "))
        if adicionar > 0:
            qtd += adicionar
            print(f"{adicionar} produtos adicionados. Estoque atual: {qtd} produtos.")
        else:
            print("Quantidade inválida. Tente novamente.")
    
    elif opcao == "2":
        remover = int(input("Quantos produtos forma vendidos? "))
        if 0 < remover <= qtd:
            qtd -= remover
            print(f"{remover} produtos vendidos. Estoque atual: {qtd} produtos.")
        else:
            print("Quantidade inválida ou insuficiente no estoque. Tente novamente.")
    
    elif opcao == "3":
        print(f"Estoque atual: {qtd} produtos.")
        print("Saindo do sistema de controle de estoque.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")      