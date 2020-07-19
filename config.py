# Variables
board_size = 1000

squares = ('A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
           'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8',
           'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8',
           'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8',
           'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8',
           'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
           'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8',
           'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8')

# Available Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 255, 255)

# Derived Variables
white_square_color = BLUE
black_square_color = RED

background_color = TEAL

square_size = board_size/10

central_offset = square_size/4

square_positions = {
    'A1': (1*square_size, 8*square_size),
    'A2': (1*square_size, 7*square_size),
    'A3': (1*square_size, 6*square_size),
    'A4': (1*square_size, 5*square_size),
    'A5': (1*square_size, 4*square_size),
    'A6': (1*square_size, 3*square_size),
    'A7': (1*square_size, 2*square_size),
    'A8': (1*square_size, 1*square_size),
    'B1': (2*square_size, 8*square_size),
    'B2': (2*square_size, 7*square_size),
    'B3': (2*square_size, 6*square_size),
    'B4': (2*square_size, 5*square_size),
    'B5': (2*square_size, 4*square_size),
    'B6': (2*square_size, 3*square_size),
    'B7': (2*square_size, 2*square_size),
    'B8': (2*square_size, 1*square_size),
    'C1': (3*square_size, 8*square_size),
    'C2': (3*square_size, 7*square_size),
    'C3': (3*square_size, 6*square_size),
    'C4': (3*square_size, 5*square_size),
    'C5': (3*square_size, 4*square_size),
    'C6': (3*square_size, 3*square_size),
    'C7': (3*square_size, 2*square_size),
    'C8': (3*square_size, 1*square_size),
    'D1': (4*square_size, 8*square_size),
    'D2': (4*square_size, 7*square_size),
    'D3': (4*square_size, 6*square_size),
    'D4': (4*square_size, 5*square_size),
    'D5': (4*square_size, 4*square_size),
    'D6': (4*square_size, 3*square_size),
    'D7': (4*square_size, 2*square_size),
    'D8': (4*square_size, 1*square_size),
    'E1': (5*square_size, 8*square_size),
    'E2': (5*square_size, 7*square_size),
    'E3': (5*square_size, 6*square_size),
    'E4': (5*square_size, 5*square_size),
    'E5': (5*square_size, 4*square_size),
    'E6': (5*square_size, 3*square_size),
    'E7': (5*square_size, 2*square_size),
    'E8': (5*square_size, 1*square_size),
    'F1': (6*square_size, 8*square_size),
    'F2': (6*square_size, 7*square_size),
    'F3': (6*square_size, 6*square_size),
    'F4': (6*square_size, 5*square_size),
    'F5': (6*square_size, 4*square_size),
    'F6': (6*square_size, 3*square_size),
    'F7': (6*square_size, 2*square_size),
    'F8': (6*square_size, 1*square_size),
    'G1': (7*square_size, 8*square_size),
    'G2': (7*square_size, 7*square_size),
    'G3': (7*square_size, 6*square_size),
    'G4': (7*square_size, 5*square_size),
    'G5': (7*square_size, 4*square_size),
    'G6': (7*square_size, 3*square_size),
    'G7': (7*square_size, 2*square_size),
    'G8': (7*square_size, 1*square_size),
    'H1': (8*square_size, 8*square_size),
    'H2': (8*square_size, 7*square_size),
    'H3': (8*square_size, 6*square_size),
    'H4': (8*square_size, 5*square_size),
    'H5': (8*square_size, 4*square_size),
    'H6': (8*square_size, 3*square_size),
    'H7': (8*square_size, 2*square_size),
    'H8': (8*square_size, 1*square_size)
}

square_colors = {
    'A1': 'BLACK',
    'A2': 'WHITE',
    'A3': 'BLACK',
    'A4': 'WHITE',
    'A5': 'BLACK',
    'A6': 'WHITE',
    'A7': 'BLACK',
    'A8': 'WHITE',
    'B1': 'WHITE',
    'B2': 'BLACK',
    'B3': 'WHITE',
    'B4': 'BLACK',
    'B5': 'WHITE',
    'B6': 'BLACK',
    'B7': 'WHITE',
    'B8': 'BLACK',
    'C1': 'BLACK',
    'C2': 'WHITE',
    'C3': 'BLACK',
    'C4': 'WHITE',
    'C5': 'BLACK',
    'C6': 'WHITE',
    'C7': 'BLACK',
    'C8': 'WHITE',
    'D1': 'WHITE',
    'D2': 'BLACK',
    'D3': 'WHITE',
    'D4': 'BLACK',
    'D5': 'WHITE',
    'D6': 'BLACK',
    'D7': 'WHITE',
    'D8': 'BLACK',
    'E1': 'BLACK',
    'E2': 'WHITE',
    'E3': 'BLACK',
    'E4': 'WHITE',
    'E5': 'BLACK',
    'E6': 'WHITE',
    'E7': 'BLACK',
    'E8': 'WHITE',
    'F1': 'WHITE',
    'F2': 'BLACK',
    'F3': 'WHITE',
    'F4': 'BLACK',
    'F5': 'WHITE',
    'F6': 'BLACK',
    'F7': 'WHITE',
    'F8': 'BLACK',
    'G1': 'BLACK',
    'G2': 'WHITE',
    'G3': 'BLACK',
    'G4': 'WHITE',
    'G5': 'BLACK',
    'G6': 'WHITE',
    'G7': 'BLACK',
    'G8': 'WHITE',
    'H1': 'WHITE',
    'H2': 'BLACK',
    'H3': 'WHITE',
    'H4': 'BLACK',
    'H5': 'WHITE',
    'H6': 'BLACK',
    'H7': 'WHITE',
    'H8': 'BLACK'}


def sqr_color(pcolor):
    if pcolor == 'WHITE':
        return white_square_color
    if pcolor == 'BLACK':
        return black_square_color
