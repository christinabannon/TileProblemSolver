import copy
import sys
import printer
import numpy as np
import pieces

from puzzle import Puzzle



class Solver(object):


    def __init__(self, puzzle, allPieces):
        self.puzzle = puzzle
        self.allPieces = allPieces


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


    def getAvailable(self, piecesFit, piecesFailed):
        piecesAvailable = np.setdiff1d(self.allPieces, piecesFit)
        piecesAvailable = np.setdiff1d(piecesAvailable, piecesFailed)
        return piecesAvailable


    def solve(self, piecesFit, piecesLeft, puzzles, spaces = ""):
        if (len(piecesFit) == len(self.allPieces)):
            print(printer.getPretty(puzzles[len(puzzles) - 1], spaces))
            print("EXITED THROUGH COMPLETION")
            sys.exit(0)
        else:
            # for pieceNumber in piecesLeft:
            for pieceIndex in range(0, len(piecesLeft)):
                pieceNumber = piecesLeft[pieceIndex]
                # print(spaces + "pieceNumber = " + str(pieceNumber))
                # print(spaces + "piecesFit:" + str(piecesFit))
                # print(spaces + "piecesLeft:" + str(piecesLeft))
                piece = pieces.getPiece(pieceNumber)
                fits, newPuzzle = self.fitPiece(puzzles[len(puzzles)-1], piece)
                if fits:
                    print(spaces + "pieceNumber = " + str(pieceNumber) + " fits")
                    oldPiecesLeft = copy.deepcopy(piecesLeft)
                    piecesFit.append(pieceNumber)
                    piecesLeft.remove(pieceNumber)
                    puzzles.append(newPuzzle)
                    valid = self.solve(piecesFit, piecesLeft, puzzles, (spaces + "  "))
                    puzzles.pop()
                    poppedPiece = piecesFit.pop()
                    piecesLeft = oldPiecesLeft
                    print(spaces + "-poppedPiece = " + str(poppedPiece))
                    print(spaces + "-piecesFit:" + str(piecesFit))
                    print(spaces + "-piecesLeft:" + str(piecesLeft))
                else:
                    print(spaces + "pieceNumber = " + str(pieceNumber) + " does NOT fit")

