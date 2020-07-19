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
