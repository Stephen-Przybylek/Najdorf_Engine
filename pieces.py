import pygame
import config


class Pawn:
    def __init__(self, disp, square, color):
        self.disp = disp
        self.square = square
        self.color = color
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self):
        if self.color == 'WHITE':
            box_clr = config.WHITE
            txt_clr = config.BLACK
        if self.color == 'BLACK':
            box_clr = config.BLACK
            txt_clr = config.WHITE
        pygame.draw.rect(self.disp, box_clr,
                         (config.square_positions[self.square][0] + config.central_offset, config.square_positions[self.square]
                          [1] + config.central_offset, config.square_size/2, config.square_size/2))
        textsurface = self.font.render('P', False, txt_clr)
        self.disp.blit(textsurface, (config.square_positions[self.square][0] + config.central_offset + 15, config.square_positions[self.square]
                                     [1] + config.central_offset))

    def move(self, square):

        self.square = square

    def valid_moves(self, pl, wpl, bpl, en_passant=False):
        occupied_by_white = [s.square for s in wpl]
        occupied_by_black = [s.square for s in bpl]
        occupied_by_any = occupied_by_white + occupied_by_black
        id = config.square_id_reverse[self.square]
        moves = []
        if self.color == 'WHITE':
            if id % 8 != 0:
                if config.square_id[id + 1] not in occupied_by_any:
                    moves.append((config.square_id[id + 1]))
                if id > 9:
                    if config.square_id[id - 7] not in occupied_by_white and config.square_id[id - 7] in occupied_by_black:
                        moves.append(config.square_id[id - 7])
                if id < 57:
                    if config.square_id[id + 9] not in occupied_by_white and config.square_id[id + 9] in occupied_by_black:
                        moves.append(config.square_id[id + 9])
            if id % 8 == 2:
                if config.square_id[id + 2] not in occupied_by_any and config.square_id[id + 1] not in occupied_by_any:
                    moves.append(config.square_id[id + 2])
            if (en_passant and id % 8 == 5) and id > 9:
                if config.square_id[id - 7] not in occupied_by_any:
                    moves.append(config.square_id[id - 7])
            if (en_passant and id % 8 == 5) and id < 57:
                if config.square_id[id + 9] not in occupied_by_any:
                    moves.append(config.square_id[id + 9])
        if self.color == 'BLACK':
            if id % 8 != 1:
                if config.square_id[id - 1] not in occupied_by_any:
                    moves.append(config.square_id[id - 1])
                if id > 9:
                    if config.square_id[id - 9] not in occupied_by_black and config.square_id[id - 9] in occupied_by_white:
                        moves.append(config.square_id[id - 9])
                if id < 57:
                    if config.square_id[id + 7] not in occupied_by_black and config.square_id[id + 7] in occupied_by_white:
                        moves.append(config.square_id[id + 7])
            if id % 8 == 7:
                if config.square_id[id - 2] not in occupied_by_any and config.square_id[id - 1] not in occupied_by_any:
                    moves.append(config.square_id[id - 2])
            if (en_passant and id % 8 == 4) and id > 9:
                if config.square_id[id - 9] not in occupied_by_any:
                    moves.append(config.square_id[id - 9])
            if (en_passant and id % 8 == 4) and id < 57:
                if config.square_id[id + 7] not in occupied_by_any:
                    moves.append(config.square_id[id + 7])

        return moves


class Rook:
    def __init__(self, disp, square, color):
        self.disp = disp
        self.square = square
        self.color = color
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self):
        if self.color == 'WHITE':
            box_clr = config.WHITE
            txt_clr = config.BLACK
        if self.color == 'BLACK':
            box_clr = config.BLACK
            txt_clr = config.WHITE
        pygame.draw.rect(self.disp, box_clr,
                         (config.square_positions[self.square][0] + config.central_offset, config.square_positions[self.square]
                          [1] + config.central_offset, config.square_size/2, config.square_size/2))
        textsurface = self.font.render('R', False, txt_clr)
        self.disp.blit(textsurface, (config.square_positions[self.square][0] + config.central_offset + 15, config.square_positions[self.square]
                                     [1] + config.central_offset))

    def move(self, square):
        self.square = square

    def valid_moves(self, pl, wpl, bpl, en_passant=False):
        occupied_by_white = [s.square for s in wpl]
        occupied_by_black = [s.square for s in bpl]
        occupied_by_any = occupied_by_white + occupied_by_black
        id = config.square_id_reverse[self.square]
        moves = []
        if self.color == 'WHITE':
            for i in range(1, 9):
                if (((id + i) % 8) == 1):
                    break
                if config.square_id[id + i] not in occupied_by_any:
                    moves.append(config.square_id[id + i])
                elif config.square_id[id + i] in occupied_by_black:
                    moves.append(config.square_id[id + i])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i) % 8) == 0):
                    break
                if config.square_id[id - i] not in occupied_by_any:
                    moves.append(config.square_id[id - i])
                elif config.square_id[id - i] in occupied_by_black:
                    moves.append(config.square_id[id - i])
                    break
                else:
                    break
            for i in range(1, 9):
                if ((id + 8*i) > 64):
                    break
                if config.square_id[id + i*8] not in occupied_by_any:
                    moves.append(config.square_id[id + i*8])
                elif config.square_id[id + i*8] in occupied_by_black:
                    moves.append(config.square_id[id + i*8])
                    break
                else:
                    break
            for i in range(1, 9):
                if ((id - i*8) < 1):
                    break
                if config.square_id[id - i*8] not in occupied_by_any:
                    moves.append(config.square_id[id - i*8])
                elif config.square_id[id - i*8] in occupied_by_black:
                    moves.append(config.square_id[id - i*8])
                    break
                else:
                    break
        if self.color == 'BLACK':
            for i in range(1, 9):
                if (((id + i) % 8) == 1):
                    break
                if config.square_id[id + i] not in occupied_by_any:
                    moves.append(config.square_id[id + i])
                elif config.square_id[id + i] in occupied_by_white:
                    moves.append(config.square_id[id + i])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i) % 8) == 0):
                    break
                if config.square_id[id - i] not in occupied_by_any:
                    moves.append(config.square_id[id - i])
                elif config.square_id[id - i] in occupied_by_white:
                    moves.append(config.square_id[id - i])
                    break
                else:
                    break
            for i in range(1, 9):
                if ((id + 8*i) > 64):
                    break
                if config.square_id[id + i*8] not in occupied_by_any:
                    moves.append(config.square_id[id + i*8])
                elif config.square_id[id + i*8] in occupied_by_white:
                    moves.append(config.square_id[id + i*8])
                    break
                else:
                    break
            for i in range(1, 9):
                if ((id - i*8) < 1):
                    break
                if config.square_id[id - i*8] not in occupied_by_any:
                    moves.append(config.square_id[id - i*8])
                elif config.square_id[id - i*8] in occupied_by_white:
                    moves.append(config.square_id[id - i*8])
                    break
                else:
                    break
        return moves


class Knight:
    def __init__(self, disp, square, color):
        self.disp = disp
        self.square = square
        self.color = color
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self):
        if self.color == 'WHITE':
            box_clr = config.WHITE
            txt_clr = config.BLACK
        if self.color == 'BLACK':
            box_clr = config.BLACK
            txt_clr = config.WHITE
        pygame.draw.rect(self.disp, box_clr,
                         (config.square_positions[self.square][0] + config.central_offset, config.square_positions[self.square]
                          [1] + config.central_offset, config.square_size/2, config.square_size/2))
        textsurface = self.font.render('N', False, txt_clr)
        self.disp.blit(textsurface, (config.square_positions[self.square][0] + config.central_offset + 15, config.square_positions[self.square]
                                     [1] + config.central_offset))

    def move(self, square):
        self.square = square

    def valid_moves(self, pl, wpl, bpl, en_passant=False):
        occupied_by_white = [s.square for s in wpl]
        occupied_by_black = [s.square for s in bpl]
        occupied_by_any = occupied_by_white + occupied_by_black
        id = config.square_id_reverse[self.square]
        moves = []
        if self.color == 'WHITE':
            if ((id > 16) and ((id % 8) != 1)) and config.square_id[id - 17] not in occupied_by_white:
                moves.append(config.square_id[id - 17])
            if ((id > 16) and ((id % 8) != 0)) and config.square_id[id - 15] not in occupied_by_white:
                moves.append(config.square_id[id - 15])
            if ((id > 8) and (((id % 8) != 2) and ((id % 8) != 1))) and config.square_id[id - 10] not in occupied_by_white:
                moves.append(config.square_id[id - 10])
            if ((id > 8) and (((id % 8) != 0) and ((id % 8) != 7))) and config.square_id[id - 6] not in occupied_by_white:
                moves.append(config.square_id[id - 6])
            if ((id < 57) and (((id % 8) != 1) and ((id % 8) != 2))) and config.square_id[id + 6] not in occupied_by_white:
                moves.append(config.square_id[id + 6])
            if ((id < 57) and (((id % 8) != 0) and ((id % 8) != 7))) and config.square_id[id + 10] not in occupied_by_white:
                moves.append(config.square_id[id + 10])
            if id < 49 and (id % 8) != 1 and config.square_id[id + 15] not in occupied_by_white:
                moves.append(config.square_id[id + 15])
            if ((id < 49) and ((id % 8) != 0)) and config.square_id[id + 17] not in occupied_by_white:
                moves.append(config.square_id[id + 17])
        if self.color == 'BLACK':
            if ((id > 16) and ((id % 8) != 1)) and config.square_id[id - 17] not in occupied_by_black:
                moves.append(config.square_id[id - 17])
            if ((id > 16) and ((id % 8) != 0)) and config.square_id[id - 15] not in occupied_by_black:
                moves.append(config.square_id[id - 15])
            if ((id > 8) and (((id % 8) != 2) and ((id % 8) != 1))) and config.square_id[id - 10] not in occupied_by_black:
                moves.append(config.square_id[id - 10])
            if ((id > 8) and (((id % 8) != 0) and ((id % 8) != 7))) and config.square_id[id - 6] not in occupied_by_black:
                moves.append(config.square_id[id - 6])
            if ((id < 57) and (((id % 8) != 1) and ((id % 8) != 2))) and config.square_id[id + 6] not in occupied_by_black:
                moves.append(config.square_id[id + 6])
            if ((id < 57) and (((id % 8) != 0) and ((id % 8) != 7))) and config.square_id[id + 10] not in occupied_by_black:
                moves.append(config.square_id[id + 10])
            if id < 49 and (id % 8) != 1 and config.square_id[id + 15] not in occupied_by_black:
                moves.append(config.square_id[id + 15])
            if ((id < 49) and ((id % 8) != 0)) and config.square_id[id + 17] not in occupied_by_black:
                moves.append(config.square_id[id + 17])
        return moves


class Bishop:
    def __init__(self, disp, square, color):
        self.disp = disp
        self.square = square
        self.color = color
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self):
        if self.color == 'WHITE':
            box_clr = config.WHITE
            txt_clr = config.BLACK
        if self.color == 'BLACK':
            box_clr = config.BLACK
            txt_clr = config.WHITE
        pygame.draw.rect(self.disp, box_clr,
                         (config.square_positions[self.square][0] + config.central_offset, config.square_positions[self.square]
                          [1] + config.central_offset, config.square_size/2, config.square_size/2))
        textsurface = self.font.render('B', False, txt_clr)
        self.disp.blit(textsurface, (config.square_positions[self.square][0] + config.central_offset + 15, config.square_positions[self.square]
                                     [1] + config.central_offset))

    def move(self, square):
        self.square = square

    def valid_moves(self, pl, wpl, bpl, en_passant=False):
        occupied_by_white = [s.square for s in wpl]
        occupied_by_black = [s.square for s in bpl]
        occupied_by_any = occupied_by_white + occupied_by_black
        id = config.square_id_reverse[self.square]
        moves = []
        if self.color == 'WHITE':
            for i in range(1, 9):
                if (((id + i*9) > 64) or id % 8 == 0):
                    break
                if config.square_id[id + i*9] not in occupied_by_any:
                    moves.append(config.square_id[id + i*9])
                elif config.square_id[id + i*9] in occupied_by_black:
                    moves.append(config.square_id[id + i*9])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i*9) < 1) or id % 8 == 1):
                    break
                if config.square_id[id - i*9] not in occupied_by_any:
                    moves.append(config.square_id[id - i*9])
                elif config.square_id[id - i*9] in occupied_by_black:
                    moves.append(config.square_id[id - i*9])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id + i*7) > 64) or id % 8 == 1):
                    break
                if config.square_id[id + i*7] not in occupied_by_any:
                    moves.append(config.square_id[id + i*7])
                elif config.square_id[id + i*7] in occupied_by_black:
                    moves.append(config.square_id[id + i*7])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i*7) < 1) or id % 8 == 0):
                    break
                if config.square_id[id - i*7] not in occupied_by_any:
                    moves.append(config.square_id[id - i*7])
                elif config.square_id[id - i*7] in occupied_by_black:
                    moves.append(config.square_id[id - i*7])
                    break
                else:
                    break

        if self.color == 'BLACK':
            for i in range(1, 9):
                if (((id + i*9) > 64) or id % 8 == 0):
                    break
                if config.square_id[id + i*9] not in occupied_by_any:
                    moves.append(config.square_id[id + i*9])
                elif config.square_id[id + i*9] in occupied_by_white:
                    moves.append(config.square_id[id + i*9])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i*9) < 1) or id % 8 == 1):
                    break
                if config.square_id[id - i*9] not in occupied_by_any:
                    moves.append(config.square_id[id - i*9])
                elif config.square_id[id - i*9] in occupied_by_white:
                    moves.append(config.square_id[id - i*9])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id + i*7) > 64) or id % 8 == 1):
                    break
                if config.square_id[id + i*7] not in occupied_by_any:
                    moves.append(config.square_id[id + i*7])
                elif config.square_id[id + i*7] in occupied_by_white:
                    moves.append(config.square_id[id + i*7])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i*7) < 1) or id % 8 == 0):
                    break
                if config.square_id[id - i*7] not in occupied_by_any:
                    moves.append(config.square_id[id - i*7])
                elif config.square_id[id - i*7] in occupied_by_white:
                    moves.append(config.square_id[id - i*7])
                    break
                else:
                    break
        return moves


class Queen:
    def __init__(self, disp, square, color):
        self.disp = disp
        self.square = square
        self.color = color
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self):
        if self.color == 'WHITE':
            box_clr = config.WHITE
            txt_clr = config.BLACK
        if self.color == 'BLACK':
            box_clr = config.BLACK
            txt_clr = config.WHITE
        pygame.draw.rect(self.disp, box_clr,
                         (config.square_positions[self.square][0] + config.central_offset, config.square_positions[self.square]
                          [1] + config.central_offset, config.square_size/2, config.square_size/2))
        textsurface = self.font.render('Q', False, txt_clr)
        self.disp.blit(textsurface, (config.square_positions[self.square][0] + config.central_offset + 15, config.square_positions[self.square]
                                     [1] + config.central_offset))

    def move(self, square):
        self.square = square

    def valid_moves(self, pl, wpl, bpl, en_passant=False):
        occupied_by_white = [s.square for s in wpl]
        occupied_by_black = [s.square for s in bpl]
        occupied_by_any = occupied_by_white + occupied_by_black
        id = config.square_id_reverse[self.square]
        moves = []
        if self.color == 'WHITE':
            for i in range(1, 9):
                if (((id + i) % 8) == 1):
                    break
                if config.square_id[id + i] not in occupied_by_any:
                    moves.append(config.square_id[id + i])
                elif config.square_id[id + i] in occupied_by_black:
                    moves.append(config.square_id[id + i])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i) % 8) == 0):
                    break
                if config.square_id[id - i] not in occupied_by_any:
                    moves.append(config.square_id[id - i])
                elif config.square_id[id - i] in occupied_by_black:
                    moves.append(config.square_id[id - i])
                    break
                else:
                    break
            for i in range(1, 9):
                if ((id + 8*i) > 64):
                    break
                if config.square_id[id + i*8] not in occupied_by_any:
                    moves.append(config.square_id[id + i*8])
                elif config.square_id[id + i*8] in occupied_by_black:
                    moves.append(config.square_id[id + i*8])
                    break
                else:
                    break
            for i in range(1, 9):
                if ((id - i*8) < 1):
                    break
                if config.square_id[id - i*8] not in occupied_by_any:
                    moves.append(config.square_id[id - i*8])
                elif config.square_id[id - i*8] in occupied_by_black:
                    moves.append(config.square_id[id - i*8])
                    break
                else:
                    break
        if self.color == 'BLACK':
            for i in range(1, 9):
                if (((id + i) % 8) == 1):
                    break
                if config.square_id[id + i] not in occupied_by_any:
                    moves.append(config.square_id[id + i])
                elif config.square_id[id + i] in occupied_by_white:
                    moves.append(config.square_id[id + i])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i) % 8) == 0):
                    break
                if config.square_id[id - i] not in occupied_by_any:
                    moves.append(config.square_id[id - i])
                elif config.square_id[id - i] in occupied_by_white:
                    moves.append(config.square_id[id - i])
                    break
                else:
                    break
            for i in range(1, 9):
                if ((id + 8*i) > 64):
                    break
                if config.square_id[id + i*8] not in occupied_by_any:
                    moves.append(config.square_id[id + i*8])
                elif config.square_id[id + i*8] in occupied_by_white:
                    moves.append(config.square_id[id + i*8])
                    break
                else:
                    break
            for i in range(1, 9):
                if ((id - i*8) < 1):
                    break
                if config.square_id[id - i*8] not in occupied_by_any:
                    moves.append(config.square_id[id - i*8])
                elif config.square_id[id - i*8] in occupied_by_white:
                    moves.append(config.square_id[id - i*8])
                    break
                else:
                    break
        if self.color == 'WHITE':
            for i in range(1, 9):
                if (((id + i*9) > 64) or id % 8 == 0):
                    break
                if config.square_id[id + i*9] not in occupied_by_any:
                    moves.append(config.square_id[id + i*9])
                elif config.square_id[id + i*9] in occupied_by_black:
                    moves.append(config.square_id[id + i*9])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i*9) < 1) or id % 8 == 1):
                    break
                if config.square_id[id - i*9] not in occupied_by_any:
                    moves.append(config.square_id[id - i*9])
                elif config.square_id[id - i*9] in occupied_by_black:
                    moves.append(config.square_id[id - i*9])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id + i*7) > 64) or id % 8 == 1):
                    break
                if config.square_id[id + i*7] not in occupied_by_any:
                    moves.append(config.square_id[id + i*7])
                elif config.square_id[id + i*7] in occupied_by_black:
                    moves.append(config.square_id[id + i*7])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i*7) < 1) or id % 8 == 0):
                    break
                if config.square_id[id - i*7] not in occupied_by_any:
                    moves.append(config.square_id[id - i*7])
                elif config.square_id[id - i*7] in occupied_by_black:
                    moves.append(config.square_id[id - i*7])
                    break
                else:
                    break

        if self.color == 'BLACK':
            for i in range(1, 9):
                if (((id + i*9) > 64) or id % 8 == 0):
                    break
                if config.square_id[id + i*9] not in occupied_by_any:
                    moves.append(config.square_id[id + i*9])
                elif config.square_id[id + i*9] in occupied_by_white:
                    moves.append(config.square_id[id + i*9])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i*9) < 1) or id % 8 == 1):
                    break
                if config.square_id[id - i*9] not in occupied_by_any:
                    moves.append(config.square_id[id - i*9])
                elif config.square_id[id - i*9] in occupied_by_white:
                    moves.append(config.square_id[id - i*9])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id + i*7) > 64) or id % 8 == 1):
                    break
                if config.square_id[id + i*7] not in occupied_by_any:
                    moves.append(config.square_id[id + i*7])
                elif config.square_id[id + i*7] in occupied_by_white:
                    moves.append(config.square_id[id + i*7])
                    break
                else:
                    break
            for i in range(1, 9):
                if (((id - i*7) < 1) or id % 8 == 0):
                    break
                if config.square_id[id - i*7] not in occupied_by_any:
                    moves.append(config.square_id[id - i*7])
                elif config.square_id[id - i*7] in occupied_by_white:
                    moves.append(config.square_id[id - i*7])
                    break
                else:
                    break
        return moves


class King:
    def __init__(self, disp, square, color):
        self.disp = disp
        self.square = square
        self.color = color
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def render(self):
        if self.color == 'WHITE':
            box_clr = config.WHITE
            txt_clr = config.BLACK
        if self.color == 'BLACK':
            box_clr = config.BLACK
            txt_clr = config.WHITE
        pygame.draw.rect(self.disp, box_clr,
                         (config.square_positions[self.square][0] + config.central_offset, config.square_positions[self.square]
                          [1] + config.central_offset, config.square_size/2, config.square_size/2))
        textsurface = self.font.render('K', False, txt_clr)
        self.disp.blit(textsurface, (config.square_positions[self.square][0] + config.central_offset + 15, config.square_positions[self.square]
                                     [1] + config.central_offset))

    def move(self, square):
        self.square = square


def initialize_pieces(disp):
    wp1 = Pawn(disp, 'A2', 'WHITE')
    wp2 = Pawn(disp, 'B2', 'WHITE')
    wp3 = Pawn(disp, 'C2', 'WHITE')
    wp4 = Pawn(disp, 'D2', 'WHITE')
    wp5 = Pawn(disp, 'E2', 'WHITE')
    wp6 = Pawn(disp, 'F2', 'WHITE')
    wp7 = Pawn(disp, 'G2', 'WHITE')
    wp8 = Pawn(disp, 'H2', 'WHITE')
    wr1 = Rook(disp, 'A1', 'WHITE')
    wr2 = Rook(disp, 'H1', 'WHITE')
    wn1 = Knight(disp, 'B1', 'WHITE')
    wn2 = Knight(disp, 'G1', 'WHITE')
    wb1 = Bishop(disp, 'C1', 'WHITE')
    wb2 = Bishop(disp, 'F1', 'WHITE')
    wq = Queen(disp, 'D1', 'WHITE')
    wk = King(disp, 'E1', 'WHITE')

    wpl = [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8,
           wr1, wr2, wn1, wn2, wb1, wb2, wq, wk]

    bp1 = Pawn(disp, 'A7', 'BLACK')
    bp2 = Pawn(disp, 'B7', 'BLACK')
    bp3 = Pawn(disp, 'C7', 'BLACK')
    bp4 = Pawn(disp, 'D7', 'BLACK')
    bp5 = Pawn(disp, 'E7', 'BLACK')
    bp6 = Pawn(disp, 'F7', 'BLACK')
    bp7 = Pawn(disp, 'G7', 'BLACK')
    bp8 = Pawn(disp, 'H7', 'BLACK')
    br1 = Rook(disp, 'A8', 'BLACK')
    br2 = Rook(disp, 'H8', 'BLACK')
    bn1 = Knight(disp, 'B8', 'BLACK')
    bn2 = Knight(disp, 'G8', 'BLACK')
    bb1 = Bishop(disp, 'C8', 'BLACK')
    bb2 = Bishop(disp, 'F8', 'BLACK')
    bq = Queen(disp, 'D8', 'BLACK')
    bk = King(disp, 'E8', 'BLACK')

    bpl = [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8,
           br1, br2, bn1, bn2, bb1, bb2, bq, bk]

    pl = [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8,
          wr1, wr2, wn1, wn2, wb1, wb2, wq, wk, bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8,
          br1, br2, bn1, bn2, bb1, bb2, bq, bk]

    return pl, wpl, bpl
