import enum

# --------------------------------------------------
# ScreenManager class
# Manages all the screens inside the game.
# No constructor, it's a static class, accessible anywhere.
# One screen is active at a time, OBVIOUSLY.
# --------------------------------------------------


class GameStates(enum.Enum):
    QUIT = 0
    MENU = 1
    GAME = 2
    LOBBY = 3


class ScreenManager:

    active_screen = GameStates.MENU

    # Changes the currently visible screen to the specified one.
    @staticmethod
    def setActiveScreen(screen): ScreenManager.active_screen = screen

    @staticmethod
    def getActiveScreen(): return ScreenManager.active_screen

