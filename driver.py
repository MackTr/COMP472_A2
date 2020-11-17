from GBFS_h1 import *
from astar_h1 import *
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

node, closedList, exactTime = astar_h1(puzzleList[2])

# for i in closedList:
#     str1 = ' '.join(str(e) for e in i.state)
#     print(str(i.cost + i.heuristic)+ ' ' + str(i.heuristic) + ' ' + str(i.cost)+ ' ' + str1)


# for i in closedList:
#     str1 = ' '.join(str(e) for e in i.state)
#     if(node.parent is None):
#         cost = 0
#     else:
#         cost = i.cost #+ i.parent.cost
#     print("f(n) = " + str(i.heuristic+cost) + ",g(n) = " + str(cost) + ",h(n) = " + str(i.heuristic) + ",state = " + str1)


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
#             move = 0
#         else:
#             cost = node.cost - node.parent.cost
#             move = node.move
#         log.append(str(move) + ' ' + str(cost) + ' ' + str1)
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
#             move = 0
#         else:
#             cost = node.cost - node.parent.cost
#             move = node.move
#         log.append(str(move) + ' ' + str(cost) + ' ' + str1)
#         node = node.parent
#         costTotal = costTotal + cost
        

#     log.reverse()
#     for state in log:
#         f.write(state + '\n')
#     f.write(str(costTotal) + ' ' + str(exactTime))

#PRINT SOLUTIONS FOR UCS    
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
#             move = 0
#         else:
#             cost = node.cost-node.parent.cost
#             move = node.move
#         log.append(str(move) + ' ' + str(cost) + ' ' + str1)
#         node = node.parent
#         costTotal = costTotal + cost

#     log.reverse()
#     for state in log:
#         f.write(state + '\n')
#     f.write(str(costTotal) + ' ' + str(exactTime))


# SEARCH FILES

#PRINT SEARCH FILE FOR A STAR   
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = astar_h1(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_astar-h1_search.txt"
    f = open(fileName, "w")
    
    for i in closedList:
        str1 = ' '.join(str(e) for e in i.state)
        f.write(str(i.cost + i.heuristic)+ ' ' + str(i.cost) + ' ' + str(i.heuristic) + ' ' + str1 + '\n')
        

#PRINT SEARCH FILE FOR GBFS   
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = gbfs_h1(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_gbfs-h1_search.txt"
    f = open(fileName, "w")
    closedList.sort(key=getHeuristic)
    for i in closedList:
        str1 = ' '.join(str(e) for e in i.state)
        f.write(str(i.heuristic)+ ' ' + str(0) + ' ' + str(i.heuristic) + ' ' + str1 + '\n')       


#PRINT SEARCH FILE FOR UCS   
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = ucs(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_ucs_search.txt"
    f = open(fileName, "w")
    closedList.sort(key=getCost)
    for i in closedList:
        str1 = ' '.join(str(e) for e in i.state)
        print(str(i.cost)+ ' ' + str(i.cost) + ' ' + str(0)+ ' ' + str1 + '\n')
        f.write(str(i.cost)+ ' ' + str(i.cost) + ' ' + str(0)+ ' ' + str1 + '\n')     
