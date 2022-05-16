from colorama import Fore

from grade import Grade


def createGrade():
    while True:
        grade = float(input("Note (1-6):"))
        if 1 <= grade <= 6:
            break
        else:
            printError("Eingabe ungültig!")

    while True:
        weighting = int(input("Gewichtung (0-10):"))
        if 0 <= weighting <= 10:
            break
        else:
            printError("Eingabe ungültig!")

    return Grade(grade, weighting)


def printError(message):
    print(Fore.RED + "ERROR: " + message)
    print(Fore.RESET)


def printWarning(message):
    print(Fore.YELLOW + "WARN: " + message)
    print(Fore.RESET)
