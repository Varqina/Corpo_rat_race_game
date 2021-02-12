import random
from turtle import Turtle

from RatClassAI import RatClassAI


class RatClassUser(RatClassAI):
    def __init__(self, diligence, intellect, helpful, ambitious, sneaky, idler, color):
        super().__init__()
        self.diligence = diligence
        self.intellect = intellect
        self.helpful = helpful
        self.ambitious = ambitious
        self.sneaky = sneaky
        self.idler = idler
        self.color = color
        self.turtle.color(self.color)











