from .widget import Widget
from rendering.spritesheet import SpriteSheet
from .text import Text

# --------------------------------------------------
# SpriteButton class
# Its a Text on top of a Texture.
# We use a SpriteSheet with 3 Textures for each Button state : REST - HOVER - PRESSED
# --------------------------------------------------


class SpriteButton(Widget):

    # Constructor
    def __init__(self, x, y, width, height, sprite_path, text, font_path):
        super().__init__(x, y, width, height)

        self.spritesheet = SpriteSheet(sprite_path, 1, 3, self.x, self.y)
        self.textures = self.spritesheet.getTexturesAsLine()

        for tex in self.textures:
           tex.scale(self.width, self.height)

        self.text = text
        self.text_size = int(self.height / 2)
        self.text_color = (0, 0, 0)
        self.font = font_path

        self.label = Text(x + self.width / 2, y + self.height / 2, self.text_size, self.text, self.font)
        self.label.setX(self.x + self.width / 2 - self.label.getWidth() / 2)
        self.label.setY(self.y + self.height / 2 - self.label.getHeight() / 2)
        self.label.setColor(self.text_color)

    # Renders the Button to the specified window.
    def render(self, window):
        self.textures[self.state.value].setX(self.x)
        self.textures[self.state.value].setY(self.y)
        self.textures[self.state.value].render(window)
        self.label.render(window)

    # Getters and Setters
    def getTextColor(self): return self.text_color
    def setTextColor(self, new_color):
        self.text_color = new_color
        self.label.setColor(new_color)

    def getText(self): return self.text
    def setText(self, new_text):
        self.text = new_text
        self.label.setText(new_text)

    def getLabel(self): return self.label

    def getTextSize(self): return self.text_size
    def setTextSize(self, new_size):
        self.text_size = new_size
        self.label.setSize(new_size)

    def setTextPosition(self, coords_in_button):
        self.label.setX(coords_in_button[0] + self.x)
        self.label.setY(coords_in_button[1] + self.y)

    def setFont(self, new_font_path):
        self.font = new_font_path
        self.label.setFont(new_font_path)


