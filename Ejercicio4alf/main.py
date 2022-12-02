numeros = []
contador = 0
while contador < 5:
    numero = input("Di tu numero")
    numeros.append(numero)
    contador += 1
numeros.sort()
print(numeros)