from ..uicomponent import UIComponent

# --------------------------------------------------
# Layout class
# A Layout is a container that contains UIComponents
# such as buttons, texts, ...
# --------------------------------------------------


class Layout(UIComponent):

    # Constructor
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.components = list()

    # Add or remove components from the list.
    def addComponent(self, component): self.components.append(component)
    def removeComponent(self, component): self.components.remove(component)

    # Updates the state of all the components in the list.
    def input(self, event):
        for component in self.components:
            component.input(event)

    # Renders all the components in the list.
    def render(self, window):
        for component in self.components:
            component.render(window)

    # Getters & Setters
    def getComponents(self): return self.components

    def setX(self, new_x):
        vector_x = new_x - self.x
        for component in self.components:
            component.setX(component.getX() + vector_x)

        self.x = new_x

    def setY(self, new_y):
        vector_y = new_y - self.y
        for component in self.components:
            component.setY(component.getY() + vector_y)

        self.y = new_y


