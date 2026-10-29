positivos=0
negativos=0
zeros=0
for i in range (10):
    numero =int(input("digite um número:"))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1
print("quantidade de positivos:", positivos)
print("quantidade de negativos:", negativos)
print("quantidade de zeros:", zeros)