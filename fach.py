class Fach:

    def __init__(self, name, noten):
        self.name = name
        self.noten = noten

    def durchschnitt(self):
        a = sum(self.noten)
        return a / len(self.noten)