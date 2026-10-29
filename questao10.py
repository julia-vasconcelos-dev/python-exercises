saldo=1000
opcao=0
while opcao !=4:
    print("\n=====caixa eletrônico=====")
    print("1- Consultar saldo")
    print("2- Despositar")
    print("3- Sacar")
    print("4- Sair")

    opcao= int(input("Digite uma opção:"))

    if opcao== 1:
       print("Saldo atual:R$", saldo) 

    elif opcao== 2:
       valor= float(input("Digite o valor do deposito:R$ "))
       saldo=saldo+ valor
       print("Depósito realizado com sucesso")
       print("Saldo atual: R$", saldo)
    elif opcao== 3:
       valor = float(input("Digite o valor do saque:R$ "))   
    
       if valor <= saldo:
        saldo =saldo-valor
        print("Saque realizado com sucesso!")
        print("Saldo atual: R$ ", saldo)
       else:
        print("saldo insuficiente!")

    elif opcao== 4:
        print("Programa encerrado!")
    
    else:
        print("Opção inválida!")