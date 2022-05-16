from colorama import Fore

from subject import Subject
from functions import printError
from grade import Grade


# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Notenrechner - unterstützt Schüler beim Ausrechnen ihres Notendurchschnitts
# Copyright (C) 2022 Noel Oliveira, Alexander Wirz, Patrice Blechschmidt

# In unserem Notenrechner kann der Benutzer seine gewünschten Fächer und in einem
# nächsten Schritt die einzelnen Noten und deren Gewichtung eintragen. Der Notenrechner
# berechnet automatisch die Durchschnittsnote der einzelnen Fächer. Des Weiteren kann eine
# Wunschdurchschnittsnote eingegeben werden und der Notenrechner berechnet die in der
# nächsten Prüfung benötigte Note.


# app = QApplication(sys.argv)
# screen = Window(mathe)
# screen.show()
# sys.exit(app.exec())

def chose_subject():
    if len(all_subjects) == 0:
        printError("Keine Fächer zur Auswahl vorhanden! Bitte Fach erstellen.")
        return

    print("Wähle ein Fach aus folgender Liste aus:")
    chosen_subject = input(print(",".join(all_subjects.keys())))

    if chosen_subject in all_subjects:
        return chosen_subject
    else:
        printError("Ausgewähltes Fach nicht vorhanden!")
        return


all_subjects = {}

while True:
    print("Welche operation möchtest du ausführen?")
    operation = int(
        input("(0) Abbruch | (1) Durchschnitt | (2) Wunschnote | (3) Note hinzufügen | (4) Fach hinzufügen: "))

    match operation:
        case 0:
            break
        case 1:
            chosen_subject = all_subjects.get(chose_subject())
            if chosen_subject is None:
                continue

            all_subjects.get(chosen_subject.name).average()
        case 2:
            chosen_subject = all_subjects.get(chose_subject())
            if chosen_subject is None:
                continue

            all_subjects.get(chosen_subject.name).wish_grade()
        case 3:
            chosen_subject = all_subjects.get(chose_subject())
            if chosen_subject is None:
                continue

            all_subjects.get(chosen_subject.name).add_grade()
        case 4:
            name = input("Bitte name vom Fach eingeben: ")
            all_subjects[name] = Subject(name)

            # file = open(name, 'wb')
            # exec("{} = {}" % (name, Fach(name, notenEingabe())))
            # notenEingabe()
            # pickle.dump(Fach(name), file)
        case _:
            printError("Operation nicht vorhaden!")
