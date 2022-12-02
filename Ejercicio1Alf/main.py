#lista es con []
#tupla es con ()
lista = ["Matematicas","Física", "Química", "Historia", "Lengua"]
tupla = (1,2,3,4,5)
scores= []
for valor in lista:
    score = input("Que nota has sacado en "+valor +"?")
    scores.append(score)
for i in range(len(lista)):
    print("En la asignatura " + lista[i] + "has sacado " + scores[i])