class Fach:

    def __init__(self, name, noten):
        self.name = name
        self.noten = noten

    def durchschnitt(self):
        a = sum(self.noten)
        return a / len(self.noten)

    def wunschnote(self, wunschnote):
        a = wunschnote * (len(self.noten) + 1)
        return a - sum(self.noten)
