import pygame
import random
import time
import Cube3


class Seen(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(None, 64)
        self.display_width = 1000
        self.display_height = 600
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Cubing')
        pygame.display.update()
        self.crashed = False
        self.square_size = 50
        self.spacing = 5

    def block_display(self,x,y,colors):
        red = (255, 0, 0)  # F 0
        orange = (255, 128, 0)  # B 1
        white = (255, 255, 255)  # R 2
        yellow = (255, 255, 0)  # L 3
        blue = (0, 0, 255)  # U 4
        green = (0, 128, 0)  # D 5
        color_trans = {0:red,1:orange,2:white,3:yellow,4:blue,5:green}
        color = 0
        for i in range(3*len(colors)):
            if i % 3 == 0 and i != 0:
                color += 1
            pygame.draw.rect(self.gameDisplay, color_trans[colors[color]],
                             (x, y, self.square_size, self.square_size))
            pygame.draw.rect(self.gameDisplay, color_trans[colors[color]],
                             (x, y + self.square_size + self.spacing, self.square_size, self.square_size))
            pygame.draw.rect(self.gameDisplay, color_trans[colors[color]],
                             (x, y + 2 * (self.square_size + self.spacing), self.square_size,
                              self.square_size))
            x += self.square_size + self.spacing

    def block_display_dict(self,x,y,faces,cube):
        start_x = x
        red = (255, 0, 0)  # F 0
        orange = (255, 128, 0)  # B 1
        white = (255, 255, 255)  # R 2
        yellow = (255, 255, 0)  # L 3
        blue = (0, 0, 255)  # U 4
        green = (0, 128, 0)  # D 5
        color_trans = {0: red, 1: orange, 2: white, 3: yellow, 4: blue, 5: green}
        for face in faces:
            counter = 0
            for i in range(9):
                if i%3 == 0 and i != 0:
                    counter += 1
                    x = start_x
                pygame.draw.rect(self.gameDisplay, color_trans[cube[face][i]],
                                 (x, y + counter * (self.square_size + self.spacing), self.square_size, self.square_size))
                x += self.square_size + self.spacing

            start_x = x

    def color_display(self,cube=False):
        if not cube:
            colors_list = [2,4,3,5]
            self.block_display(337,55,[1])
            self.block_display(172,220,colors_list)
            self.block_display(337,385,[0])
            return -1
        mid = ["L","U","R","D"]
        self.block_display_dict(337, 55, ["B"], cube)
        self.block_display_dict(172, 220, mid, cube)
        self.block_display_dict(337, 385, ["F"], cube)

    def functionApp(self):
        if __name__ == '__main__':
            cube = Cube3.Rubik()
            self.color_display(cube.faces)
            pygame.display.update()
            print("Input move List")
            moves = "D L2 U' B2 U B2 U R' B2 R2 D2 R D' L' D' L' R' F' B2 D2 R2 D2 U L2 B2"
            #moves = "U D' D D' D' D D' L"
            moves = moves.upper()
            moves = list(moves.split(" "))
            new_moves = []
            for move in moves:
                if "2" in move:
                    new_moves.append(move[0])
                    new_moves.append(move[0])
                else:
                    new_moves.append(move)
            print(new_moves,len(new_moves))
            counter = 0
            while not self.crashed:
                if counter == 0:
                    for move in new_moves:
                        print(move)
                        cube.faces = Cube3.moves(cube.faces, move)
                        event = pygame.event.get()
                        """loop = True
                        while loop:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        loop = False"""
                        self.color_display(cube.faces)
                        pygame.display.update()
                        """
                        if event.type == pygame.QUIT:
                            self.crashed = True"""
                    counter += 1
                event = pygame.event.get()
                try:
                    if event.type == pygame.QUIT:
                        self.crashed = True
                except AttributeError:
                    pass

a = Seen()
a.functionApp()

