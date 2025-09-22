import numpy as np
class studant:
    def __init__(self,name,note1,note2,note3):
        self.name = name
        self.note1 = note1
        self.note2 = note2
        self.note3 = note3
    def totalNote(self):
        return self.note1 + self.note2 + self.note3 
    def average(self):
        return np.median(self.totalNote()) #PORQUE O NUMPY NAO FUNCIONA AQUI?
    def avaliation(self):
        if self.average >= 6.0:
            return f"Aprovate"
        else:
            return f"Reprovation"

studant1 = studant("GUSTAVO",7.0,8.0,9.0)

