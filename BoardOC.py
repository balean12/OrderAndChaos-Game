import random
from texttable import Texttable
from ValidErrors import Validator as valid, BoardError, SaveError

class Player:
    def __init__(self, playerSign):
        self._playerSign = playerSign
    def getPlayer(self):
        return self._playerSign




class Board:
    def __init__(self):
        self._board = [["*" for column in range(0,6)] for rows in range(0,6)]
        self._rows = 6
        self._columns = 6

    def addMove(self, row,column,sign):
        if self._board[int(row)][int(column)] == "*":
            self._board[int(row)][int(column)] = sign
        else:
            raise BoardError("No a free space!")
    def checkChaosWin(self): #REFA:))
        for row in range(0,6):
            for col in range(0,6):
                if self._board[row][col] == "*":
                    return False
        return True
    def checkWinOrder(self, sign):
        return self.checkOrderWinDiagonalPos(sign) or self.checkOrderWinHorizontal(sign) or self.checkOrderWinVertical(sign) or self.checkOrderWinDiagonalNeg(sign)

    def checkOrderWinHorizontal(self, sign):
        for row in range(0, self._rows):
            for column in range(0, self._columns-4):
                if self._board[row][column] == self._board[row][column+1] == self._board[row][column+2] \
                        == self._board[row][column + 3] == self._board[row][column+4] == sign:
                    return True
        return False

    def checkOrderWinVertical(self,sign):
        for row in range(0, self._rows-4):
            for column in range(0, self._columns):
                if self._board[row][column] == self._board[row+1][column] == self._board[row+2][column] \
                        == self._board[row+3][column] == self._board[row+4][column] == sign:
                    return True
        return False

    def checkOrderWinDiagonalPos(self, sign):
        for row in range(self._rows - 2, self._rows):
            for column in range(0, self._columns-4):
                if self._board[row][column] == self._board[row - 1][column + 1] == self._board[row - 2][column +2] \
                        == self._board[row - 3][column+3] == self._board[row - 4][column+4] == sign:
                    return True
        return False

    def checkOrderWinDiagonalNeg(self, sign):
        for row in range (0, self._rows-4):
            for column in range(0, self._columns-4):
                if self._board[row][column] == self._board[row + 1][column + 1] == self._board[row + 2][column + 2] \
                        == self._board[row + 3][column + 3] == self._board[row + 4][column + 4] == sign:
                    return True
        return False
    def computerMove(self):
        row = random.randint(0,5)
        col = random.randint(0,5)
        list = ['X', 'O']
        sign = random.choice(list)
        while self._board[row][col] != "*":
            row = random.randint(0, 5)
            col = random.randint(0, 5)
        self._board[row][col] = sign
        return sign

    def showBoard(self):
        t = Texttable()
        for i in range(0,6):
            row = self._board[i][:]
            t.add_row(row)
        return t.draw()
    def getBoard(self):
        return self._board
    def setBoard(self, row, col, sign):
        self._board[row][col] = sign

    def saveGameToFile(self):
        try:
            f = open('savedGame.txt', 'w')
            for i in range(6):
                row = ""
                for j in range(6):
                    row = row + str(self.getBoard()[i][j]) + " "
                f.write(row + "\n")
            f.close()
        except IOError:
            raise SaveError("Game could not be saved")

    def restoreSavedGame(self):
        try:
            f = open('savedGame.txt', 'r')
            line = f.readline().strip()
            i = 0
            while line!="":
                line = line.split(" ")
                for j in range(6):
                    self.setBoard(i,j,line[j])
                i+=1
                line = f.readline().strip()
            f.close()
        except IOError:
            raise SaveError("Game could not be restored!")

