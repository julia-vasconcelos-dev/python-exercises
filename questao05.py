quantidade = int(input("Digite a quantidade de números: "))

while quantidade <= 0:
    print("Digite uma quantidade maior que zero.")
    quantidade = int(input("Digite a quantidade de números: "))

soma = 0

for i in range(quantidade):
    numero = float(input("Digite um número: "))
    soma = soma + numero

    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

media = soma / quantidade

print("Soma:", soma)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
