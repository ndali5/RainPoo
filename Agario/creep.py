import pygame
from pygame.math import Vector2

from Agario import core

creep1 = []

class Creep:

    def __init__ (self) :
        self.taille = 5
        self.position = Vector2()


    def mourir(self):
        pass

    def afficher(self):
        for i in range(0, 1000):
            drops.append(Drop(1600))

        pygame.draw.circle(core.screen, (int(self.couleur.x), int(self.couleur.y), int(self.couleur.z)),
                           (int(self.position.x), int(self.position.y)), self.taille)
        pass