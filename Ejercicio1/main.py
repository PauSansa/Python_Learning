class Vehiculo:
    color = "Negro"
    ruedas = 4
    puertas = 4


class Coche(Vehiculo):
    velocidad = 130
    Cilindrada = "115 cv"


audi = Coche()

print(audi.Cilindrada)
