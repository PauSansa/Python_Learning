subjects = ["Mátematicas", "física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = int(input("Que nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que recuperar " + str(subjects))

