from puzzle import Puzzle
from aStar import AStar
from solver import PuzzleSolver

def testPuzzle():

    # Both inputs follow same pattern
    # 1: Declare the puzzle
    # 2: Declare a solver looking at the declared puzzle
    # 3: Run solver
    # 4: Print the solver's stored solution
    
    puzzle4x4_1 = Puzzle([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 11], [13, 14, 15, 12]])

    solver1 = PuzzleSolver(AStar(puzzle4x4_1))
    solver1.run()
    solver1.printSolution()

    puzzle4x4_2 = Puzzle([[1, 3, 6, 4], [5, 2, 0, 8], [10, 9, 7, 11], [14, 15, 13, 12]])

    solver2 = PuzzleSolver(AStar(puzzle4x4_2))
    solver2.run()
    solver2.printSolution()


if __name__ == '__main__' :
    testPuzzle()