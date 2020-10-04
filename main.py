from puzzle import Puzzle
from solver import Solver


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


def solve(type):
    puzzle = Puzzle(type)
    solver = Solver(puzzle, [1,2,3,4,5])
    puzzleArray = [puzzle.getGraph()]
    solver.solve([], [1, 2, 3, 4, 5], puzzleArray);

action = getSelectedAction()
while (action != "2"):
    puzzleType = choosePuzzle()
    solve(puzzleType)
    print("\n")
    action = getSelectedAction()

print("GoodBye!")