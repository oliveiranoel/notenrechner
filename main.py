import os

from functions import print_error, print_warning, choose_subject, loadAllSubjectsFromFiles, saveAllSubjectsToFiles, \
    displayAllSubjects
from subject import Subject

# Load all subjects from the files into the dictionary list
all_subjects = loadAllSubjectsFromFiles()


# The loop will be repeated as long as the user doesn't enter the number 0.
while True:
    print("\nWelche operation möchtest du ausführen?")
    operation = int(input("(1) Fächer anzeigen | (2) Fach hinzufügen | (3) Fach löschen | (4) Noten anzeigen | (5) "
                          "Note hinzufügen | (6) Note löschen | (7) Durchschnitt | (8) Wunschnote | (0) Abbruch"))

    match operation:
        case 0:
            # Save all subjects to files and exit the loop.
            saveAllSubjectsToFiles(all_subjects)
            break
        case 1:
            # Print out all the subjects
            displayAllSubjects(all_subjects)
        case 2:
            # Unless it's not available yet, add a new subject. Otherwise, print error message.
            while True:
                name = input("Bitte name vom Fach eingeben: ")

                if name not in all_subjects:
                    all_subjects.update({name: Subject(name)})
                    break

                print_warning("Fach existiert bereits!")
        case 3:
            # Delete the chosen subject and also, if present, the file for it.
            chosen_subject = all_subjects.get(choose_subject(all_subjects))

            del all_subjects[chosen_subject.name]
            if os.path.exists("./subjects/" + chosen_subject.name + ".txt"):
                os.remove("./subjects/" + chosen_subject.name + ".txt")
        case 4:
            # Print out all the grades for a subject with their weighting.
            chosen_subject = all_subjects.get(choose_subject(all_subjects))

            print("\nNote | Gewichtung")
            print("---")
            for grade in chosen_subject.grades:
                print(grade.grade, " | ", grade.weighting)
        case 5:
            # Add a grade to the chosen subject
            chosen_subject = all_subjects.get(choose_subject(all_subjects))
            all_subjects.get(chosen_subject.name).add_grade()
        case 6:
            # Delete a chosen grade from a chosen subject.
            chosen_subject = all_subjects.get(choose_subject(all_subjects))

            print("\nNr. | Note | Gewichtung")
            print("---")
            for index, grade in enumerate(chosen_subject.grades):
                print(index, " | ", grade.grade, " | ", grade.weighting)

            nr = int(input("Welche Note möchten sie löschen?"))
            del chosen_subject.grades[nr]
        case 7:
            # Get the average grade for the chosen subject.
            chosen_subject = all_subjects.get(choose_subject(all_subjects))
            all_subjects.get(chosen_subject.name).average()
        case 8:
            # Get the wish grade for the chosen subject.
            chosen_subject = all_subjects.get(choose_subject(all_subjects))
            all_subjects.get(chosen_subject.name).wish_grade()
        case _:
            # Print error message if a operation was chosen, which is not available,
            print_error("Operation nicht vorhaden!")
