saldo = 1000
opcao = 0

while opcao != 4:
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        print("Saldo atual: R$", saldo)

    elif opcao == 2:
        valor = float(input("Digite o valor do depósito: R$ "))

        if valor > 0:
            saldo = saldo + valor
            print("Depósito realizado com sucesso!")
            print("Saldo atual: R$", saldo)
        else:
            print("O valor do depósito deve ser maior que zero.")

    elif opcao == 3:
        valor = float(input("Digite o valor do saque: R$ "))

        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        elif valor <= saldo:
            saldo = saldo - valor
            print("Saque realizado com sucesso!")
            print("Saldo atual: R$", saldo)
        else:
            print("Saldo insuficiente!")

    elif opcao == 4:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")
