from table import Table 
from solver import Solver

game = Table()
game.printTable()

solution = Solver(game.grid)
solution.solver(game.grid)