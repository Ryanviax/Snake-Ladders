from app.screen_manager import ScreenManager, GameStates
from app.screen import Screen
from rendering.texture import Texture
from ui.widget.spritebutton import SpriteButton
from ui.widget.widget import WidgetStates
import pygame

# --------------------------------------------------
# MenuScreen screen
# Contains the main menu
# --------------------------------------------------


class MenuScreen(Screen):

    def __init__(self, window):
        super().__init__(window)

        self.background = Texture.fromFile(0, 0, "textures/main_background2.jpg")
        self.background.scale(self.WIDTH, self.HEIGHT)

        self.join_button = SpriteButton(self.WIDTH / 2 - 150, self.HEIGHT / 2 - 213, 300, 125, "textures/button.png", "JOIN", "fonts/passion_one.ttf")
        self.join_button.setTextColor((30, 30, 30))

        self.create_button = SpriteButton(self.WIDTH / 2 - 150, self.HEIGHT / 2 - 63, 300, 125, "textures/button.png", "CREATE", "fonts/passion_one.ttf")
        self.create_button.setTextColor((30, 30, 30))

        self.quit_button = SpriteButton(self.WIDTH / 2 - 150, self.HEIGHT / 2 + 87, 300, 125, "textures/button.png", "QUIT", "fonts/passion_one.ttf")
        self.quit_button.setTextColor((30, 30, 30))

    # updates the screen
    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.setRunning(False)

            self.join_button.input(event)
            self.create_button.input(event)
            self.quit_button.input(event)

        if self.join_button.getState() == WidgetStates.PRESSED:
            self.join_button.setState(WidgetStates.REST)
            ScreenManager.setActiveScreen(GameStates.LOBBY)
            self.setRunning(False)

        if self.create_button.getState() == WidgetStates.PRESSED:
            self.create_button.setState(WidgetStates.REST)
            ScreenManager.setActiveScreen(GameStates.GAME)
            self.setRunning(False)

        if self.quit_button.getState() == WidgetStates.PRESSED:
            ScreenManager.setActiveScreen(GameStates.QUIT)
            self.setRunning(False)


    # renders the screen
    def render(self):
        self.window.fill((0, 125, 0))

        self.background.render(self.window)

        self.join_button.render(self.window)
        self.create_button.render(self.window)
        self.quit_button.render(self.window)

