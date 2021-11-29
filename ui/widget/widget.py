from ui.uicomponent import UIComponent
import pygame
import enum


class WidgetStates(enum.Enum):
    REST = 0
    HOVER = 1
    PRESSED = 2


class Widget(UIComponent):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.state = WidgetStates.REST

    def input(self, event):
        mouse_position = pygame.mouse.get_pos()

        self.state = WidgetStates.REST

        if self.x < mouse_position[0] < self.x + self.width:
            if self.y < mouse_position[1] < self.y + self.height:
                self.state = WidgetStates.HOVER

        if self.getState() == WidgetStates.HOVER:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = WidgetStates.PRESSED

    # render() : method to be implemented in the child class
    def render(self, window):
        pass

    def getState(self): return self.state
    def setState(self, new_state): self.state = new_state
