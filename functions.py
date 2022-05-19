from grade import Grade


def create_grade():
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
    print("\033[91mERROR: " + message + "\033[0m")


def print_warning(message):
    print("\033[93mWARN: " + message + "\033[0m")
