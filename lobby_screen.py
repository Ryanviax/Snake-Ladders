import pygame
from app.screen_manager import ScreenManager, GameStates
from app.screen import Screen
from ui.widget.spritebutton import SpriteButton, Text
from ui.widget.widget import WidgetStates
from rendering.texture import Texture

import sys
import threading

# --------------------------------------------------
# LobbyScreen screen
# Contains the waiting room of the game
# --------------------------------------------------


class LobbyScreen(Screen):

    # Constructor
    def __init__(self, window, socket):
        super().__init__(window)
        self.socket = socket
        self.socket.connect(("127.0.0.1", 1233))

        # sending pseudo to server
        args = sys.argv
        self.pseudo = args[1]
        message = args[1]
        self.socket.send(message.encode('ascii'))

        self.nb_players = 1
        self.listening = False

        self.back_button = SpriteButton(20, 20, 75, 75, "textures/back-button.png", "", "fonts/passion_one.ttf")
        self.ready_button = SpriteButton(300, 550, 200, 75, "textures/green_button.png", "READY", "fonts/passion_one.ttf")
        self.ready_button.setTextColor((30, 30, 30))
        self.leave_button = SpriteButton(600, 550, 200, 75, "textures/red_button.png", "LEAVE", "fonts/passion_one.ttf")
        self.leave_button.setTextColor((30, 30, 30))

        self.players_text = Text(self.WIDTH - 150, 50, 25, "Players: ", "fonts/passion_one.ttf")

        self.box_texture = Texture(self.WIDTH / 2 - 300, self.HEIGHT / 2 - 190 - 50, pygame.image.load("textures/box2.png").convert_alpha())
        self.box_texture.scale(600, 300)

        self.player1_text = Text(320, 150, 30, "Waiting..." + self.pseudo, "fonts/passion_one.ttf")
        self.player1_texture = Texture.fromFile(700, 150 - 15, "textures/checkmark.png")
        self.player1_texture.scale(50, 50)

        self.player2_text = Text(320, 200, 30, "Waiting...", "fonts/passion_one.ttf")
        self.player2_texture = Texture.fromFile(700, 200 - 15, "textures/checkmark.png")
        self.player2_texture.scale(50, 50)

        """
        self.player3_text = Text(320, 250, 30, "Waiting...", "fonts/passion_one.ttf")
        self.player3_texture = Texture.fromFile(500, 250 - 15, "textures/checkmark.png")
        self.player3_texture.scale(50, 50)

        self.player4_text = Text(320, 300, 30, "Waiting...", "fonts/passion_one.ttf")
        self.player4_texture = Texture.fromFile(500, 300 - 15, "textures/checkmark.png")
        self.player4_texture.scale(50, 50)

        self.player5_text = Text(320, 350, 30, "Waiting...", "fonts/passion_one.ttf")
        self.player5_texture = Texture.fromFile(500, 350 - 15, "textures/checkmark.png")
        self.player5_texture.scale(50, 50)
        """

        self.status_text = Text(self.WIDTH / 2 - 180, 500, 40, "Waiting for {0} players...".format(5 - self.nb_players), "fonts/passion_one.ttf")

    def receive_from_server(self, x):
        message = self.socket.recv(1024)
        data = message.decode('utf-8')
        # process data & update ui
        data = data.replace('[', '')        # taking out the brackets
        data = data.replace(']', '')
        data = data.replace('\"', '')
        data = data.replace('b', '')
        data = data.split(",")
        if data[0] == self.pseudo:
            self.player1_text.setText("You - " + data[0])
        else:
            self.player1_text.setText(data[0])
        
        if data[2] == self.pseudo:
            self.player2_text.setText("You - " + data[2])
        else:
            self.player2_text.setText(data[2])
        
        self.nb_players = 2

        # self.listening = False

    # updates the screen
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ScreenManager.setActiveScreen(GameStates.MENU)
                    self.setRunning(False)
            
            self.back_button.input(event)
            self.ready_button.input(event)
            self.leave_button.input(event)

        if self.back_button.getState() == WidgetStates.PRESSED or self.leave_button.getState() == WidgetStates.PRESSED:
            self.back_button.setState(WidgetStates.REST)
            ScreenManager.setActiveScreen(GameStates.MENU)
            self.setRunning(False)
        
        self.players_text.setText("Players: {0}/{1}".format(self.nb_players, 5))

        if self.ready_button.getState() == WidgetStates.PRESSED:
            self.ready_button.setState(WidgetStates.REST)
            message = "1"
            self.socket.send(message.encode('ascii'))

        # lobby loop
        if self.listening == False:
            th = threading.Thread(target=self.receive_from_server, args=(self,))
            th.start()
            self.listening = True

        # if everybody is ready launch gamescreen
        if self.nb_players >= 2:
            ScreenManager.setActiveScreen(GameStates.GAME)
            self.setRunning(False)

        # or launch game screen


    # renders the screen
    def render(self):
        #super().render()
        self.window.fill([0, 125, 0])

        self.back_button.render(self.window)
        self.ready_button.render(self.window)
        self.leave_button.render(self.window)
        self.players_text.render(self.window)
        self.box_texture.render(self.window)

        self.player1_text.render(self.window)
        if self.player1_text.getText() != "Waiting...":
            self.player1_texture.render(self.window)

        self.player2_text.render(self.window)
        if self.player2_text.getText() != "Waiting...":
            self.player2_texture.render(self.window)

        """
        self.player3_text.render(self.window)
        if self.player3_text.getText() != "Waiting...":
            self.player3_texture.render(self.window)

        self.player4_text.render(self.window)
        if self.player4_text.getText() != "Waiting...":
            self.player4_texture.render(self.window)

        self.player5_text.render(self.window)
        if self.player5_text.getText() != "Waiting...":
            self.player5_texture.render(self.window)
        """

        self.status_text.render(self.window)


