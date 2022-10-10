class PuzzleSolver:

    def __init__(self, strategy):

        self.strategy = strategy

    def printPerformance(self):

        # The source code likely uses this to compare different strategies.
        # In this case, it prints out how many "expanded nodes" are in the search tree.
        # This can be used to determine which strategy is more effective by comparing the total nodes checked.
        print(f'{self.strategy} - Expanded nodes: {self.strategy.numNodes}')

    def printSolution(self):

        # Prints steps for solution
        print('Solution:')

        for s in self.strategy.solution:
            print(s)

    def run(self):

        # Checks to make sure puzzle is solvable, then runs the solver.
        if not self.strategy.start.isSolvable():

            raise RuntimeError('This puzzle is not solvable.')

        self.strategy.solvePuzzle()