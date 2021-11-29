from .widget import Widget
import pygame


# --------------------------------------------------
# Text class
# Based on pygame's font and label features
# Notice that in the Setters we need to re-render the font when we modify the parameters.
# --------------------------------------------------


class Text(Widget):

    # Constructor
    def __init__(self, x, y, size, text, path_to_font):
        self.text = text
        self.size = size
        self.color = (255, 255, 255)
        self.path_to_font = path_to_font
        self.font = pygame.font.Font(path_to_font, self.size)

        super().__init__(x, y, self.font.size(self.text)[0], self.font.size(self.text)[1])
        self.label = self.font.render(self.text, 1, self.color)

    # Renders the Text to the specified window.
    def render(self, window):
        self.label = self.font.render(self.text, 1, self.color)
        window.blit(self.label, (self.x, self.y))

    # Getters & Setters
    def getColor(self): return self.color
    def setColor(self, new_color): self.color = new_color

    def getSize(self): return self.size

    def setSize(self, new_size):
        self.size = new_size
        self.font = pygame.font.Font(self.path_to_font, new_size)

    def getText(self): return self.text

    def setText(self, new_text):
        self.text = new_text
        self.label = self.font.render(self.text, 1, self.color)

    def setFont(self, path_to_font):
        self.path_to_font = path_to_font
        self.font = pygame.font.Font(path_to_font, self.size)
