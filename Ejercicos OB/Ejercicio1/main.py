class Vehiculo():

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


    def __str__(self):
        return "Color {}, {} Ruedas y {} puertas".format(self.color, self.ruedas, self.puertas)

Audi = Vehiculo("Negro", 4, 3)

print(Audi)
