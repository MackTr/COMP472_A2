goal = [1, 2, 3, 4, 5, 6, 7, 0]
board = [4, 2, 3, 1, 5, 6, 7, 0]


def heuristicSimple(board, goal):
    heuristic = 0
    for i in range(len(board)):
        if(board[i]!=goal[i]):
            heuristic += 1
    return heuristic

#print(heuristicSimple(board, goal))

open = [{
    "state": board.copy(),
    "heuristic": heuristicSimple(board, goal),
    "index": 7 
}]

def vertical(board, index):
    newIndex = (index + 4) % 8
    temp = board.copy()
    temp[index], temp[newIndex] = temp[newIndex], temp[index]
    node = [{
        "state": temp.copy(),
        "heuristic": heuristicSimple(temp, goal),
        "index": newIndex 
    }]
    open.extend(node)

def horizontalTowardsLeft(board, index):
    if index != 0 and index != 4:
        temp = board.copy()
        temp[index], temp[index-1] = temp[index-1], temp[index]
        index = index - 1
        node = [{
        "state": temp,
        "heuristic": heuristicSimple(temp, goal),
        "index": index 
        }]
        open.extend(node)
    elif index == 0:
        temp = board.copy()
        temp[index], temp[index+3] = temp[index+3], temp[index]
        index = index + 3
        node = [{
        "state": temp,
        "heuristic": heuristicSimple(temp, goal),
        "index": index 
        }]
        open.extend(node)
    elif index == 4:
        temp = board.copy()
        temp[index], temp[index+3] = temp[index+3], temp[index]
        index = index + 3
        node = [{
        "state": temp,
        "heuristic": heuristicSimple(temp, goal),
        "index": index 
        }]
        open.extend(node)
 

def horizontalTowardsRight(board, index):
    if index != 3 and index != 7:
        temp = board.copy()
        temp[index], temp[index+1] = temp[index+1], temp[index]
        index = index + 1
        node = [{
        "state": temp,
        "heuristic": heuristicSimple(temp, goal),
        "index": index 
        }]
        open.extend(node)
    elif index == 3:
        temp = board.copy()
        temp[index], temp[index-3] = temp[index-3], temp[index]
        index = index - 3
        node = [{
        "state": temp,
        "heuristic": heuristicSimple(temp, goal),
        "index": index 
        }]
        open.extend(node)
    elif index == 7:
        temp = board.copy()
        temp[index], temp[index-3] = temp[index-3], temp[index]
        index = index - 3
        node = [{
        "state": temp,
        "heuristic": heuristicSimple(temp, goal),
        "index": index 
        }]
        open.extend(node)

def diagonal(board, index):
    if index == 3:
        temp = board.copy()
        temp[index], temp[index+1] = temp[index+1], temp[index]
        index = index + 1
        node = [{
        "state": temp,
        "heuristic": heuristicSimple(temp, goal),
        "index": index 
        }]
        open.extend(node)
    elif index == 4:
        temp = board.copy()
        temp[index], temp[index-1] = temp[index-1], temp[index]
        index = index - 1
        node = [{
        "state": temp,
        "heuristic": heuristicSimple(temp, goal),
        "index": index 
        }]
        open.extend(node)
    elif index == 0:
        temp = board.copy()
        temp[index], temp[index+7] = temp[index+7], temp[index]
        index = index + 7
        node = [{
        "state": temp,
        "heuristic": heuristicSimple(temp, goal),
        "index": index 
        }]
        open.extend(node)
    elif index == 7:
        temp = board.copy()
        temp[index], temp[index-7] = temp[index-7], temp[index]
        index = index - 7
        node = [{
        "state": temp,
        "heuristic": heuristicSimple(temp, goal),
        "index": index 
        }]
        open.extend(node)

vertical(board, 7)
horizontalTowardsLeft(board, 7)
horizontalTowardsRight(board, 7)
diagonal(board, 7)
print(open)
#open = sorted(open, key=lambda k: k['heuristic'])
#print(open)