import pygame
import time

# --------------------------------------------------
# Screen class
# Represents a "page" of the game like the Menu for example.
# Each Screen has its own loop inside of which there is a timer.
# Game ticks are restricted to the same amount for every user.
# Game fps are not.
# --------------------------------------------------


class Screen:

    # Constructor
    def __init__(self, window):
        self.window = window
        self.running = True
        self.ticks = 0
        self.frames = 0
        self.current_fps = 0

        self.WIDTH, self.HEIGHT = pygame.display.get_surface().get_size()

        #self.WIDTH = Utils.getWindowDimension()[0]
        #self.HEIGHT = Utils.getWindowDimension()[1]

    # Screen's main loop, contains timer.
    def loop(self, fps):
        started = time.time()

        before = time.time_ns()
        elapsed = 0
        ns = 1000000000.0 / fps

        timer = 0
        start = started

        while self.isRunning():
            now = time.time_ns()
            elapsed = now - before
            tick = False
            render = False

            if elapsed >= ns:
                before += ns
                tick = True
                self.ticks += 1
            else:
                render = True
                self.frames += 1

            if tick: self.update()
            if render: self.render()

            pygame.display.flip()

            if time.time() - started > 1:
                started += 1
                self.current_fps = self.frames
                self.ticks = 0
                self.frames = 0

            timer = time.time() - start

    # Method to be extended by the child class.
    def update(self):
        pass

    # Method to be extended by the child class.
    def render(self):
        self.window.fill((0, 0, 0))

    def isRunning(self): return self.running
    def setRunning(self, state): self.running = state

    def getScreenFPS(self): return self.current_fps
    def getScreenTicks(self): return self.ticks
