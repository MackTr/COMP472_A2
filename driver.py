#from GBFS_h0 import *
from GBFS_h1 import *
from GBFS_h2 import *
#from astar_h0 import *
from astar_h1 import *
from astar_h2 import *
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

# SOLUTIONS FILES

#PRINT SOLUTIONS FOR A* H1
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = astar_h1(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_astar-h1_solution.txt"
    f = open(fileName, "w")
    log = []
    costTotal = 0
    cost = 0
    if node is None:
        f.write("No solution")
    else:
        while node != None:
            str1 = ' '.join(str(e) for e in node.state)
            if(node.parent == None):
                cost = 0
                move = 0
            else:
                cost = node.cost - node.parent.cost
                move = node.move
            log.append(str(move) + ' ' + str(cost) + ' ' + str1)
            node = node.parent
            costTotal = costTotal + cost  
        log.reverse()
        for state in log:
            f.write(state + '\n')
        f.write(str(costTotal) + ' ' + str(exactTime))


#PRINT SOLUTIONS FOR A* H2
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = astar_h2(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_astar-h2_solution.txt"
    f = open(fileName, "w")
    log = []
    costTotal = 0
    cost = 0
    if node is None:
        f.write("No solution")
    else:
        while node != None:
            str1 = ' '.join(str(e) for e in node.state)
            if(node.parent == None):
                cost = 0
                move = 0
            else:
                cost = node.cost - node.parent.cost
                move = node.move
            log.append(str(move) + ' ' + str(cost) + ' ' + str1)
            node = node.parent
            costTotal = costTotal + cost  
        log.reverse()
        for state in log:
            f.write(state + '\n')
        f.write(str(costTotal) + ' ' + str(exactTime))


#PRINT SOLUTIONS FOR GBFS H1   
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = gbfs_h1(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_gbfs-h1_solution.txt"
    f = open(fileName, "w")
    log = []
    costTotal = 0
    cost = 0
    if node is None:
        f.write("No solution")
    else:
        while node != None:
            str1 = ' '.join(str(e) for e in node.state)
            if node.parent is None:
                cost = 0
                move = 0
            else:
                cost = node.cost - node.parent.cost
                move = node.move
            log.append(str(move) + ' ' + str(cost) + ' ' + str1)
            node = node.parent
            costTotal = costTotal + cost
        log.reverse()
        for state in log:
            f.write(state + '\n')
        f.write(str(costTotal) + ' ' + str(exactTime))


#PRINT SOLUTIONS FOR GBFS H2   
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = gbfs_h2(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_gbfs-h2_solution.txt"
    f = open(fileName, "w")
    log = []
    costTotal = 0
    cost = 0
    if node is None:
        f.write("No solution")
    else:
        while node != None:
            str1 = ' '.join(str(e) for e in node.state)
            if node.parent is None:
                cost = 0
                move = 0
            else:
                cost = node.cost - node.parent.cost
                move = node.move
            log.append(str(move) + ' ' + str(cost) + ' ' + str1)
            node = node.parent
            costTotal = costTotal + cost
        log.reverse()
        for state in log:
            f.write(state + '\n')
        f.write(str(costTotal) + ' ' + str(exactTime))


#PRINT SOLUTIONS FOR UCS    
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = ucs(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_ucs_solution.txt"
    f = open(fileName, "w")
    log = []
    costTotal = 0
    cost = 0
    if node is None:
        f.write("No solution")
    else:
        while node != None:
            str1 = ' '.join(str(e) for e in node.state)
            if(node.parent == None):
                cost = 0
                move = 0
            else:
                cost = node.cost-node.parent.cost
                move = node.move
            log.append(str(move) + ' ' + str(cost) + ' ' + str1)
            node = node.parent
            costTotal = costTotal + cost
        log.reverse()
        for state in log:
            f.write(state + '\n')
        f.write(str(costTotal) + ' ' + str(exactTime))


# # SEARCH FILES

#PRINT SEARCH FILE FOR A STAR H1   
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = astar_h1(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_astar-h1_search.txt"
    f = open(fileName, "w")  
    for i in closedList:
        str1 = ' '.join(str(e) for e in i.state)
        f.write(str(i.cost + i.heuristic)+ ' ' + str(i.cost) + ' ' + str(i.heuristic) + ' ' + str1 + '\n')


#PRINT SEARCH FILE FOR A STAR H2   
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = astar_h2(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_astar-h2_search.txt"
    f = open(fileName, "w")  
    for i in closedList:
        str1 = ' '.join(str(e) for e in i.state)
        f.write(str(i.cost + i.heuristic)+ ' ' + str(i.cost) + ' ' + str(i.heuristic) + ' ' + str1 + '\n')
        

#PRINT SEARCH FILE FOR GBFS H1  
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = gbfs_h1(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_gbfs-h1_search.txt"
    f = open(fileName, "w")
#    closedList.sort(key=getHeuristic)
    for i in closedList:
        str1 = ' '.join(str(e) for e in i.state)
        f.write(str(i.heuristic)+ ' ' + str(0) + ' ' + str(i.heuristic) + ' ' + str1 + '\n')


#PRINT SEARCH FILE FOR GBFS H2  
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = gbfs_h2(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_gbfs-h2_search.txt"
    f = open(fileName, "w")
    for i in closedList:
        str1 = ' '.join(str(e) for e in i.state)
        f.write(str(i.heuristic)+ ' ' + str(0) + ' ' + str(i.heuristic) + ' ' + str1 + '\n')


#PRINT SEARCH FILE FOR UCS   
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = ucs(puzzleList[puzzleNumber])
    fileName = "txt/" + str(puzzleNumber) + "_ucs_search.txt"
    f = open(fileName, "w")
    for i in closedList:
        str1 = ' '.join(str(e) for e in i.state)
        f.write(str(i.cost)+ ' ' + str(i.cost) + ' ' + str(0)+ ' ' + str1 + '\n')     
