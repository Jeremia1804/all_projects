from Final import Final

file = Final()
valiny = file.preparer()
while file.depart != valiny:
    print(valiny.etat)
    print(valiny.matrice)
    print()
    valiny = valiny.predecesseur

print(valiny.etat)
print(valiny.matrice)
print()