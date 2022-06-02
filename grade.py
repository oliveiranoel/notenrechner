class Grade:
    """
        This class represents a grade as an object with two parameters. The object is used within a Subject
        :param int grade: The grade between 1-6.
        :param float weighting: The weighting of the grade on how much it counts between 0 - 10.
    """

    def __init__(self, grade, weighting):
        self.grade = grade
        self.weighting = weighting
