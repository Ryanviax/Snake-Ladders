from app.gameobject import GameObject
from .texture import Texture
import pygame

# --------------------------------------------------
# SpriteSheet class
# Its a matrix of textures in a single image.
# Very useful to pack all the different textures for a single purpose.
# --------------------------------------------------


class SpriteSheet(GameObject):

    # Constructor
    def __init__(self, path, rows, cols, x, y):
        self.path = path
        self.rows = rows
        self.cols = cols

        self.sheet = pygame.image.load(path).convert_alpha()
        super().__init__(x, y, self.sheet.get_width(), self.sheet.get_height())

    # Returns the texture which is at the specified indexed coordinates.
    def getTextureAt(self, index_x, index_y):
        w = self.width / self.cols
        h = self.height / self.rows
        x = index_x * w
        y = index_y * h

        image = pygame.Surface([w, h], pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        texture = Texture(self.x, self.y, image)

        return texture

    # Returns all the rows of the Texture matrix as a line.
    def getTexturesAsLine(self):
        result = []
        for i in range(self.rows):
            for j in range(self.cols):
                result.append(self.getTextureAt(j, i))

        return result

    # Returns a matrix of Textures.
    def getTexturesAsMatrix(self):
        result = [[None for i in range(self.cols)] for j in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                result[row][col] = self.getTextureAt(row, col)

        return result

    # Getters & Setters
    def getFrameWidth(self): return self.sheet.get_width() / self.cols
    def getFrameHeight(self): return self.sheet.get_height() / self.rows

    def getCols(self): return self.cols
    def getRows(self): return self.rows
