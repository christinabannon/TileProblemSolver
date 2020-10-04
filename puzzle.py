# the puzzle will be one of the 4 Types
# each puzzle will be a 2d array
#

class Puzzle(object):
    puzzleType = 0
    graph = [[]]
    pieces = [1, 2, 3, 4, 5]
    def __init__(self, type):
        self.puzzleType = type
        if type == "1":
            self.graph = [[ 0,  0,  0,  0, -1, -1,  0,  0,  0,  0],
                          [ 0,  0,  0, -1, -1, -1, -1,  0,  0,  0],
                          [ 0,  0, -1, -1, -1, -1, -1, -1,  0,  0],
                          [ 0, -1, -1, -1, -1, -1, -1, -1, -1,  0],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
        elif type == "2":
            self.graph = [[ 0, -1, -1, -1, -1,  0],
                          [-1, -1, -1, -1, -1, -1],
                          [ 0, -1, -1, -1, -1,  0],
                          [-1, -1, -1, -1, -1, -1],
                          [ 0, -1, -1, -1, -1,  0],
                          [-1, -1, -1, -1, -1, -1]]
        elif type == "3":
            self.graph = [[ 0,  0,  0,  0, -1, -1,  0,  0,  0,  0],
                          [ 0, -1, -1, -1, -1, -1, -1, -1, -1,  0],
                          [ 0,  0, -1, -1, -1, -1, -1, -1,  0,  0],
                          [ 0,  0,  0, -1, -1, -1, -1,  0,  0,  0],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
        elif type == "4":
            self.graph = [[ 0,  0,  0, -1, -1, -1, -1,  0,  0,  0],
                          [ 0,  0, -1, -1, -1, -1, -1, -1,  0,  0],
                          [ 0,  0,  0, -1, -1, -1, -1,  0,  0,  0],
                          [ 0,  0,  0,  0, -1, -1,  0,  0,  0,  0],
                          [ 0,  0,  0, -1, -1, -1, -1,  0,  0,  0],
                          [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

    def getType(self):
        return self.puzzleType

    def getGraph(self):
        return self.graph

    def getSize(self):
        return len(self.graph[0]) * len(self.graph)

    def getNumCols(self):
        return len(self.graph[0])

    def getNumRows(self):
        return len(self.rows)





