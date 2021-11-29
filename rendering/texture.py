from app.gameobject import GameObject
import pygame

# --------------------------------------------------
# Texture class
# Extends GameObject class.
# Based on pygame's Surface class.
# Two ways you can initialise it : using a Surface or using a path to an image (png).
# --------------------------------------------------


class Texture(GameObject):

    # Constructor
    def __init__(self, x, y, surface):
        self.image = surface
        super().__init__(x, y, surface.get_width(), surface.get_height())

    # Class method that is used as a "second constructor"
    @classmethod
    def fromFile(cls, x, y, path):
        return cls(x, y, pygame.image.load(path).convert_alpha())

    # Renders the texture to the specified window.
    def render(self, window):
        window.blit(self.image, (self.x, self.y))

    # Scales the texture according to the specified dimensions.
    def scale(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        self.image = pygame.transform.scale(self.image, (new_width, new_height))