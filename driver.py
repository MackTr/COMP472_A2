from UCS import *

file_read = open("samplePuzzles.txt", "r")

puzzleList = []


def addPuzzleToList(puzzleText):
    puzzle = []
    for char in puzzleText:
        if char.isnumeric():
            puzzle.append(int(char))
    puzzleList.append(puzzle)

for puzzleText in file_read:
    addPuzzleToList(puzzleText)

for index in range(0, len(puzzleList)):

    ucs_result = ucs(puzzleList[0])
    file_write_solution = open(str(index) + "_ucs_solution.txt", "w")
    file_write_search = open(str(index) + "_ucs_search.txt", "w")

    if ucs_result != None:
        print("need to be ")
    else:
        file_write_solution.write("No solution")
        file_write_search.write("No solution")

    file_write_solution.close()
    file_write_search.close()


