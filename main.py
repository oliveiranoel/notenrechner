#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Notenrechner - unterstützt Schüler beim Ausrechnen ihres Notendurchschnitts
# Copyright (C) 2022 Noel Oliveira, Alexander Wirz, Patrice Blechschmidt

# In unserem Notenrechner kann der Benutzer seine gewünschten Fächer und in einem
# nächsten Schritt die einzelnen Noten und deren Gewichtung eintragen. Der Notenrechner
# berechnet automatisch die Durchschnittsnote der einzelnen Fächer. Des Weiteren kann eine
# Wunschdurchschnittsnote eingegeben werden und der Notenrechner berechnet die in der
# nächsten Prüfung benötigte Note.
from fach import Fach

fachMathe = Fach("mathe", [5, 6])

print(fachMathe.durchschnitt())

while True:
    a = float(input("Wunschnote:"))
    if a == 0:
        break
    else:
        print(fachMathe.wunschnote(a))
