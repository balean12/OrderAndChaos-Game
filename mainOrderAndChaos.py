from GameOC import Game
from ValidErrors import Validator, BoardError
from BoardOC import Board, Player

board = Board()
game = Game(board)
game.startGame()