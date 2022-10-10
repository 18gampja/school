import random

class Puzzle:

    def __init__(self, position):

        self.position = position
        self.NUM_ROWS = len(position)
        self.NUM_COLUMNS = len(position[0])
        self.END_POS = self.genEndPos()

    def __str__(self):

        # Generates a string to represent the current puzzle state
        puzzleLength = (3 * self.NUM_ROWS) + 1
        puzzleString =  '-' * puzzleLength + '\n'

        for i in range(self.NUM_ROWS):

            for j in range(self.NUM_COLUMNS):

                puzzleString += '|{0: >2}'.format(str(self.position[i][j]))

                if(j == self.NUM_COLUMNS - 1):

                    puzzleString += '|\n'

        return puzzleString

    def genEndPos(self):

        # Creates a puzzle object that represents completion to compare to
        endPos = []
        newRow = []

        for i in range(1, self.NUM_ROWS * self.NUM_COLUMNS + 1):
            
            newRow.append(i)
            
            if(len(newRow) == self.NUM_COLUMNS):

                endPos.append(newRow)
                newRow = []

        endPos[-1][-1] = 0

        return endPos

    def swap(self, x1, y1, x2, y2):

        # Swaps two tiles
        clone = [list(row) for row in self.position]
        
        temp = clone[x1][y1]
        clone[x1][y1] = clone[x2][y2]
        clone[x2][y2] = temp

        return clone

    @staticmethod
    def isOdd(num):

        return num % 2 != 0

    @staticmethod
    def isEven(num):

        return num % 2 == 0

    def countBlank(self):

        # Determines how many spaces from the bottom row
        zeroRow, _ = self.getCoords(0)
        return self.NUM_ROWS - zeroRow

    def getCoords(self, tile, pos = None):

        # Returns the coordinates of a tile
        if not pos:
            pos = self.position

        for i in range(self.NUM_ROWS):

            for j in range(self.NUM_COLUMNS):

                if pos[i][j] == tile:
                    return i, j

        return RuntimeError('Invalid tile value')

    def inversionCount(self):

        # Counts inversions by seeing if numbers precede smaller numbers, returns total
        invCount = 0
        puzzList = [number for row in self.position for number in row if number != 0]

        for i in range(len(puzzList)):
            
            for j in range(i + 1, len(puzzList)):
                
                if puzzList[i] > puzzList[j]:

                    invCount += 1

        return invCount

    def getMoves(self):

        # Checks to see which moves are valid to build a list of possible moves
        moves = []

        i, j = self.getCoords(0)

        if i > 0:

            moves.append(Puzzle(self.swap(i, j, i - 1, j))) # Move up

        if j < self.NUM_COLUMNS - 1:

            moves.append(Puzzle(self.swap(i, j, i, j + 1))) # Move right

        if j > 0:

            moves.append(Puzzle(self.swap(i, j, i, j - 1))) # Move left

        if i < self.NUM_ROWS - 1:

            moves.append(Puzzle(self.swap(i, j, i + 1, j))) # Move down

        return moves

    def manhattanDistance(self):

        dist = 0

        # finds the distance between two points
        for i in range(self.NUM_ROWS):

            for j in range(self.NUM_COLUMNS):

                i1, j1 = self.getCoords(self.position[i][j], self.END_POS)
                dist += abs(i - i1) + abs(j - j1)

        return dist

    def misplaced(self):

        # Counts how many tiles are in the wrong spot
        misplaced = 0

        for i in range(self.NUM_ROWS):

            for j in range(self.NUM_COLUMNS):

                if self.position[i][j] != self.END_POS[i][j]:
                    
                    misplaced += 1

    def isSolvable(self):

        # Checks to see if the puzzle is solvable
        invCount = self.inversionCount()
        blankPos = self.countBlank()

        # Checks for an even inversion, unless the blank space an even number of moves from a bottom corner
        if self.isOdd(self.NUM_ROWS) and self.isEven(invCount):
            return True

        elif self.isEven(self.NUM_ROWS) and self.isEven(blankPos) and self.isOdd(invCount):
            return True

        elif not self.isOdd(self.NUM_ROWS) and self.isOdd(blankPos) and self.isEven(invCount):
            return True

        else:
            return False

    def randPos(self):

        # Shuffles puzzle until it's solvable
        while True:

            random.shuffle(self.position)

            for row in self.position:
                random.shuffle(row)

            if self.isSolvable():
                break