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
    for s in config.squares:
        pygame.draw.rect(disp, config.sqr_color(
            config.square_colors[s]), (config.square_positions[s][0], config.square_positions[s][1], 100, 100))


# Start Game
pygame.init()
pygame.font.init()


DISPLAY = pygame.display.set_mode((config.board_size, config.board_size))

piece_list, white_piece_list, black_piece_list = pieces.initialize_pieces(
    DISPLAY)


while True:
    DISPLAY.fill(config.background_color)
    draw_board(DISPLAY)

    for piece in piece_list:
        piece.render()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
