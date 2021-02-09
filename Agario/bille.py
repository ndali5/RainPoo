from pygame.math import Vector2, Vector3


class Bille:

    def __init__(self):
        self.taille = 2
        self.vitesse = 2
        self.direction = Vector2()
        self.position = Vector2()
        self.couleur = Vector3()

    def suivre(self):
        pass

    def mourir(self):
        pass

    def manger(self):
        pass

    def afficher(self):
        pass