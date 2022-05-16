from functions import createGrade, printWarning, printError


class Subject:

    def __init__(self, name):
        self.name = name
        self.grades = []

    def average(self):
        if not self.grades:
            printError("Keine Noten vorhanden! Bitte erstelle eine Note")
            return

        total = 0
        sum_weighting = 0
        for e in self.grades:
            total = total + (e.grade * e.weighting)
            sum_weighting = sum_weighting + e.weighting

        print(round(total / sum_weighting, 3))

    def wish_grade(self):
        total_existing_grades = 0
        wish_grade = float(input("Wunschnote:"))
        weighting_wish_grade = float(input("Gewichtung Wunschnote:"))
        total_weighting = weighting_wish_grade

        for e in self.grades:
            total_existing_grades = total_existing_grades + (e.grade * e.weighting)
            total_weighting = total_weighting + e.weighting

        result = ((wish_grade * total_weighting) - total_existing_grades) / weighting_wish_grade

        if 6 >= result >= 1:
            print(result)
        else:
            printWarning("Wunschnote nicht möglich")

    def add_grade(self):
        self.grades.append(createGrade())

