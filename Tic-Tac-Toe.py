from ast import Return
from hashlib import new
from operator import truediv
from re import T
from tabnanny import check
from tkinter import Grid


class GridObject:
    def __init__(self):
        self.value = None

    def SetValue(self, value):
        self.value = value

    def GetValue(self):
        return self.value

class Grid:
    def __init__(self):
        self.grid = self.CreateGrid()

    def CreateGrid(self):
        mainArray = []
        for i in range(3):
            newArray = []
            for j in range(3):
                newArray.append(GridObject())
            mainArray.append(newArray)
        return mainArray

    def GetGridObjectValue(self, x, y):
        return self.grid[y][x].GetValue()

    def SetGridObjectValue(self, x, y, value):
        self.grid[y][x].SetValue(value)

    def CheckLine(self, x, y, currentValue):
        if x == 0:
            if currentValue == self.GetGridObjectValue(x + 1, y) and currentValue == self.GetGridObjectValue(x + 2, y):
                return True
            if y == 0 and currentValue == self.GetGridObjectValue(x + 1, y + 1) and currentValue == self.GetGridObjectValue(x + 2, y + 2):
                return True
        if x == 1:
            if currentValue == self.GetGridObjectValue(x - 1, y) and currentValue == self.GetGridObjectValue(x + 1, y):
                return True
        if x == 2:
            if currentValue == self.GetGridObjectValue(x - 1, y) and currentValue == self.GetGridObjectValue(x - 2, y):
                return True
            if y == 0 and self.GetGridObjectValue(x - 1, y + 1) and currentValue == self.GetGridObjectValue(x - 2, y + 2):
                return True
        if y == 0:
            if currentValue == self.GetGridObjectValue(x, y + 1) and currentValue == self.GetGridObjectValue(x, y + 2):
                return True
        if y == 1:
            if currentValue == self.GetGridObjectValue(x, y - 1) and currentValue == self.GetGridObjectValue(x, y + 1):
                return True
        if y == 2:
            if currentValue == self.GetGridObjectValue(x, y - 1) and currentValue == self.GetGridObjectValue(x, y - 2):
                return True
        return False

    def ReturnValuesAsString(self):
        string = "-------\n"
        for array in self.grid:
            for gridObject in array:
                if gridObject.GetValue() != None:
                    string += "|" + gridObject.GetValue()
                else:
                    string += "| " 
            string += "|\n-------\n"
        return string


class Player():
    def __init__(self, value, name):
        self.value = value
        self.name = name

class GameManager():
    def __init__(self):
        self.grid = Grid()
        self.player1 = Player("X", "Player 1")
        self.player2 = Player("O", "Player 2")
        self.currentPlayer = self.player1

    def CheckIfEmpty(self, x, y, value):
        if self.grid.GetGridObjectValue(x, y) == None:
            return True

    def AddValue(self, x, y, value):
        self.grid.SetGridObjectValue(x, y, value)
        if self.grid.CheckLine(x, y, value):
            self.Win()

    def Win(self):
        return self.currentPlayer.name + " wins!!!"

    def ChangeTurn(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    def Turn(self, coordX, coordY):
        if self.CheckIfEmpty(coordX, coordY, self.currentPlayer.value):
            self.AddValue(coordX, coordY, self.currentPlayer.value)
        else:
            pass #Casilla no vacia
        if self.grid.CheckLine():
            return self.Win()

    def ShowGrid(self):
        return self.grid.ReturnValuesAsString()



gameManager = GameManager()
print(gameManager.ShowGrid())
coordX = int(input("Select the horizontal coordinate: "))
coordY = int(input("Select the vertical coordinate: "))
print(gameManager.Turn(coordX, coordY))