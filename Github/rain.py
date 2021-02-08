from Github import core
from Github.drop import Drop

drops = []


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1600, 800]

    for i in range(0, 1000):
        drops.append(Drop(400))

    print("Setup END-----------")


def run():
    print("Run")
    for d in drops:
        d.tomber(400)
        d.afficher(core)


core.main(setup, run)
