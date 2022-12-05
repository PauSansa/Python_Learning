palabra = input("Diga aqui su palabra: ")
def getReversed():

    temp = list(palabra)
    temp.reverse()
    reversedString = "".join(temp)
    return reversedString

    getReversed()

if getReversed() == palabra:
    print(f"La palabra {palabra} es un palíndromo")
else:
    print(f"La palabra {palabra} no es un palíndromo")