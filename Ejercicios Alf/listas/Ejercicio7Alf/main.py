import string
alphabet = list(string.ascii_lowercase)
multiples = []

for letra in alphabet:
    if alphabet.index(letra) % 3 == 0 and alphabet.index(letra) != 0:
        multiples.append(letra)
for multiplo in multiples:
    alphabet.remove(multiplo)
print(alphabet)