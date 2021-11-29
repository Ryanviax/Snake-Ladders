from pygame.locals import *
#from ui import Button
#from ui.widget.widget import WidgetStates
#from ui.widget.spritebutton import SpriteButton
from game import Game

import sys
args = sys.argv
pseudo = args[1]
print("Client created with pseudo:", args[1])

# SCREEN CONFIGURATION
WIDTH = 1080
HEIGHT = 720
FPS = 60

def main():
    
    game = Game(WIDTH, HEIGHT, pseudo)          # Actually the creation of a client

    game.run(FPS)

    game.quit()

    #global running


if __name__ == "__main__":
    main()
