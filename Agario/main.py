from Agario import core, player
from Agario.bille import Bille
from Agario.creep import Creep, creep1
from Agario.player import Player



mon_joueur1 = None
creep1 = []
bille1 = None


def setup():
    print("setup START------")
    core.fps = 30
    core.WINDOW_SIZE = [1200 , 600]

    global mon_joueur1
    mon_joueur1=Player()

    print("Setup END---------")

def run():
    for c in creep1:
        c.afficher(core)

    mon_joueur1.afficher(core)
    if core.getMouseLeftClick() is not None:
        mon_joueur1.deplacer(core.getMouseLeftClick())




if __name__ == '__main__' :
    core.main(setup,run)
