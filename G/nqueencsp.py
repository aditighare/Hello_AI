
class Board():

    def __init__(self, n):
        self.n = n
        self.spaces = n * n
        self.constraints = [0 for i in range(self.spaces)]
        self.queenSpaces = []

    def getPossibleMoves(self):
        possibleMoves = []
        for move, numConstraints in enumerate(self.constraints):
            if numConstraints == 0:
                possibleMoves.append(move)
        return possibleMoves

    def makeMove(self, space):
        self.queenSpaces.append(space)
        self.addOrRemoveConstraints(space)

    def removeMove(self, space):
        self.queenSpaces.remove(space)
        self.addOrRemoveConstraints(space, add=False)

    def addOrRemoveConstraints(self, move, add=True):
        if (add):
            mutationFx = self.addConstraint
        else:
            mutationFx = self.removeConstraint
        row = move // self.n
        col = move % self.n
        rdStartRow = row + col
        ldStartRow = row - col

        for i in range(self.n):
            mutationFx(self.rcToSpace(row, i))
            mutationFx(self.rcToSpace(i, col))
            if rdStartRow > -1:
                mutationFx(self.rcToSpace(rdStartRow, i))
                rdStartRow -= 1
            if ldStartRow < self.n:
                mutationFx(self.rcToSpace(ldStartRow, i))
                ldStartRow += 1
    def addConstraint(self, move):
        if not move == -1:
            self.constraints[move] += 1
    def removeConstraint(self, move):
        if not move == -1:
            self.constraints[move] -= 1

    def rcToSpace(self, row, col):
        space = row * self.n + col
        if space >= self.spaces or space < 0:
            return -1
        else:
            return space


    def print(self):
        for r in range(self.n):
            row = ""
            for c in range(self.n):
                if(self.rcToSpace(r,c) in self.queenSpaces):
                    row += "Q"
                else:
                    row += "-"
                row += "  "
            print(row)
