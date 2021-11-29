from .layout import Layout

# --------------------------------------------------
# Popup class
# It's a custom Layout.
# --------------------------------------------------


class Popup(Layout):

    # Constructor
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def input(self, event):
        super().input(event)

    def render(self, window):
        super().render(window)

