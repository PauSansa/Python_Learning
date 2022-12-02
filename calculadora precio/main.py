print("1 para Calculadora, 2 para Tabla de Valores")
metodo = input()
if metodo == 1:
    print("Cuantas Unidades?")
    valor = int(input())
    if valor < 5:
        print("El valor", valor, "es demasiado bajo")
    elif 5 <= valor <= 19:
        tarifa = valor * 7.23
        print(valor, "unidades saldrian por", round(tarifa,2), "€")
    elif 20 <= valor <= 49:
        tarifa = valor * 6.80
        print(valor, "unidades saldrian por", round(tarifa,2), "€")
    elif 59 <= valor:
        tarifa = valor * 6.38
        print(valor, "unidades saldrian por", round(tarifa,2), "€") 
else:
    valor = 6
    while valor < 100:
        if valor < 5:
            print("El valor", valor, "es demasiado bajo")
        elif 5 <= valor <= 19:
            tarifa = valor * 7.23
            print(valor, "unidades saldrian por", round(tarifa,2), "€")
        elif 20 <= valor <= 49:
            tarifa = valor * 6.80
            print(valor, "unidades saldrian por", round(tarifa,2), "€")
        elif 59 <= valor:
            tarifa = valor * 6.38
            print(valor, "unidades saldrian por", round(tarifa,2), "€") 
        valor += 1

