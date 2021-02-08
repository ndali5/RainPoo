import random
import pygame
from pygame.rect import Rect
import core



def setup():
    print("Setup START---------")
    core.fps = 1
    core.WINDOW_SIZE = [400, 400]
    print("Setup END-----------")

def run():

    pygame.draw.circle(core.screen,(255, 255, 255),(200,200),100,1)
    pygame.draw.rect(core.screen,(0, 255, 0),Rect((100, 100), (200, 200)),1)

    count = 0
    for i in range(0,100000):
        x = random.uniform(100, 300)
        y = random.uniform(100, 300)

        dist = (200-x)*(200-x)+(200-y)*(200-y)

        if dist < 100*100 :
            pygame.draw.circle(core.screen, (0, 0, 255), (int(x), int(y)), 2, 1)
            count+=1
        else :
            pygame.draw.circle(core.screen, (255, 0, 0), (int(x), int(y)), 2, 1)

    pi = float(4 * count/100000.0)
    print("PI : ")
    print(pi)
    core.noLoop()





core.main(setup,run)


