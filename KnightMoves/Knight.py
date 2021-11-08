from GUI import KnightEngine
from KnightMoves import util


def isInside(x, y, boardSize):
    if x < 0 or x > boardSize - 1 or y < 0 or y > boardSize - 1:
        return False
    else:
        return True


def breadthFirstSearch(finalX, finalY, boardSize):
    visited = set()
    queue = util.Queue()
    duplicates = []
    queue.push(((0, 0), list()))
    listActions = []
    while not queue.isEmpty():
        currentPos = queue.pop()

        currentX, currentY = currentPos[0]
        if currentX == finalX and currentY == finalY:
            print("The list of actions is: ", currentPos[1])
            return currentPos[1]
        else:
            successors = getActions(currentPos[0], boardSize)
            visited.add(currentPos[0])
            for successor in successors:
                if successor[0] not in visited and successor[0] not in duplicates:
                    listActions = list(currentPos[1])
                    listActions.append(successor[1])
                    queue.push((successor[0], listActions))
                    duplicates.append(successor[0])

    return listActions


def depthFirstSearch(finalX, finalY, boardSize):
    visited = set()
    stack = util.Stack()
    stack.push(((0, 0), list()))
    listActions = []
    while not stack.isEmpty():
        currentPos = stack.pop()
        currentX, currentY = currentPos[0]
        if currentX == finalX and currentY == finalY:
            print("The list of actions is: ", currentPos[1])
            return currentPos[1]
        else:
            successors = getActions(currentPos[0], boardSize)
            visited.add(currentPos[0])
            for successor in successors:
                if successor[0] not in visited:
                    listActions = list(currentPos[1])
                    listActions.append(successor[1])
                    stack.push((successor[0], listActions))

    return listActions


def uniformCostSearch(finalX, finalY, boardSize):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = []
    queue = util.PriorityQueue()
    start = (0, 0)
    queue.push((start, [],0), 0)
    while not queue.isEmpty():
        currentPosition = queue.pop()
        currentState = currentPosition[0]
        currentX, currentY = currentPosition[0]
        path = currentPosition[1]
        if currentX == finalX and currentY == finalY:
            print("The list of actions is: ",currentPosition[1],"\nThe cost is",currentPosition[2])
            return currentPosition[1]
        if currentState not in visited:
            visited.append(currentState)
            successorsList = getActions(currentState, boardSize)
            for successor in successorsList:
                if successor[0] not in visited and successor[0] not in [nod[0] for nod in queue.heap]:
                    currentRoute = list(path)
                    currentRoute += [successor[1]]
                    cost = currentPosition[2]
                    queue.push((successor[0], currentRoute, cost + 1), cost + 1)


def matchingColors(state, finalX, finalY):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    currentX, currentY = state
    auxX = currentX % 2
    auxY = currentY % 2
    aux2X = finalX % 2
    aux2Y = finalY % 2
    if auxX == aux2X and auxY == aux2Y:
        return 2
    elif auxX == aux2X and auxY != aux2Y:
        return 1
    elif auxX != aux2X and auxY == aux2Y:
        return 1
    elif auxX != aux2X and auxY != aux2Y:
        return 2

def manhattanDistance(state, finalX, finalY):
    currentX, currentY = state
    return (abs(currentX - finalX) + abs(currentY - finalY)) / 3

def aStarSearchMC(finalX, finalY, boardSize, heuristic=matchingColors):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = []
    queue = util.PriorityQueue()
    start = (0, 0);

    startHeuristic = heuristic(start, finalX, finalY)
    queue.push((start, [], startHeuristic),startHeuristic)

    while not queue.isEmpty():
        currentPosition = queue.pop()
        currentState = currentPosition[0]
        currentX, currentY = currentPosition[0]
        if currentX == finalX and currentY == finalY:
            print("The list of actions is: ",currentPosition[1],"\nThe cost is",currentPosition[2])
            return currentPosition[1]
        if currentState not in visited:
            visited.append(currentState)
            successorsList = getActions(currentState, boardSize)
            for successor in successorsList:
                if successor[0] not in visited and successor[0] not in [nod[0] for nod in queue.heap]:
                    currentRoute = list(currentPosition[1])
                    currentRoute += [successor[1]]
                    cost = currentPosition[2]
                    getHeuristic = heuristic(successor[0], finalX, finalY)
                    queue.push((successor[0], currentRoute,  cost + getHeuristic),cost + getHeuristic)

    return []

def aStarSearchMD(finalX, finalY, boardSize, heuristic=manhattanDistance):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = []
    queue = util.PriorityQueue()
    start = (0, 0);

    startHeuristic = heuristic(start, finalX, finalY)
    queue.push((start, [], startHeuristic),startHeuristic)

    while not queue.isEmpty():
        currentPosition = queue.pop()
        currentState = currentPosition[0]
        currentX, currentY = currentPosition[0]
        if currentX == finalX and currentY == finalY:
            print("The list of actions is: ",currentPosition[1],"\nThe cost is",currentPosition[2])
            return currentPosition[1]
        if currentState not in visited:
            visited.append(currentState)
            successorsList = getActions(currentState, boardSize)
            for successor in successorsList:
                if successor[0] not in visited and successor[0] not in [nod[0] for nod in queue.heap]:
                    currentRoute = list(currentPosition[1])
                    currentRoute += [successor[1]]
                    cost = currentPosition[2]
                    getHeuristic = heuristic(successor[0], finalX, finalY)
                    queue.push((successor[0], currentRoute,  cost + getHeuristic),cost + getHeuristic)

    return []



def getActions(state, boardSize):
    possible_directions = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
    valid_actions_from_state = []
    for action in possible_directions:
        x, y = state
        nextx, nexty = int(x + action[0]), int(y + action[1])
        if isInside(nextx, nexty, boardSize):
            valid_actions_from_state.append(((nextx, nexty), action))
    return valid_actions_from_state


# depthFirstSearch(15,15)

def passMovesToGUI():
    listActions = depthFirstSearch(7, 4)
    currentX = 0
    currentY = 0
    game_state = KnightEngine.GameState()
    for action in listActions:
        move = KnightEngine.Move((currentX, currentY), (currentX + action[0], currentY + action[1]), game_state.board)
        currentX += action[0]
        currentY += action[1]
        game_state.makeMove(move)


def getMovesDFS(x, y, boardSize):
    listActions = depthFirstSearch(x, y, boardSize)
    print('Numar noduri expandate:', len(listActions))
    return listActions


def getMovesBFS(x, y, boardSize):
    listActions = breadthFirstSearch(x, y, boardSize)
    print('Numar noduri expandate:', len(listActions))
    return listActions


def getMovesUCS(x, y, boardSize):
    listActions = uniformCostSearch(x, y, boardSize)
    print('Numar noduri expandate:', len(listActions))
    return listActions


def getMovesASSMC(x, y, boardSize):
    listActions = aStarSearchMC(x, y, boardSize)
    print('Numar noduri expandate:', len(listActions))
    return listActions

def getMovesASSMD(x, y, boardSize):
    listActions = aStarSearchMD(x, y, boardSize)
    print('Numar noduri expandate:', len(listActions))
    return listActions
