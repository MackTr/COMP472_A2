from helper_2x4 import *
import time

class Node:
  def __init__(self, state, move, cost, parent):
    self.state = state
    self.move = move
    self.cost = cost
    self.parent = parent
      
def getChildrenNodes(puzzleList, currentPosition, node):

    move_cost_list = getPossibleMovesWithCost(puzzleList, currentPosition)
    nodes_list = []

    for move_cost in move_cost_list:
        state = createNewState(move_cost[0], currentPosition, puzzleList)
        move = move_cost[0]
        cost = node.cost + move_cost[1]
        parent = node
        nodes_list.append(Node(state, move, cost, parent))

    return nodes_list

def getCost(node: Node):
    return node.cost

def ucs(puzzleList):

    openList = []
    closedList = []

    openList.append(Node(puzzleList, 0, 0, None))

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
            if openListPosition > -1 and openList[openListPosition].cost > newNode.cost:
                openList[openListPosition] = newNode
            elif openListPosition == -1 and closedListPosition > -1 and closedList[closedListPosition].cost > newNode.cost:
                closedList.pop(closedListPosition)
                openList.append(newNode)
            elif openListPosition == -1 and closedListPosition == -1:
                openList.append(newNode)

        openList.sort(key=getCost)

    if timeOut < time.time():
        node = None
        exactTime = None
        return node, closedList, exactTime
