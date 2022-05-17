from subject import Subject
from functions import print_error, print_warning
import pickle
import os


def chose_subject():
    if len(all_subjects) == 0:
        print_error("Keine Fächer zur Auswahl vorhanden! Bitte Fach erstellen.")
        return

    while True:
        print("Wähle ein Fach aus folgender Liste aus:")
        print(", ".join(all_subjects.keys()))
        chosen_subject = input()

        if chosen_subject in all_subjects:
            return chosen_subject
        else:
            print_warning("Ausgewähltes Fach nicht vorhanden!")


# app = QApplication(sys.argv)
# screen = Window(mathe)
# screen.show()
# sys.exit(app.exec())

# Load all subjects into the dictionary list
all_subjects = {}
for filename in os.listdir("./subjects"):
    with open(os.path.join("./subjects", filename), 'rb') as f:
        data = pickle.load(f)
        all_subjects.update({data.name: data})
        f.close()

while True:
    print("\nWelche operation möchtest du ausführen?")
    operation = int(input("(1) Fächer anzeigen | (2) Fach hinzufügen | (3) Fach löschen | (4) Noten anzeigen | (5) Note hinzufügen | (6) Note löschen | (7) Durchschnitt | (8) Wunschnote | (0) Abbruch"))

    match operation:
        case 0:
            for key, value in all_subjects.items():
                f = open("./subjects/" + key + ".txt", "wb")
                pickle.dump(value, f)
                f.close()
            break
        case 1:
            print("\nFächer")
            print("---")
            for subject in all_subjects.values():
                print(subject.name)
        case 2:
            while True:
                name = input("Bitte name vom Fach eingeben: ")

                if name not in all_subjects:
                    all_subjects.update({name: Subject(name)})
                    break

                print_warning("Fach existiert bereits!")
        case 3:
            chosen_subject = all_subjects.get(chose_subject())
            if chosen_subject is None:
                continue

            del all_subjects[chosen_subject.name]
            if os.path.exists("./subjects/" + chosen_subject.name + ".txt"):
                os.remove("./subjects/" + chosen_subject.name + ".txt")
        case 4:
            chosen_subject = all_subjects.get(chose_subject())
            if chosen_subject is None:
                continue

            print("\nNote | Gewichtung")
            print("---")
            for grade in chosen_subject.grades:
                print(grade.grade, " | ", grade.weighting)
        case 5:
            chosen_subject = all_subjects.get(chose_subject())
            if chosen_subject is None:
                continue

            all_subjects.get(chosen_subject.name).add_grade()
        case 6:
            chosen_subject = all_subjects.get(chose_subject())
            if chosen_subject is None:
                continue

            print("\nNr. | Note | Gewichtung")
            print("---")
            for index, grade in enumerate(chosen_subject.grades):
                print(index, " | ", grade.grade, " | ", grade.weighting)

            nr = int(input("Welche Note möchten sie löschen?"))
            del chosen_subject.grades[nr]
        case 7:
            chosen_subject = all_subjects.get(chose_subject())
            if chosen_subject is None:
                continue

            all_subjects.get(chosen_subject.name).average()
        case 8:
            chosen_subject = all_subjects.get(chose_subject())
            if chosen_subject is None:
                continue

            all_subjects.get(chosen_subject.name).wish_grade()
        case _:
            print_error("Operation nicht vorhaden!")
