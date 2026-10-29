quantidade =int(input("Digite a quantidade de números informados:"))
soma=0
for i in range (quantidade):
    numero=float(input("Digite um número:"))
    soma=soma+numero
    if i ==0:
        maior=numero
        menor=numero
    else:
        if numero > maior:
            maior=numero
        if numero < menor:
            menor=numero            

media= soma/quantidade
print("soma:", soma)
print("media:", media)
print("maior valor:", maior)
print("menor valor:",menor)