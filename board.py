import sys
import os
import math
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


def detect_square(pos):
    closest = None
    cdist = config.board_size
    for key, value in config.square_positions.items():
        center = (value[0] + config.square_size/2,
                  value[1] + config.square_size/2)
        dist = math.sqrt(
            math.pow((center[0] - pos[0]), 2) + math.pow((center[1] - pos[1]), 2))
        if dist < cdist:
            cdist = dist
            closest = key
    return closest


def select_piece(square, pl):
    for p in pl:
        if p.square == square:
            return p
    return None


def move(piece, square):
    pass


# Start Game
pygame.init()
pygame.font.init()


DISPLAY = pygame.display.set_mode((config.board_size, config.board_size))

piece_list, white_piece_list, black_piece_list = pieces.initialize_pieces(
    DISPLAY)

move_list = []
while True:
    DISPLAY.fill(config.background_color)
    draw_board(DISPLAY)

    for piece in piece_list:
        piece.render()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            psquare = detect_square(pos)
            if select_piece(psquare, piece_list) is not None or len(move_list) == 1:
                move_list.append(psquare)
            if len(move_list) == 2:
                if move_list[1] in select_piece(move_list[0], piece_list).valid_moves(piece_list, white_piece_list, black_piece_list):
                    to_square_p = select_piece(move_list[1], piece_list)
                    if to_square_p is not None:
                        piece_list.remove(to_square_p)
                        if to_square_p.color == 'WHITE':
                            white_piece_list.remove(to_square_p)
                        if to_square_p.color == 'BLACK':
                            black_piece_list.remove(to_square_p)
                    select_piece(move_list[0], piece_list).move(move_list[1])
                move_list = []
    pygame.display.update()
