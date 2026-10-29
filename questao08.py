aprovado = 0
recuperacao = 0
reprovado = 0
total = 0

nota = float(input("Digite sua nota: "))

while nota != -1:
    total += 1

    if nota >= 7:
        aprovado += 1
    elif nota >= 5:
        recuperacao += 1
    else:
        reprovado += 1

    nota = float(input("Digite sua nota: "))

print("Quantidade de aprovados:", aprovado)
print("Quantidade de recuperação:", recuperacao)
print("Quantidade de reprovados:", reprovado)
print("Quantidade total de estudantes:", total)
