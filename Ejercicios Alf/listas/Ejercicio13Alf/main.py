print("introduce numeros separados por comas:")
numeros = input()
numeros = numeros.split(",")


for i in range(len(numeros)):
    numeros[i] = int(numeros[i])
def media():
    suma = 0
    for numero in numeros:
        suma += numero
    media = suma / len(numeros)
    return media
def desviacionTipica():
    

print(media())