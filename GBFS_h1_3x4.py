from helper_3x4 import *
import time

def getBestHeuristic(state):
    firstGoalH = heuristicSimple(state, firstGoalState)
    secondGoalH = heuristicSimple(state, secondGoalState)
    if firstGoalH < secondGoalH: return firstGoalH
    else: return secondGoalH

def heuristicSimple(board, goal):
    heuristic = 0
    for i in range(0, len(board)):
        if(board[i]!=goal[i]):
            heuristic += 1
    return heuristic

class Node:
  def __init__(self, state, move, cost, heuristic, parent):
    self.state = state
    self.move = move
    self.cost = cost
    self.heuristic = heuristic
    self.parent = parent

def getChildrenNodes(puzzleList, currentPosition, node):

    move_cost_list = getPossibleMovesWithCost(puzzleList, currentPosition)
    nodes_list = []

    for move_cost in move_cost_list:
        state = createNewState(move_cost[0], currentPosition, puzzleList)
        move = move_cost[0]
        cost = node.cost + move_cost[1]
        heuristic = getBestHeuristic(state)
        parent = node
        nodes_list.append(Node(state, move, cost, heuristic, parent))

    return nodes_list

def getHeuristic(node: Node):
    return node.heuristic

def gbfs_h1(puzzleList):

    openList = []
    closedList = []

    openList.append(Node(puzzleList, 0, 0, 0, None))

    timeOut = time.time() + 60

    while timeOut > time.time():

        node = openList.pop(0)
        puzzleList = node.state
        currentPosition = getZeroPosition(puzzleList)

        if goalAchieved(puzzleList):
            exactTime = 60 - (timeOut - time.time())
            return node, closedList, exactTime

        closedList.append(node)

        newNodes = getChildrenNodes(puzzleList, currentPosition, node)

        for newNode in newNodes:
            openListPosition = isStateInList(openList, newNode)
            closedListPosition = isStateInList(closedList, newNode)
            if openListPosition == -1 and closedListPosition == -1:
                openList.append(newNode)


        openList.sort(key=getHeuristic)

    if timeOut < time.time():
        node = None
        exactTime = None
        return node, closedList, exactTime

file = open("sample3x4.txt", "r")

puzzleList = []

def addPuzzleToList(puzzleText):
    puzzleText.replace("\\n", "")
    puzzle = puzzleText.split(' ')
    for index in range(0, len(puzzle)):
        puzzle[index] = int(puzzle[index])
    puzzleList.append(puzzle)

for puzzleText in file:
    addPuzzleToList(puzzleText)
    
for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = gbfs_h1(puzzleList[puzzleNumber])
    fileName = "3x4/" + str(puzzleNumber) + "_gbfs-h1_3x4_solution.txt"
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

for puzzleNumber in range(0, len(puzzleList)):
    node, closedList, exactTime = gbfs_h1(puzzleList[puzzleNumber])
    fileName = "3x4/" + str(puzzleNumber) + "_gbfs-h1_3x4_search.txt"
    f = open(fileName, "w")
#    closedList.sort(key=getHeuristic)
    for i in closedList:
        str1 = ' '.join(str(e) for e in i.state)
        f.write(str(i.heuristic)+ ' ' + str(0) + ' ' + str(i.heuristic) + ' ' + str1 + '\n')
