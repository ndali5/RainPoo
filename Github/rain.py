from Github import core
from Github.drop import Drop

drops = []


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1600, 800]

    for i in range(0, 1000):
        drops.append(Drop(1600))

    print("Setup END-----------")


def run():
    print("Run")
    for d in drops:
        d.tomber(800)
        d.afficher(core)


core.main(setup, run)
