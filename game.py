from app.screen_manager import ScreenManager, GameStates
import pygame
from menu_screen import MenuScreen
from game_screen import GameScreen
from lobby_screen import LobbyScreen

import socket
# --------------------------------------------------
# Game class
# Contains everything the game has
# Changes between screens
# --------------------------------------------------


class Game():

    # Constructor
    def __init__(self, width, height, pseudo):
        self.width = width
        self.height = height
        self.pseudo = pseudo

        pygame.init()
        self.window = pygame.display.set_mode((width, height), pygame.NOFRAME | pygame.DOUBLEBUF)
        self.running = True
        self.screen_manager = ScreenManager()

        # Networking
        self.socket = socket.socket()

        # Screens
        self.menu_screen = MenuScreen(self.window)
        self.lobby_screen = None #LobbyScreen(self.window, self.socket)
        self.game_screen = None  #GameScreen(self.window, self.socket)

        

    # runs the game
    def run(self, fps):
        

        while self.running:

            # Menu
            if self.screen_manager.getActiveScreen() == GameStates.MENU:
                self.menu_screen.setRunning(True)
                if self.game_screen != None: self.game_screen.setRunning(False)
                if self.lobby_screen != None: self.lobby_screen.setRunning(False)

                self.menu_screen.loop(fps)
            
            # Lobby
            if self.screen_manager.getActiveScreen() == GameStates.LOBBY:
                self.lobby_screen = LobbyScreen(self.window, self.socket)
                self.lobby_screen.loop(fps)
                self.lobby_screen.setRunning(True)

                self.menu_screen.setRunning(False)
                if self.game_screen != None: self.game_screen.setRunning(False)

                

            # Game
            elif self.screen_manager.getActiveScreen() == GameStates.GAME:
                self.game_screen = GameScreen(self.window, self.socket)
                self.game_screen.loop(fps)
                self.game_screen.setRunning(True)
                
                self.menu_screen.setRunning(False)
                self.lobby_screen.setRunning(False)

                
            # Quit
            elif self.screen_manager.getActiveScreen() == GameStates.QUIT:
                if self.game_screen != None: self.game_screen.setRunning(False)
                self.menu_screen.setRunning(False)
                if self.lobby_screen != None: self.lobby_screen.setRunning(False)

                self.socket.close()
                self.running = False
    
    def quit(self): pygame.quit()

    def getScreenManager(self): return self.screen_manager
    def setRunning(self, running): self.running = running