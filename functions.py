import os
import pickle

from grade import Grade


def create_grade():
    """
    Create a grade object with the weighting. If a false grade (1-6) or weighting (0-10) value is entered, an error
    message will be displayed.
    :return: A grade object with the grade and weighting
    """
    while True:
        grade = float(input("Note (1-6):"))
        if 1 <= grade <= 6:
            break
        else:
            print_warning("Eingabe ungültig!")

    while True:
        weighting = int(input("Gewichtung (0-10):"))
        if 0 <= weighting <= 10:
            break
        else:
            print_warning("Eingabe ungültig!")

    return Grade(grade, weighting)


def print_error(message):
    """
    Display an error message in red Text.
    :param message: The message to be displayed.
    """
    print("\033[91mERROR: " + message + "\033[0m")


def print_warning(message):
    """
    Display an warning message in orange Text.
    :param message: The message to be displayed.
    """
    print("\033[93mWARN: " + message + "\033[0m")


def choose_subject(all_subjects):
    """
    Chose a subject from all existing subjects. If a subject name is entered, which doesn't exist, an error message
    will be displayed. Also, if there are no subjects to choose from, an error will be displayed.
    :return: All the subjects that were loaded from the files.
    """
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


def loadAllSubjectsFromFiles():
    """
    Load all Files from the subjects folder, convert them to objects and save as dictionary of objects with the name
    of the subject as key.
    :return: All the subjects that were loaded from the files.
    """
    all_subjects = {}
    for filename in os.listdir("./subjects"):
        with open(os.path.join("./subjects", filename), 'rb') as f:
            data = pickle.load(f)
            f.close()
            all_subjects.update({data.name: data})
    return all_subjects


def saveAllSubjectsToFiles(all_subjects):
    """
    Saves all subjects in one each file to the subject folder.
    :param all_subjects: All subjects that were available during runtime
    """
    for key, value in all_subjects.items():
        f = open("./subjects/" + key + ".txt", "wb")
        pickle.dump(value, f)
        f.close()


def displayAllSubjects(all_subjects):
    """
    Print out all the subjects
    :param all_subjects: All the subjects
    """
    if all_subjects:
        print("\nFächer")
        print("---")
        for subject in all_subjects.values():
            print(subject.name)
    else:
        print_error("Keine Fächer zur Auswahl vorhanden! Bitte Fach erstellen.")
