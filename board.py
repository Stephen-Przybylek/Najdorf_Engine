import sys
import os
import pieces
import pygame
import config
from pygame.locals import *

if not pygame.font:
    print("Warning, fonts disabled")
if not pygame.mixer:
    print("Warning, sound disabled")


# Functions

''' Draw the board squares on the screen '''


def draw_board(disp):
    for i in range(1, 9):
        for x in range(1, 9):
            # alternate sequence on each row
            if (i + x) % 2 == 0:
                pygame.draw.rect(disp, (255, 0, 0),
                                 (x*config.square_size, i*config.square_size, config.square_size, config.square_size))
            else:
                pygame.draw.rect(disp, (0, 0, 255),
                                 (x*config.square_size, i*config.square_size, config.square_size, config.square_size))


# Start Game
pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 30)

DISPLAY = pygame.display.set_mode((config.board_size, config.board_size))

piece_list, white_piece_list, black_piece_list = pieces.initialize_pieces(
    DISPLAY)


while True:
    DISPLAY.fill((0, 255, 0))
    draw_board(DISPLAY)

    for piece in piece_list:
        piece.render(font)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
