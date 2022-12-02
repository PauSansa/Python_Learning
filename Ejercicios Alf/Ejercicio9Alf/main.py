print("Di una palabra")
word = input()
vocals = ["a","e","i","o","u"]
numVocals= {"a":0, "e":0, "i":0, "o":0, "u":0}
wordList = list(word)
#compara cada item de la lista wordList con la de vocals
for letter in wordList:
    for letterv in vocals:
        if letter == letterv:
            #cuando encuentra que son iguales le suma uno al valor de la key letter
            numVocals[letter] += 1

print("La palabra que has introducido tiene:")
for vocal in numVocals:
    if numVocals[vocal] != 0:
        print(str(numVocals[vocal]) + " " + str(vocal).upper() + "'s")





