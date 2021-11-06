"""Displaying main frame, engine running, knight moves"""
import time

import pygame as p
import KnightEngine
from KnightMoves import Knight
import sys

BOARD_WIDTH = BOARD_HEIGHT = 680

DIMENSION8 = 8
DIMENSION12 = 12
DIMENSION16 = 16

MAX_FPS = 15
IMAGES = {}


def loadImage(square_size):
    """
    Initialize a global directory of Knight Image
    This will be called exactly once in the main.
    """
    piece = 'bN'
    IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (square_size, square_size))


def main(dimension, posX, posY):
    """
    The main driver for our code.
    This will handle user input and updating the graphics.
    """

    p.init()
    screen = p.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    game_state = KnightEngine.GameState()

    loadImage(BOARD_HEIGHT // dimension)  # do this only once before while loop
    running = True

    currentX = 0
    currentY = 0
    board = [[]]
    listActions = Knight.getMovesUCS(posX, posY, dimension)

    if dimension == 16:
        board = game_state.board16
    elif dimension == 12:
        board = game_state.board12
    elif dimension == 8:
        board = game_state.board8
    exitBoolean = False
    while running:
        for e in p.event.get():

            if e.type == p.QUIT:
                p.quit()
                sys.exit()
            elif e.type == p.KEYDOWN:
                if exitBoolean == True:
                    p.quit()
                    sys.exit()
                actionsForTable(listActions, currentX, currentY, game_state, screen, clock, dimension)
                exitBoolean = True
        square_size = BOARD_HEIGHT // dimension

        drawGameState(screen, board, dimension, square_size)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, board, DIMENSION, square_size):
    """
    Responsible for all the graphics within current game state.
    """
    drawBoard(screen, DIMENSION, square_size)  # draw squares on the board
    drawPieces(screen, board, DIMENSION, square_size)  # draw pieces on top of those squares


def actionsForTable(listActions, currentX, currentY, game_state, screen, clock, dimension):
    board = [[]]
    square_size = 0

    if dimension == 8:
        board = game_state.board8
        square_size = BOARD_HEIGHT // DIMENSION8
    elif dimension == 12:
        board = game_state.board12
        square_size = BOARD_HEIGHT // DIMENSION12
    elif dimension == 16:
        board = game_state.board16
        square_size = BOARD_HEIGHT // DIMENSION16

    for action in listActions:
        move = KnightEngine.Move((currentX, currentY), (currentX + action[0], currentY + action[1]),
                                 board)
        currentX += action[0]
        currentY += action[1]
        game_state.makeMove(move, board)

        drawGameState(screen, board, dimension, square_size)

        clock.tick(MAX_FPS)
        p.display.flip()

        time.sleep(0.3)


def drawBoard(screen, DIMENSION, square_size):
    """
    Draw the squares on the board
    The top left square is always light.
    """
    global colors
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * square_size, row * square_size, square_size, square_size))


def drawPieces(screen, board, DIMENSION, square_size):
    """
    Draw the pieces on the board using the current game_state.board
    """
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * square_size, row * square_size, square_size, square_size))


if __name__ == "__main__":
    dimension = int(sys.argv[1])
    x = int(sys.argv[2])
    y = int(sys.argv[3])
    main(dimension, x, y)
