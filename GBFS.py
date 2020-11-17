from helper_2x4 import *
import time

class Node:
  def __init__(self, state, heuristic, parent):
    self.state = state
    self.heuristic = heuristic
    self.parent = parent

def getChildrenNodes(puzzleList, currentPosition, node):

    move_cost_list = getPossibleMovesWithCost(puzzleList, currentPosition)
    nodes_list = []

    for move_cost in move_cost_list:
        state = createNewState(move_cost[0], currentPosition, puzzleList)
        heuristic = getBestHeuristic(state)
        parent = node
        nodes_list.append(Node(state, heuristic, parent))

    return nodes_list

def getHeuristic(node: Node):
    return node.heuristic

def gbfs(puzzleList):

    openList = []
    closedList = []

    openList.append(Node(puzzleList, 0, None))

    timeOut = time.time() + 60
    timePrint = time.time() + 2

    while timeOut > time.time():

        node = openList.pop(0)
        puzzleList = node.state
        currentPosition = getZeroPosition(puzzleList)

        if goalAchieved(puzzleList):
            print(timeOut - time.time())
            print("found!")
            print(puzzleList)


            log = []
            print("closedList")
            for puzzle in closedList:
                print(puzzle.state)

            print("openList")
            while node != None:
                log.append(node.state)
                node = node.parent

            log.reverse()
            for state in log:
                print(state)

            return node, closedList
            break

        closedList.append(node)

        newNodes = getChildrenNodes(puzzleList, currentPosition, node)

        for newNode in newNodes:
            openListPosition = isStateInList(openList, newNode)
            closedListPosition = isStateInList(closedList, newNode)
            if openListPosition == -1 and closedListPosition == -1:
                openList.append(newNode)


        openList.sort(key=getHeuristic)

        if timePrint < time.time():
            timePrint = time.time() + 2
            print(puzzleList)
            print("running")


    if timeOut < time.time():

        for index in range(0, len(openList)):
            if goalAchieved(openList[index].state):
                print("it was in there")
        for index in range(0, len(closedList)):
            if goalAchieved(closedList[index].state):
                print("it was in closed!")

        print("gbfs time out!")
        return None

#gbfs([3, 1, 2, 6, 5, 0, 7, 4])