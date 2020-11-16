puzzleList = [1,0,3,4,5,6,2,7]
currentPosition = [1]

cornerPosition = [0,3,4,7]
firstGoalState = [1,2,3,4,5,6,7,0]
secondGoalState = [1,3,5,7,2,4,6,0]

def checkWrappingMove():

    if currentPosition == 0:
        return 3
    elif currentPosition == 3:
        return 0
    elif currentPosition == 4:
        return 7
    elif currentPosition == 7:
        return 4
    else:
        return -1

def checkDiagonalMoves():

    if currentPosition == 0:
        return 5,7
    elif currentPosition == 3:
        return 4,6
    elif currentPosition == 4:
        return 1,3
    elif currentPosition == 7:
        return 0,2
    else:
        return -1

def getPossibleMoves():

    move_cost = []
    specialMove = False
    for index in cornerPosition:
        if index == currentPosition: specialMove = True

    if specialMove:
        move_cost.append =

def isGoal():
    if puzzleList == firstGoalState: return True
    elif puzzleList == secondGoalState: return True
    else puzzleList == secondGoalState: return False
