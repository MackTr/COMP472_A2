#from astart import *
from GBFS import *

file_read = open("samplePuzzles.txt", "r")
List = file_read.readlines()

puzzleList = []
for i in List:
    i = i.strip()
    i = i.replace(" ", ", ")
   # i = int(i)
    puzzleList.append(i)

puzzle = puzzleList[0]
#astar(puzzle)
gbfs(puzzle)




