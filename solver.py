import copy
import sys
import printer
import numpy as np
import pieces


class Solver(object):


    def __init__(self, puzzle, allPieces):
        self.puzzle = puzzle
        self.allPieces = allPieces
        self.backtracks = 0


    def fitCell(self, pieceValue, puzzleValue):
        return not (puzzleValue >= 0 and pieceValue > 0)


    def loopCells(self, puzzle, piece):
        # goal is to see if a given block fits in this puzzle space without any rotation
        pieceLength= len(piece[0])
        pieceHeight = len(piece)
        allPieceCells = pieceHeight * pieceLength
        pieceCellsFilled = 0

        testPuzzle = copy.deepcopy(puzzle)
        puzzleRow = 0
        puzzleCol = 0

        pieceCellsToBePlaced = (pieceCellsFilled < allPieceCells)
        puzzleSpotsLeft = ((puzzleRow < len(testPuzzle)) and (puzzleCol < len(testPuzzle[0])))

        # while the problem has not been solved, and we still have spots to search
        while pieceCellsToBePlaced and puzzleSpotsLeft:
            pieceCol = 0
            pieceRow = 0
            pieceCellsFilled = 0
            testPuzzle = copy.deepcopy(puzzle)

            pieceCell = piece[pieceRow][pieceCol]
            puzzleCell = testPuzzle[puzzleRow + pieceRow][puzzleCol + pieceCol]
            cellFits = self.fitCell(pieceCell, puzzleCell)

            puzzleSpotsLeft = (((puzzleRow + pieceRow) < len(testPuzzle)) and ((puzzleCol + pieceCol) < len(testPuzzle[0])))
            while cellFits and pieceCellsToBePlaced and puzzleSpotsLeft:
                pieceCell = piece[pieceRow][pieceCol]
                puzzleCell = testPuzzle[puzzleRow + pieceRow][puzzleCol + pieceCol]
                cellFits = self.fitCell(pieceCell, puzzleCell)
                if cellFits:
                    newPuzzleCellValue = max(puzzleCell, pieceCell)
                    testPuzzle[puzzleRow + pieceRow][puzzleCol + pieceCol] = newPuzzleCellValue
                    pieceCellsFilled += 1
                    pieceCol += 1
                    if pieceCol >= pieceLength:
                        pieceCol %= pieceLength
                        pieceRow += 1
                pieceCellsToBePlaced = (pieceCellsFilled < allPieceCells)
                puzzleSpotsLeft = (((puzzleRow + pieceRow) < len(testPuzzle)) and ((puzzleCol + pieceCol) < len(testPuzzle[0])))

            if pieceCellsToBePlaced:
                puzzleCol = 1 + puzzleCol
                if puzzleCol >= len(testPuzzle[0]):
                    puzzleCol %= len(testPuzzle[0])
                    puzzleRow += 1
                puzzleSpotsLeft = ((puzzleRow < len(testPuzzle)) and (puzzleCol < len(testPuzzle[0])))
                testPuzzle = copy.deepcopy(puzzle)

        return ((pieceCellsFilled == allPieceCells), testPuzzle)


    def fitPiece(self, puzzle, piece):
        # goal is to rotate each block to see if that helps it fit into the puzzle
        fit, testPuzzle = self.loopCells(puzzle, piece)
        if not fit:
            piece = np.flip(piece, 0)
            fit, testPuzzle = self.loopCells(puzzle, piece)
            if not fit:
                piece = np.flip(piece, 1)
                fit, testPuzzle = self.loopCells(puzzle, piece)
                if not fit:
                    piece = np.flip(piece, 0)
                    fit, testPuzzle = self.loopCells(puzzle, piece)
        return fit, testPuzzle


    def puzzleValid(self, fits, puzzle):
        # going to look for cube combos less than 3, return false if they exist
        if fits:
            row = 0
            while row < len(puzzle):
                col = 0
                while col < len(puzzle[0]):
                    if puzzle[row][col] == -1:
                        piecesConnected = self.checkConnections(puzzle, [row, col], [row, col])
                        if piecesConnected < 3:
                            return False
                        col += 3
                    else:
                        col += 1
                row += 1
            return True
        else:
            return False


    def checkConnections(self, puzzle, lastCell, currentCell, piecesConnected=1):
        row = currentCell[0]
        col = currentCell[1]

        if (piecesConnected < 3 and (row - 1) >= 0) and (puzzle[row - 1][col] == -1) and ([row - 1, col] != lastCell):
            piecesConnected += 1
            nextCell = [row - 1, col]
            piecesConnected = self.checkConnections(puzzle, currentCell, nextCell, piecesConnected)

        if (piecesConnected < 3 and row + 1 < len(puzzle)) and (puzzle[row + 1][col] == -1) and ([row + 1, col] != lastCell):
            piecesConnected += 1
            nextCell = [row + 1, col]
            piecesConnected = self.checkConnections(puzzle, currentCell, nextCell, piecesConnected)

        if (piecesConnected < 3 and (col - 1) >= 0) and (puzzle[row][col - 1] == -1) and ([row, col - 1] != lastCell):
            piecesConnected += 1
            nextCell = [row, col - 1]
            piecesConnected = self.checkConnections(puzzle, currentCell, nextCell, piecesConnected)

        if (piecesConnected < 3 and (col + 1) < len(puzzle[0])) and (puzzle[row][col + 1] == -1) and ([row, col + 1] != lastCell):
            piecesConnected += 1
            nextCell = [row, col + 1]
            piecesConnected = self.checkConnections(puzzle, currentCell, nextCell, piecesConnected)

        return piecesConnected


    def getAvailable(self, piecesFit, piecesFailed):
        piecesAvailable = np.setdiff1d(self.allPieces, piecesFit)
        piecesAvailable = np.setdiff1d(piecesAvailable, piecesFailed)
        return piecesAvailable


    def solve(self, piecesFit, piecesLeft, puzzleStack, spaces = ""):
        if (len(piecesFit) == len(self.allPieces)):
            print(printer.getPretty(puzzleStack[len(puzzleStack) - 1], spaces))
            print(spaces + "COMPLETED")
            print("backtracks = " + str(self.backtracks))
            # sys.exit(0)
            return True
        else:
            for pieceIndex in range(0, len(piecesLeft)):
                pieceNumber = piecesLeft[pieceIndex]
                piece = pieces.getPiece(pieceNumber)
                fits, newPuzzle = self.fitPiece(puzzleStack[len(puzzleStack)-1], piece)
                fits = self.puzzleValid(fits, newPuzzle)
                if fits:
                    print(printer.getPretty(newPuzzle, spaces))
                    oldPiecesLeft = copy.deepcopy(piecesLeft)
                    piecesFit.append(pieceNumber)
                    piecesLeft.remove(pieceNumber)
                    puzzleStack.append(newPuzzle)
                    solved = self.solve(piecesFit, piecesLeft, puzzleStack, (spaces + "    "))
                    if (solved):
                        return True
                    else:
                        puzzleStack.pop()
                        piecesFit.pop()
                        piecesLeft = oldPiecesLeft
                        self.backtracks += 1

