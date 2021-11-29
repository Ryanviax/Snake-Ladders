from app.gameobject import GameObject
from rendering.texture import Texture

import pygame

class Pawn(GameObject):
    
    def __init__(self, pseudo, color):
        super().__init__(0, 0, 16, 16)
        self.pseudo = pseudo
        self.color = color
        self.board_position = (0, 0)


    def update(self):
        pass

    def render(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), 16)

    def move(self, new_board_position, board_dimensions):
        self.board_position = new_board_position
        self.x = 45 * new_board_position[0] + 42 + board_dimensions[0]                          # size of tile * board pos + border offset + board_x
        self.y = 45 * new_board_position[1] - 42 + board_dimensions[1] + board_dimensions[3]    # tile size * board pos - border_offset + 

class Board(GameObject):

    # 10 x 10 board 100 cell
    # each cell is 45x45 px
    # the first cell's center is at (42, 42)

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.pawns = list()

        self.texture = Texture.fromFile(self.x, self.y, "textures/board.png")

        # Constants
        self.pawn_colors = [(192, 57, 43), (142, 68, 173), (52, 152, 219), (22, 160, 133), (241, 196, 15), ] # red - purple - blue - green - yellow
        self.ladders = [(1, 38), (4, 14), (8, 30), (21, 42), (28, 76), (50, 67), (71, 92), (80, 99)], 
        self.snakes = [(32, 10), (36, 6), (48, 26), (62, 18), (88, 24), (95, 56), (97, 78)]

    def update(self):
        pass

    def render(self, window):
        self.texture.render(window)
        for pawn in self.pawns:
            pawn.render(window)

    def addPawn(self, pseudo):
        self.pawns.append(Pawn(pseudo, self.pawn_colors[len(self.pawns) - 1]))
        for pawn in self.pawns:
            if pawn.pseudo == pseudo:
                pawn.move((0, 0), (self.x, self.y, self.width, self.height))

    def movePawn(self, player_pseudo, board_position):        
        new_position = board_position
        for snake in self.snakes:
            if snake[1] == board_position:      # if the board_position matches a snake
                new_position = snake[0]         # then we move the pawn down the snake

        for ladder in self.snakes:
            if ladder[0] == board_position:     # if the board_position matches a ladder
                new_position = ladder[1]        # then we move the pawn up the ladder 

        # moving the pawn
        for pawn in self.pawns:
            if pawn.player_pseudo == player_pseudo:
                pawn.move(new_position, (self.x, self.y, self.width, self.height))