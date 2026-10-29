n = int(input("Digite a quantidade de números: "))

for i in range(n):
    numero = int(input("Digite um número: "))

    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

diferenca = maior - menor

print("Maior valor:", maior)
print("Menor valor:", menor)
print("Diferença:", diferenca)

    
