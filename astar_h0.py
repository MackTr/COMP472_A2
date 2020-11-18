from helper_2x4 import *
import time

def getBestHeuristic(state):
    firstGoalH = demoHeuristic(state)
    secondGoalH = demoHeuristic(state)
    if firstGoalH < secondGoalH: return firstGoalH
    else: return secondGoalH

def demoHeuristic(board):
    if board[7] == 0: return 0
    else: return 1

class Node:
  def __init__(self, state, move, cost, heuristic, fn, parent):
    self.state = state
    self.move = move
    self.cost = cost
    self.heuristic = heuristic
    self.fn = fn
    self.parent = parent

def getChildrenNodes(puzzleList, currentPosition, node):

    move_cost_list = getPossibleMovesWithCost(puzzleList, currentPosition)
    nodes_list = []

    for move_cost in move_cost_list:
        state = createNewState(move_cost[0], currentPosition, puzzleList)
        move = move_cost[0]
        cost = node.cost + move_cost[1]
        heuristic = getBestHeuristic(state)
        fn = cost + heuristic
        parent = node
        nodes_list.append(Node(state, move, cost, heuristic, fn, parent))

    return nodes_list

def getFn(node: Node):
    return node.fn

def astar_h0(puzzleList):

    openList = []
    closedList = []

    openList.append(Node(puzzleList, 0, 0, 0, 0, None))

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
            if openListPosition > -1 and openList[openListPosition].fn > newNode.fn:
                openList[openListPosition] = newNode
            elif openListPosition == -1 and closedListPosition > -1 and closedList[closedListPosition].fn > newNode.fn:
                closedList.pop(closedListPosition)
                openList.append(newNode)
            elif openListPosition == -1 and closedListPosition == -1:
                openList.append(newNode)


        openList.sort(key=getFn)

    if timeOut < time.time():
        node = None
        exactTime = None
        return node, closedList, exactTime