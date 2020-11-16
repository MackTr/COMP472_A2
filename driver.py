file = open("samplePuzzles.txt", "r")

puzzleList = []


def addPuzzleToList(puzzleText):
    puzzle = []
    for char in puzzleText:
        if char.isnumeric():
            puzzle.append(int(char))
    puzzleList.append(puzzle)

for puzzleText in file:
    addPuzzleToList(puzzleText)

print(puzzleList)

