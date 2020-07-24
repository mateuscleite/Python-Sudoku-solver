class Solver:

    def __init__(self, grid):
        self.blankCellCounter = 0
        self.solution = [ [ 0 for i in range(9) ] for j in range(9) ]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.solution[i][j] = grid[i][j]
                if(grid[i][j] == 0):
                    self.blankCellCounter += 1

    #if value is valid in a cell of a given row return true, else return false
    def checkRow(self, workingTable, value, row):
        for i in range(9):
            if(value == workingTable[row][i]):
                return False
        return True

    #if value is valid in a cell of a given column return true, else return false
    def checkColumn(self, workingTable, value, column):
        for i in range(9):
            if(value == workingTable[i][column]):
                return False
        return True

    #if value is valid in a cell of a given subgrid (obtained from the row and column) return true, else return false
    def checkSubGrid(self, workingTable, value, row, column):
        xMultiplier = int(column/3)
        yMultiplier = int(row/3)
        for i in range(3):
            for j in range(3):
                if(value == workingTable[yMultiplier*3 + i][xMultiplier*3 + j]):
                    return False
        return True

    #return the coordinates of the first blank cell; returns invalid coordinates if there are none
    def findBlankCell(self, workingTable):
        for i in range(9):
            for j in range(9):
                if(workingTable[i][j] == 0):
                    return i,j
        return -1, -1

    #calls the method that solves a sudoku puzzle and prints the solution; if there is no solution, a message is displayed
    def solver(self, grid):
        workingTable = grid
        if(self.completeTable(workingTable)):
            self.solution = workingTable
            self.printSolution()
        else:
            print("No solution found")

    #this method uses backtracking to try and obtain the solution of a sudoku puzzle
    def completeTable(self, workingTable):
        row, column = self.findBlankCell(workingTable)
        if(row == -1):                                      #didn't find a blank cell
            return True
        else:      
            for possibleValue in range(1, 10):
                if(self.checkRow(workingTable, possibleValue, row) and self.checkColumn(workingTable, possibleValue, column) and self.checkSubGrid(workingTable, possibleValue, row, column)):
                    workingTable[row][column] = possibleValue
                    if(self.completeTable(workingTable)):       
                        return True                             #the value used is working
                    workingTable[row][column] = 0               #the value didn't work, reset the cell and try the next value
            return False                                        #guarantees backtracking (no value worked in this cell, so go back to the last cell analyzed and try another value)

    def printSolution(self):
        print("Solved Sudoku game")
        for i in range(9):
            for j in range(9):
                print(self.solution[i][j]," ", end = "", flush = True)
            print("\n")