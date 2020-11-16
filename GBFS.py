goal = [1, 2, 3, 4, 5, 6, 7, 0]
board = [2, 1, 4, 3, 5, 6, 7, 0]


def heuristicSimple(board, goal):
    heuristic = 0
    for i in range(len(board)):
        if(board[i]!=goal[i]):
            heuristic += 1
    return heuristic

#print(heuristicSimple(board, goal))

open = [{
    "currentBoard": board.copy(),
    "heuristic": heuristicSimple(board, goal) 
}]


def vertical(board, index):
    newIndex = (index + 4) % 8
    temp = board.copy()
    temp[index], temp[newIndex] = temp[newIndex], temp[index]
    successor = [{
        "currentBoard": temp.copy(),
        "heuristic": heuristicSimple(temp, goal) 
    }]
    open.extend(successor)

def horizontalTowardsLeft(board, index):
    if index != 3 or index != 7:
        temp = board.copy()
        temp[index], temp[index-1] = temp[index-1], temp[index]
        successor = [{
        "currentBoard": temp,
        "heuristic": heuristicSimple(temp, goal) 
        }]
        open.extend(successor)
 

def horizontalTowardsRight(board, index):
    if index != 0 or index != 4:
        temp = board.copy()
        temp[index], temp[index+1] = temp[index+1], temp[index]
        successor = [{
        "currentBoard": temp,
        "heuristic": heuristicSimple(temp, goal) 
        }]
        open.extend(successor)

def sortByHeu(successor):              # a faire
    for option in successor:
        heuristicSimple(option, goal)




vertical(board, 7)
horizontalTowardsLeft(board, 7)
print(open)
sorted(open, key=lambda h: (h.heuristic))