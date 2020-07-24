class Table:
    #obtains the sudoku puzzle from a text file
    def __init__(self):
        self.grid = [ [ 0 for i in range(9) ] for j in range(9) ]
        gameTableFile = open("gameData.txt", "r")
        for i in range(9):
            line = gameTableFile.readline()
            line = line.rstrip('\n')
            line = line.strip()
            self.grid[i] = line.split(" ")
            for j in range(9):
                self.grid[i][j] = int(self.grid[i][j])

        gameTableFile.close()
    
    def printTable(self):
        for i in range(9):
            for j in range(9):
                print(self.grid[i][j]," ", end = "", flush = True)
            print("\n")


        