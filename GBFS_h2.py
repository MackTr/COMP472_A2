from helper_2x4 import *
import time

def getBestHeuristic(state):
    firstGoalH = heuristicSumOfPermutations(state, firstGoalState)
    secondGoalH = heuristicSumOfPermutations(state, secondGoalState)
    if firstGoalH < secondGoalH: return firstGoalH
    else: return secondGoalH

def heuristicSumOfPermutations(board, goal):
    heuristic = 0
    for indexNumber in range(0, len(board)):
        number = board[indexNumber]
        shouldBeLeft = getNumberOnTheLeft(number, goal)

        for indexOnRight in range(indexNumber, len(board)):
           for numberOnLeft in shouldBeLeft:
               if numberOnLeft == board[indexOnRight] : heuristic += 1

    return heuristic

def getNumberOnTheLeft(number, goal):
    numbersOnTheLeft = []
    indexOfNumberInGoal = 0

    for index in range(0, len(goal)):
        if goal[index] == number:
            indexOfNumberInGoal = index

    for index in range(0, indexOfNumberInGoal):
        numbersOnTheLeft.append(goal[index])

    return numbersOnTheLeft

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

def gbfs_h2(puzzleList):

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