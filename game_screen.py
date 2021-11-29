import pygame
from app.screen_manager import ScreenManager, GameStates
from app.screen import Screen
from ui.widget.spritebutton import SpriteButton
from ui.widget.widget import Widget, WidgetStates

from rendering.texture import Texture

from board import Board
from dice import Dice

# --------------------------------------------------
# GameScreen screen
# Contains the gameplay
# --------------------------------------------------


class GameScreen(Screen):

    # Concstructor
    def __init__(self, window, socket):
        super().__init__(window)
        self.socket = socket

        self.background = Texture.fromFile(0, 0, "textures/main_background2.jpg")
        self.background.scale(self.WIDTH, self.HEIGHT)

        self.leave_button = SpriteButton(20, 20, 75, 75, "textures/back-button.png", "", "fonts/passion_one.ttf")
        self.roll_button = SpriteButton(48, 450, 150, 45, "textures/button.png", "ROLL", "fonts/passion_one.ttf")

        self.dice = Dice(50, 300, 75, 75)
        self.board = Board(self.WIDTH / 2 - 246, self.HEIGHT / 2 -  246, 492, 492)
        self.board.addPawn("YoYo")
        self.board.addPawn("YoYoYo")
        

    # updates the screen
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ScreenManager.setActiveScreen(GameStates.MENU)
                    self.setRunning(False)

            self.leave_button.input(event)
            self.roll_button.input(event)

        if self.leave_button.getState() == WidgetStates.PRESSED:
            self.leave_button.setState(WidgetStates.REST)
            ScreenManager.setActiveScreen(GameStates.MENU)
            self.setRunning(False)
        
        if self.roll_button.getState() == WidgetStates.PRESSED:
            self.roll_button.setState(WidgetStates.REST)
            self.dice.roll()

        self.dice.update()
        self.board.update()

        #print("GAME FPS: ", self.getScreenFPS())

    # renders the screen
    def render(self):
        super().render()

        self.background.render(self.window)

        self.leave_button.render(self.window)
        self.roll_button.render(self.window)

        self.board.render(self.window)
        self.dice.render(self.window)

