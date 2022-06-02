from functions import create_grade, print_error, print_warning


class Subject:
    """
    This class represents a subject, which contains of a name and a list of grades (object).
    :param str name: The name of the subject.
    :param grade grades: A list of objects containing grades.
    """

    def __init__(self, name):
        self.name = name
        self.grades = []

    def average(self):
        """
        Calculate the average of the subject with consideration of the weighing and print it out.
        If there are no grades, it will print out an error message.
        """
        if not self.grades:
            print_error("Keine Noten vorhanden! Bitte erstelle eine Note")
            return

        total = 0
        sum_weighting = 0
        for e in self.grades:
            total = total + (e.grade * e.weighting)
            sum_weighting = sum_weighting + e.weighting

        print("\nDurchschnitt")
        print("---")
        print(round(total / sum_weighting, 3))

    def wish_grade(self):
        """
        Calculate the wish grade of the subject with consideration of the weighing and print it out.
        If there are no grades, it will print out an error message.
        Also, if the wish grade is not possible, there will also be an error message displayed.
        """
        total_existing_grades = 0
        wish_grade = float(input("Wunschnote:"))
        weighting_wish_grade = float(input("Gewichtung Wunschnote:"))
        total_weighting = weighting_wish_grade

        for e in self.grades:
            total_existing_grades = total_existing_grades + (e.grade * e.weighting)
            total_weighting = total_weighting + e.weighting

        result = ((wish_grade * total_weighting) - total_existing_grades) / weighting_wish_grade

        if 6 >= result >= 1:
            print("\nBenötigte Note")
            print("---")
            print(result)
        else:
            print_warning("Wunschnote nicht möglich")

    def add_grade(self):
        """
        Append a grade object to the grade's list.
        """
        self.grades.append(create_grade())
