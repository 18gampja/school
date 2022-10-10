from abc import ABC, abstractmethod

from puzzle import Puzzle

class Strategy(ABC):

    # I implemented this superclass in case I want to play around with different strategies later.
    # In the source code, this is used as a foundation for another breadth first search
    numNodes = 0
    solution = None

    @abstractmethod
    def solvePuzzle(self):

        raise NotImplemented

class AStar(Strategy):
    MANHATTAN_DISTANCE, MISPLACED = 'manhattanDist', 'misplacedTiles'
    CONSTANTS = [MANHATTAN_DISTANCE, MISPLACED]

    # Functions we can use to determine heuristic value
    heuristicFuncs = {
        MANHATTAN_DISTANCE : Puzzle.manhattanDistance.__name__,
        MISPLACED : Puzzle.misplaced.__name__
    }

    def __init__(self, initialPuzzle, heuristic = None):

        # Checks to determine a defined heuristic function. Otherwise, default to the manhattan distance function
        self.start = initialPuzzle
        self.heuristicFunc = self.heuristicFuncs[self.MANHATTAN_DISTANCE]

        if heuristic:

            if heuristic not in self.CONSTANTS:

                raise RuntimeError(f'Invalid Heuristic Function Name. Must be {self.CONSTANTS}')
            
            self.heuristicFunc = self.heuristicFunc[heuristic]

    def calcNewHeuristic(self, move, endNode):

        # Determines how good a heuristic is
        return getattr(move, self.heuristicFunc)() - getattr(endNode, self.heuristicFunc)()

    def __str__(self):
        return 'A*'

    def solvePuzzle(self):

        queue = [[getattr(self.start, self.heuristicFunc)(), self.start]]
        path = []       # Current path
        expanded = []   # Explored positions
        numNodes = 0    # Total nodes

        while queue:

            # Finds which possible path has the lowest cost
            i = 0

            for j in range(1, len(queue)):

                if queue[i][0] > queue[j][0]:
                    
                    i = j

            path = queue[i]                     # Takes the path with the lowest cost
            queue = queue[: i] + queue[i + 1 :] # Removes the path taken
            endNode = path[-1]                  # The last position in the path

            if endNode.position == endNode.END_POS: # Checks to see if our end node is the last node in the result we want
                break

            if endNode.position in expanded: # Avoids infinite loop
                continue

            for move in endNode.getMoves(): # Loops through all possible moves while avoiding an infinite loop

                if move.position in expanded:

                    continue

                # Adds the path with the new positions and their values to the end of the queue
                newPath = [path[0] + self.calcNewHeuristic(move, endNode)] + path[1 :] + [move]
                queue.append(newPath)
                expanded.append(endNode.position)

            numNodes += 1

        self.numNodes = numNodes
        self.solution = path[1 :]