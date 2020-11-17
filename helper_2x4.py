#Global Variables
cornerPosition = [0,3,4,7]
firstGoalState = [1,2,3,4,5,6,7,0]
secondGoalState = [1,3,5,7,2,4,6,0]

#Heuristics Functions
def getBestHeuristic(state):
    firstGoalH = heuristicSumOfPermutations(state, firstGoalState)
    secondGoalH = heuristicSumOfPermutations(state, secondGoalState)
    if firstGoalH < secondGoalH: return firstGoalH
    else: return secondGoalH

def heuristicSimple(board, goal):
    heuristic = 0
    for i in range(0, len(board)):
        if(board[i]!=goal[i]):
            heuristic += 1
    return heuristic

def heuristicManhattan(board, goal):
    heuristic = 0

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


#Helper Functions
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

def createNewState(index, currentPosition, puzzleList):
    temporaryPuzzleList = puzzleList.copy()

    temporaryPuzzleList[currentPosition] = temporaryPuzzleList[index]
    temporaryPuzzleList[index] = 0
    return temporaryPuzzleList

def goalAchieved(puzzleList):
    if puzzleList == firstGoalState: return True
    elif puzzleList == secondGoalState: return True
    else: return False

def isStateInList(list, node):
    for index in range(0, len(list)):
        if list[index].state == node.state: return index
    return -1

def getZeroPosition(puzzle):
    for index in range(0, len(puzzle)):
        if puzzle[index] == 0:
            return index