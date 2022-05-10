from Board import Board as B
from Brain import Brain as Br
import pygame as py
from UI import UI


read = input("Enter the sudoku board:")

board = B(read)
game = UI()
b = Br(game)

game.drawBoard(board.board)

sudoku = board.board
peers = board.peers
unit = board.all

while True:
    sudoku = b.solve(sudoku, peers, unit)
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
    py.display.update()

