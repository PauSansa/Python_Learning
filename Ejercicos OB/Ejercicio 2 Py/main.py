class Alumno:
    nombre = ""
    nota = 0
    estaAprobado = ""

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        if nota >= 5:
            self.estaAprobado = "esta aprobado"
        else:
            self.estaAprobado = "esta suspendido"



    def __str__(self):
        return "El alumno {}, tiene una nota de {} y {}".format(self.nombre, self.nota, self.estaAprobado)


sansa = Alumno("Sansa", 5)
tete = Alumno("Tete", 3)
print(sansa)
print(tete)