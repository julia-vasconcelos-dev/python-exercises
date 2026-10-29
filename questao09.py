n=int(input("Digite a quantidade de número:"))
for i in range(n):
    numero= int(input("Digite o número:"))
    if i == 0:
        maior=numero
        menor=numero
    else:
        if numero > maior:
            maior= numero
        if numero < menor:
            menor= numero
    diferenca= maior-menor
    print("maior valor:", maior)
    print("menor valor:", menor)
    print("diferança:", diferenca)
    