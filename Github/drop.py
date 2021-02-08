from random import random

from pygame.math import Vector2


class Drop:

    def __init__(self):
        self.gravity = random.ramdint(5, 20)
        self.size = 2
        self.R = 255
        self.v = 0
        self.B = 112
        self.position = Vector2(50, 50)

    def tomber(self, taillefenetre):
        self.position.y = self.position.y + self.gravity
        if self.position.y > taillefenetre:
            self.raz()

    def raz(self):
        self.position.y = 0
