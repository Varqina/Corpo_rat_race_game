import random


class RatClass:
    diligence = 0
    intellect = 0
    helpful = 0
    ambitious = 0
    sneaky = 0
    idler = 0
    color = "gray"

    def setup_random_parameters(self):
        for i in range(10):
            ability = random.randint(0, 5)
            if ability == 0 : self.diligence += 1
            if ability == 1 : self.intellect += 1
            if ability == 2 : self.helpful += 1
            if ability == 3 : self.ambitious += 1
            if ability == 4 : self.sneaky += 1
            if ability == 5 : self.idler += 1

    def setup_parameters(self, diligence, intellect, helpful, ambitious, sneaky, idler, color):
        self.diligence = diligence
        self.intellect = intellect
        self.helpful = helpful
        self.ambitious = ambitious
        self.sneaky = sneaky
        self.idler = idler
        self.color = color










