# Notenrechner
from fach import Fach

fachMathe = Fach("mathe", [5, 6])

print(fachMathe.durchschnitt())
print(fachMathe.wunschnote(float(input("Wunschnote:"))))
