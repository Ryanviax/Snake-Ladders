# --------------------------------------------------
# GameObject class
# Every object in the game will extend this class.
# It contains common information and methods
# that every object has.
# --------------------------------------------------


class GameObject:

    # Constructor
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Getters & Setters
    def getX(self): return self.x
    def setX(self, new_x): self.x = new_x

    def getY(self): return self.y
    def setY(self, new_y): self.y = new_y

    def getWidth(self): return self.width
    def setWidth(self, new_width): self.width = new_width

    def getHeight(self): return self.height
    def setHeight(self, new_height): self.height = new_height

    def getCenterX(self): return self.x + self.width / 2
    def getCenterY(self): return self.y + self.height / 2
    def getCenter(self): return self.x + self.width / 2, self.y + self.height / 2

    def setCenterX(self, x): self.x = x - self.width / 2
    def setCenterY(self, y): self.y = y - self.height / 2
    def setCenter(self, pos):
        self.x = pos[0] - self.width / 2
        self.y = pos[1] - self.height / 2