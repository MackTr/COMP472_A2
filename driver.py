from GBFS import *
from astart import *
from UCS import *

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


#astar(puzzleList[2])



nodeA, closedListA = astar(puzzleList[0])
#nodeU, closedListU = ucs(puzzleList[0])
#nodeG, closedListG = gbfs(puzzleList[0])
#f = open("txt/gbfs.txt", "w")
#while node != None:
#    f.write(node.cost + node.state)
log = []
while nodeA != None:
    str1 = ' '.join(str(e) for e in nodeA.state)
    log.append(str(nodeA.cost) + ' ' + str1)
    nodeA = nodeA.parent

log.reverse()
for state in log:
    print(state)
    
#str1 = ' '.join(str(e) for e in nodeA.state)
#print(str(nodeA.cost) + ' ' + str1) 
