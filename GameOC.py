from BoardOC import Player
from ValidErrors import Validator as valid, BoardError
from random import random
class Game:
    def __init__(self, board):
        self._board = board
        #self._players = [Player["X"], Player["O"]]
        self._currentPlayer = 0

    def switchPlayer(self):
        self._currentPlayer += 1
        self._currentPlayer = self._currentPlayer % 2

    # def getCurrentPlayer(self):
    #     return self._players[self._currentPlayer]

    def uiAddMove(self):
        row = input("Give Row: ")
        column = input("Give Column: ")
        sign = input("Give sign: ")
        try:
            valid.validate_input(row,column, sign)
            try:
                self._board.addMove(row, column, sign)
                return sign
            except BoardError as be:
                print(str(be))
        except ValueError as ve:
            print (str(ve))
    # def uiComputerMove(self):
    #     self._board.computerMove()

    def startGame(self):
        GameOver = False
        print (self._board.showBoard())
        restore = input ("Do you want to restore your last game? (yes/no): ")
        if restore == "yes":
            self._board.restoreSavedGame()
        print(self._board.showBoard())
        while not GameOver:
            if self._board.checkChaosWin():
                print("Game Over! Chaos Won! Board FULL!")
                break
            if self._currentPlayer == 0:
                sign = self.uiAddMove()
                print(self._board.showBoard())
                GameOver = self._board.checkWinOrder(sign)
                if GameOver == True:
                    print(self._board.showBoard())
                    print("Player Wins!!")
                else:
                    self.switchPlayer()
            elif self._currentPlayer == 1:
                print("Computer Moves!")
                sign = self._board.computerMove()
                print(self._board.showBoard())
                GameOver = self._board.checkWinOrder(sign)
                saveFile = input ("Do you want to save the game?(yes/no): ")
                if saveFile == "yes":
                    self._board.saveGameToFile()
                if GameOver == True:
                    print(self._board.showBoard())
                    print("Computer Wins!!")
                else:
                    self.switchPlayer()
