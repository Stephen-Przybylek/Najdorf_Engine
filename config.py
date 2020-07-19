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

square_id = {
    1: 'A1',
    2: 'A2',
    3: 'A3',
    4: 'A4',
    5: 'A5',
    6: 'A6',
    7: 'A7',
    8: 'A8',
    9: 'B1',
    10: 'B2',
    11: 'B3',
    12: 'B4',
    13: 'B5',
    14: 'B6',
    15: 'B7',
    16: 'B8',
    17: 'C1',
    18: 'C2',
    19: 'C3',
    20: 'C4',
    21: 'C5',
    22: 'C6',
    23: 'C7',
    24: 'C8',
    25: 'D1',
    26: 'D2',
    27: 'D3',
    28: 'D4',
    29: 'D5',
    30: 'D6',
    31: 'D7',
    32: 'D8',
    33: 'E1',
    34: 'E2',
    35: 'E3',
    36: 'E4',
    37: 'E5',
    38: 'E6',
    39: 'E7',
    40: 'E8',
    41: 'F1',
    42: 'F2',
    43: 'F3',
    44: 'F4',
    45: 'F5',
    46: 'F6',
    47: 'F7',
    48: 'F8',
    49: 'G1',
    50: 'G2',
    51: 'G3',
    52: 'G4',
    53: 'G5',
    54: 'G6',
    55: 'G7',
    56: 'G8',
    57: 'H1',
    58: 'H2',
    59: 'H3',
    60: 'H4',
    61: 'H5',
    62: 'H6',
    63: 'H7',
    64: 'H8'}

square_id_reverse = {
    'A1': 1,
    'A2': 2,
    'A3': 3,
    'A4': 4,
    'A5': 5,
    'A6': 6,
    'A7': 7,
    'A8': 8,
    'B1': 9,
    'B2': 10,
    'B3': 11,
    'B4': 12,
    'B5': 13,
    'B6': 14,
    'B7': 15,
    'B8': 16,
    'C1': 17,
    'C2': 18,
    'C3': 19,
    'C4': 20,
    'C5': 21,
    'C6': 22,
    'C7': 23,
    'C8': 24,
    'D1': 25,
    'D2': 26,
    'D3': 27,
    'D4': 28,
    'D5': 29,
    'D6': 30,
    'D7': 31,
    'D8': 32,
    'E1': 33,
    'E2': 34,
    'E3': 35,
    'E4': 36,
    'E5': 37,
    'E6': 38,
    'E7': 39,
    'E8': 40,
    'F1': 41,
    'F2': 42,
    'F3': 43,
    'F4': 44,
    'F5': 45,
    'F6': 46,
    'F7': 47,
    'F8': 48,
    'G1': 49,
    'G2': 50,
    'G3': 51,
    'G4': 52,
    'G5': 53,
    'G6': 54,
    'G7': 55,
    'G8': 56,
    'H1': 57,
    'H2': 58,
    'H3': 59,
    'H4': 60,
    'H5': 61,
    'H6': 62,
    'H7': 63,
    'H8': 64, }


def sqr_color(pcolor):
    if pcolor == 'WHITE':
        return white_square_color
    if pcolor == 'BLACK':
        return black_square_color
