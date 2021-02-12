import random
from turtle import Turtle



class RatClassAI():
    def __init__(self):
        self.diligence = 0
        self.intellect = 0
        self.helpful = 0
        self.ambitious = 0
        self.sneaky = 0
        self.idler = 0
        self.color = "gray"
        self.turtle = Turtle()

    def setup_random_parameters(self):
        for i in range(10):
            ability = random.randint(0, 5)
            if ability == 0 : self.diligence += 1
            if ability == 1 : self.intellect += 1
            if ability == 2 : self.helpful += 1
            if ability == 3 : self.ambitious += 1
            if ability == 4 : self.sneaky += 1
            if ability == 5 : self.idler += 1









