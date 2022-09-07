import pygame
from checkers.constants import *
from checkers.board import Board
from checkers.game import Game
from minimax.algorithm import *

FPS = 60


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


# Event Loop
def main():
    run = True
    # How to make constant speed
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())
            run = False

        if game.turn == WHITE:
            value, new_board = minimax_with_pruning(game.get_board(), 3, float('-inf'), float('inf'), True, game)
            value2, old_board = minimax(game.get_board(), 3, True, game)
            print(str(value) + " " + str(value2))
            game.ai_move(new_board)
            # print(str(value) + " " + str(value2))

        if game.winner() is not None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Code for when clicked
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()
