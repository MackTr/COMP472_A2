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

node, closedList, exactTime = gbfs(puzzleList[1])

print(closedList[4].heuristic)


# #PRINT SOLUTIONS FOR A*
# for puzzleNumber in range(0, len(puzzleList)):
#     node, closedList, exactTime = astar(puzzleList[puzzleNumber])
#     fileName = "txt/" + str(puzzleNumber) + "_astar-h1_solution.txt"
#     f = open(fileName, "w")
#     log = []
#     costTotal = 0
#     cost = 0
#     while node != None:
#         str1 = ' '.join(str(e) for e in node.state)
#         if(node.parent == None):
#             cost = 0
#         else:
#             cost = node.cost-node.parent.cost
#         log.append(str(cost) + ' ' + str1)
#         node = node.parent
#         costTotal = costTotal + cost
        
#     log.reverse()
#     for state in log:
#         f.write(state + '\n')
#     f.write(str(costTotal) + ' ' + str(exactTime))


# #PRINT SOLUTIONS FOR GBFS    
# for puzzleNumber in range(0, len(puzzleList)):
#     node, closedList, exactTime = gbfs(puzzleList[puzzleNumber])
#     fileName = "txt/" + str(puzzleNumber) + "_gbfs-h1_solution.txt"
#     f = open(fileName, "w")
#     log = []
#     costTotal = 0
#     cost = 0
#     while node != None:
#         str1 = ' '.join(str(e) for e in node.state)
#         if node.parent is None:
#             cost = 0
#         else:
#             cost = node.cost-node.parent.cost
#         log.append(str(cost) + ' ' + str1)
#         node = node.parent
#         costTotal = costTotal + cost
        

#     log.reverse()
#     for state in log:
#         f.write(state + '\n')
#     f.write(str(costTotal) + ' ' + str(exactTime))

# #PRINT SOLUTIONS FOR UCS    
# for puzzleNumber in range(0, len(puzzleList)):
#     node, closedList, exactTime = ucs(puzzleList[puzzleNumber])
#     fileName = "txt/" + str(puzzleNumber) + "_ucs_solution.txt"
#     f = open(fileName, "w")
#     log = []
#     costTotal = 0
#     cost = 0
#     while node != None:
#         str1 = ' '.join(str(e) for e in node.state)
#         if(node.parent == None):
#             cost = 0
#         else:
#             cost = node.cost-node.parent.cost
#         log.append(str(cost) + ' ' + str1)
#         node = node.parent
#         costTotal = costTotal + cost

#     log.reverse()
#     for state in log:
#         f.write(state + '\n')
#     f.write(str(costTotal) + ' ' + str(exactTime))

#PRINT SEARCH FILE FOR A STAR
   
# for puzzleNumber in range(0, len(puzzleList)):
#     node, closedList, exactTime = gbfs(puzzleList[puzzleNumber])
#     fileName = "txt/" + str(puzzleNumber) + "_gbfs-h1_solution.txt"
#     f = open(fileName, "w")
    
