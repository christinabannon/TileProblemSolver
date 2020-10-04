# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import numpy as np

from puzzle import Puzzle
from solver import Solver
import printer


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def getSelectedAction():
    selectedAction = 0
    while selectedAction != "2" and selectedAction != "1":
        selectedAction =  input("Select an action"
                  "\n1. Select a puzzle to solve"
                  "\n2. Exit the program\n")
    return selectedAction

def choosePuzzle():
    puzzleType = 0
    while puzzleType != "1" and puzzleType != "2" and puzzleType != "3" and puzzleType !="4":
        puzzleType = input("Select a puzzle type 1 through 4\n")
    return puzzleType

# selectedAction = getSelectedAction()
# if selectedAction == "1":
#     puzzleType = choosePuzzle()
#     puzzle = Puzzle(type = puzzleType)
#     print(puzzle.getType() + "\n")
#     print(puzzle.getPrettyPuzzle() + "\n")
#
#     show puzzle
#     solve puzzle
#     show solution
#
#
# elif selectedAction == "2":
#     print("goodbye!")

def solve():
    puzzleType = type
    puzzle = Puzzle("4")
    allPieces = [1, 2, 3, 4, 5]
    solver = Solver(puzzle, allPieces)
    piecesUsed = []
    puzzleArray = [puzzle.getGraph()]
    solver.solve([], allPieces, puzzle);




# loopCellsTest()

solve()
