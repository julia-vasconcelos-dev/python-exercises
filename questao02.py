n = int(input("Digite um número inteiro positivo: "))
quantidade = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
        quantidade += 1

print("Quantidade de números pares:", quantidade)
