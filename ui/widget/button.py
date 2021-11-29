from .widget import Widget
from .text import Text
import pygame

# --------------------------------------------------
# Button class
# Pretty much a Text on top of a rectangle.
# --------------------------------------------------


class Button(Widget):

    # Constructor
    def __init__(self, x, y, width, height, color, text, font_path):
        super().__init__(x, y, width, height)
        self.background_color = color

        self.text = text
        self.text_color = (255, 255, 255)   # Default Text color
        self.text_size = int(self.height / 2)
        self.font = font_path

        self.label = Text(x + self.width / 2, y + self.height / 2, self.text_size, self.text, font_path)
        self.label.setColor(self.text_color)
        self.label.setX(self.x + self.width / 2 - self.label.getWidth() / 2)
        self.label.setY(self.y + self.height / 2 - self.label.getHeight() / 2)



    # Renders the Button to the specified window.
    def render(self, window):
        pygame.draw.rect(window, self.background_color, (self.x, self.y, self.width, self.height))
        self.label.render(window)

    # Getters & Setters
    def getBackgroundColor(self): return self.background_color
    def setBackgroundColor(self, new_color): self.background_color = new_color

    def getTextColor(self): return self.text_color
    def setTextColor(self, new_color):
        self.text_color = new_color
        self.label.setColor(new_color)

    def getText(self): return self.text
    def setText(self, new_text):
        self.text = new_text
        self.label.setText(new_text)

    def getTextSize(self): return self.text_size
    def setTextSize(self, new_size):
        self.text_size = new_size
        self.label.setSize(new_size)

    def setFont(self, new_font_path):
        self.font = new_font_path
        self.label.setFont(new_font_path)
