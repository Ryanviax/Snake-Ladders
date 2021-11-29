import enum

# --------------------------------------------------
# Alignment & Gravity enumerations
# We use a combination of those two sets of values
# to position a UIComponent relative to the position of
# another UIComponent.
# --------------------------------------------------


class Alignment(enum.Enum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3


class Gravity(enum.Enum):
    NONE = 0
    START = 1
    CENTER = 2
    END = 3


class UIComponent:

    # Constructor
    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.margin = (0, 0, 0, 0) # constant : (left, right, top, down)
        self.parent = None

        self.showing = True

    # Aligns self relatively to the targeted UIComponent
    def align(self, target_component, alignment, gravity):
        # LEFT ALIGNMENT
        if alignment == Alignment.LEFT and gravity == Gravity.NONE:
            self.x = target_component.getX() - self.width - self.margin[1]

        elif alignment == Alignment.LEFT and gravity == Gravity.START:
            self.x = target_component.getX() - self.width - self.margin[1]
            self.y = target_component.getY()

        elif alignment == Alignment.LEFT and gravity == Gravity.CENTER:
            self.x = target_component.getX() - self.width - self.margin[1]
            self.setCenterY(target_component.getCenterY())

        elif alignment == Alignment.LEFT and gravity == Gravity.END:
            self.x = target_component.getX() - self.width - self.margin[0]
            self.y = target_component.getY() + target_component.getHeight() - self.height

        # RIGHT ALIGNMENT
        elif alignment == Alignment.RIGHT and gravity == Gravity.NONE:
            self.x = target_component.getX() + target_component.getWidth() + self.margin[0]

        elif alignment == Alignment.RIGHT and gravity == Gravity.START:
            self.x = target_component.getX() + target_component.getWidth() + self.margin[0]
            self.y = target_component.getY()

        elif alignment == Alignment.RIGHT and gravity == Gravity.CENTER:
            self.x = target_component.getX() + target_component.getWidth() + self.margin[0]
            self.setCenterY(target_component.getCenterY())

        elif alignment == Alignment.RIGHT and gravity == Gravity.END:
            self.x = target_component.getX() + target_component.getWidth() + self.margin[0]
            self.y = target_component.getY() + target_component.getHeight() - self.height

        # TOP ALIGNMENT
        elif alignment == Alignment.TOP and gravity == Gravity.NONE:
            self.y = target_component.getY() - self.height - self.margin[3]

        elif alignment == Alignment.TOP and gravity == Gravity.START:
            self.x = target_component.getX()
            self.y = target_component.getY() - self.height - self.margin[3]

        elif alignment == Alignment.TOP and gravity == Gravity.CENTER:
            self.setCenterX(target_component.getCenterX())
            self.y = target_component.getY() - self.height - self.margin[3]

        elif alignment == Alignment.TOP and gravity == Gravity.END:
            self.x = target_component.getX() + target_component.getWidth() - self.width
            self.y = target_component.getY() - self.height - self.margin[3]

        # BOTTOM ALIGNMENT
        elif alignment == Alignment.BOTTOM and gravity == Gravity.NONE:
            self.y = target_component.getY() + target_component.getHeight() + self.margin[2]

        elif alignment == Alignment.BOTTOM and gravity == Gravity.START:
            self.x = target_component.getX()
            self.y = target_component.getY() + target_component.getHeight() + self.margin[2]

        elif alignment == Alignment.BOTTOM and gravity == Gravity.CENTER:
            self.setCenterX(target_component.getCenterX())
            self.y = target_component.getY() + target_component.getHeight() + self.margin[2]

        elif alignment == Alignment.BOTTOM and gravity == Gravity.END:
            self.x = target_component.getX() + target_component.getWidth() - self.width
            self.y = target_component.getY() + target_component.getHeight() + self.margin[2]

    # Aligns self relatively to its parent
    def alignInParent(self, alignment, gravity):
        # LEFT ALIGNMENT
        if alignment == Alignment.LEFT and gravity == Gravity.NONE:
            self.x = self.parent.getX() + self.margin[0]

        elif alignment == Alignment.LEFT and gravity == Gravity.START:
            self.x = self.parent.getX() + self.margin[0]
            self.y = self.parent.getY() + self.margin[2]

        elif alignment == Alignment.LEFT and gravity == Gravity.CENTER:
            self.x = self.parent.getX() + self.margin[0]
            self.setCenterY(self.parent.getCenterY())

        elif alignment == Alignment.LEFT and gravity == Gravity.END:
            self.x = self.parent.getX() + self.margin[0]
            self.y = self.parent.getY() + self.parent.getHeight() - self.height - self.margin[3]

        # RIGHT ALIGNMENT
        elif alignment == Alignment.RIGHT and gravity == Gravity.NONE:
            self.x = self.parent.getX() + self.parent.getWidth() - self.width - self.margin[1]

        elif alignment == Alignment.RIGHT and gravity == Gravity.START:
            self.x = self.parent.getX() + self.parent.getWidth() - self.width - self.margin[1]
            self.y = self.parent.getY() + self.margin[2]

        elif alignment == Alignment.RIGHT and gravity == Gravity.CENTER:
            self.x = self.parent.getX() + self.parent.getWidth() - self.width - self.margin[1]
            self.setCenterY(self.parent.getCenterY())

        elif alignment == Alignment.RIGHT and gravity == Gravity.END:
            self.x = self.parent.getX() + self.parent.getWidth() - self.width - self.margin[1]
            self.y = self.parent.getY() + self.parent.getHeight() - self.height - self.margin[3]

        # TOP ALIGNMENT
        elif alignment == Alignment.TOP and gravity == Gravity.NONE:
            self.y = self.parent.getY() + self.margin[2]

        elif alignment == Alignment.TOP and gravity == Gravity.START:
            self.x = self.parent.getX() + self.margin[0]
            self.y = self.parent.getY() + self.margin[2]

        elif alignment == Alignment.TOP and gravity == Gravity.CENTER:
            self.setCenterX(self.parent.getCenterX())
            self.y = self.parent.getY() + self.margin[2]

        elif alignment == Alignment.TOP and gravity == Gravity.END:
            self.x = self.parent.getX() + self.parent.getWidth() - self.width - self.margin[1]
            self.y = self.parent.getY() + self.margin[2]

        # BOTTOM ALIGNMENT
        elif alignment == Alignment.BOTTOM and gravity == Gravity.NONE:
            self.y = self.parent.getY() + self.parent.getHeight() - self.height - self.margin[3]

        elif alignment == Alignment.BOTTOM and gravity == Gravity.START:
            self.x = self.parent.getX() + self.margin[0]
            self.y = self.parent.getY() + self.parent.getHeight() - self.margin[3]

        elif alignment == Alignment.BOTTOM and gravity == Gravity.CENTER:
            self.setCenterX(self.parent.getCenterX())
            self.y = self.parent.getY() + self.parent.getHeight() - self.margin[3]

        elif alignment == Alignment.BOTTOM and gravity == Gravity.END:
            self.x = self.parent.getX() + self.parent.getWidth() - self.width - self.margin[1]
            self.y = self.parent.getY() + self.parent.getHeight() - self.margin[3]

    def show(self): self.showing = True
    def hide(self): self.showing = False

    # Getters & Setters
    def getX(self): return self.x
    def getCenterX(self): return self.x + self.width / 2
    def setX(self, new_x): self.x = new_x
    def setCenterX(self, new_center_x): self.x = new_center_x - self.width / 2

    def getY(self): return self.y
    def getCenterY(self): return self.y + self.height / 2
    def setY(self, new_y): self.y = new_y
    def setCenterY(self, new_center_y): self.y = new_center_y - self.height / 2

    def getWidth(self): return self.width
    def setWidth(self, new_width): self.width = new_width

    def getHeight(self): return self.height
    def setHeight(self, new_height): self.height = new_height

    def getMargin(self): return self.margin
    def setMargin(self, new_margin): self.margin = new_margin

    def getParent(self): return self.parent
    def setParent(self, new_parent): self.parent = new_parent
