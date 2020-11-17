import time

#Read only
cornerPosition = [0,3,4,7]
firstGoalState = [1,2,3,4,5,6,7,0]
secondGoalState = [1,3,5,7,2,4,6,0]

def getWrappingMove(currentPosition):

    if currentPosition == 0:
        return 3
    elif currentPosition == 3:
        return 0
    elif currentPosition == 4:
        return 7
    elif currentPosition == 7:
        return 4

def getDiagonalMoves(currentPosition):

    if currentPosition == 0:
        return [5, 7]
    elif currentPosition == 3:
        return [4, 6]
    elif currentPosition == 4:
        return [1, 3]
    elif currentPosition == 7:
        return [0, 2]

def getVerticalMove(currentPosition):
    if currentPosition == 0:
        return 4
    elif currentPosition == 1:
        return 5
    elif currentPosition == 2:
        return 6
    elif currentPosition == 3:
        return 7
    elif currentPosition == 4:
        return 0
    elif currentPosition == 5:
        return 1
    elif currentPosition == 6:
        return 2
    elif currentPosition == 7:
        return 3

def getHorizontalMoves(currentPosition):
    if currentPosition == 0:
        return [1]
    elif currentPosition == 1:
        return [0, 2]
    elif currentPosition == 2:
        return [1, 3]
    elif currentPosition == 3:
        return [2]
    elif currentPosition == 4:
        return [5]
    elif currentPosition == 5:
        return [4, 6]
    elif currentPosition == 6:
        return [5, 7]
    elif currentPosition == 7:
        return [6]

def getPossibleMovesWithCost(puzzleList, currentPosition):

    move_cost_list = []
    for position in getHorizontalMoves(currentPosition):
        move_cost_list.append([position, 1])

    move_cost_list.append([getVerticalMove(currentPosition), 1])

    if isCornerPosition(currentPosition):

        move_cost_list.append([getWrappingMove(currentPosition), 2])

        for position in getDiagonalMoves(currentPosition):
            move_cost_list.append([position, 3])

    return move_cost_list


def isCornerPosition(currentPosition):

    for index in cornerPosition:
        if index == currentPosition: return True

    return False

def goalAchieved(puzzleList):
    if puzzleList == firstGoalState: return True
    elif puzzleList == secondGoalState: return True
    else: return False

def createNewState(index, currentPosition, puzzleList):
    temporaryPuzzleList = puzzleList.copy()

    temporaryPuzzleList[currentPosition] = temporaryPuzzleList[index]
    temporaryPuzzleList[index] = 0
    return temporaryPuzzleList


def getPossibleStateWithCost(puzzleList, currentPosition):

    move_cost_list = getPossibleMovesWithCost(puzzleList, currentPosition)
    state_cost_list = []

    for move_cost in move_cost_list:
        state_cost_list.append([createNewState(move_cost[0], currentPosition, puzzleList), move_cost[1]])

    return state_cost_list

def getChildrenNodes(puzzleList, currentPosition, node):

    move_cost_list = getPossibleMovesWithCost(puzzleList, currentPosition)
    nodes_list = []

    for move_cost in move_cost_list:
        state = createNewState(move_cost[0], currentPosition, puzzleList)
        heuristic = getBestHeuristic(state)
        parent = node
        nodes_list.append(Node(state, heuristic, parent))

    return nodes_list

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

def isStateInList(list, node):
    for index in range(0, len(list)):
        if list[index].state == node.state: return index
    return -1

def getZeroPosition(puzzle):
    for index in range(0, len(puzzle)):
        if puzzle[index] == 0:
            return index

class Node:
  def __init__(self, state, heuristic, parent):
    self.state = state
    self.heuristic = heuristic
    self.parent = parent

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