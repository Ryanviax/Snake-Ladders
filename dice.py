import random
import time
from rendering.animation import Animation
from rendering.spritesheet import SpriteSheet

from app.gameobject import GameObject

class Dice(GameObject):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.number = random.randint(1, 6)

        self.animation = Animation(6, 5, True)

        self.spritesheet = SpriteSheet("textures/diceys.png", 1, 6, self.x, self.y)
        self.textures = self.spritesheet.getTexturesAsLine()

        self.started_timer = False
        self.tic = 0

    def roll(self):
        self.number = random.randint(1, 6)
        print("Chosen number: ", self.number)
        self.animation.play()
        self.started_timer = True

    def update(self):
        if self.started_timer == False:
            self.tic = time.perf_counter()

        #print(time.perf_counter() - self.tic)
        if (time.perf_counter() - self.tic) > 3 and self.animation.getCurrentFrame() == (self.number - 1):
            self.animation.stop()
            self.started_timer = False
            
        self.animation.update()

    def render(self, window):
        self.textures[self.animation.getCurrentFrame()].render(window)