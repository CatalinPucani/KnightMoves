from KnightMoves import util
import sys
from GUI import ChessEngine, ChessMain
boardSize = 8
def isInside(x,y):
    if(x<0 or x>boardSize-1 or y<0 or y>boardSize-1):
        return False
    else:
        return True

def breadthFirstSearch(finalX, finalY):

    visited = set()
    queue = util.Queue()
    queue.push(((0,0),list()))
    listActions = []
    while not queue.isEmpty():
       currentPos=queue.pop()
       print(currentPos)
       currentX,currentY=currentPos[0]
       if(currentX == finalX and currentY ==finalY):
          print(currentPos[1])
          return currentPos[1]
       else:
          successors=getActions(currentPos[0])
          visited.add(currentPos[0])
          for successor in successors:
              if(successor[0] not in visited):
                listActions=list(currentPos[1])
                listActions.append(successor[1])
                queue.push((successor[0],listActions))

    return listActions

def depthFirstSearch(finalX, finalY):

    visited = set()
    stack = util.Stack()
    stack.push(((0,0),list()))
    listActions = []
    while not stack.isEmpty():
       currentPos=stack.pop()
       currentX,currentY=currentPos[0]
       if(currentX == finalX and currentY ==finalY):
          print(currentPos[1])
          return currentPos[1]
       else:
          successors=getActions(currentPos[0])
          visited.add(currentPos[0])
          for successor in successors:
              if(successor[0] not in visited):
                listActions=list(currentPos[1])
                listActions.append(successor[1])
                stack.push((successor[0],listActions))

    return listActions

def uniformCostSearch(finalX,finalY):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = []
    queue = util.PriorityQueue()
    start = (0,0)
    queue.push((start, []), 0)
    while not queue.isEmpty():
        currentPosition = queue.pop()
        currentState = currentPosition[0]
        currentX,currentY=currentPosition[0]
        path = currentPosition[1]
        if (currentX == finalX and currentY == finalY):
            print(currentPosition[1])
            return currentPosition[1]
        if currentState not in visited:
            visited.append(currentState)
            successorsList = getActions(currentState)
            for successor in successorsList:
                if successor[0] not in visited:
                    currentRoute = list(path)
                    currentRoute += [successor[1]]
                    cost = 1
                    queue.push((successor[0], currentRoute), cost)



def nullHeuristic(state, finalX=None,finalY=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(finalX,finalY, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited = []
    queue = util.PriorityQueue()
    start = (0,0) ; "pozitia 0"
    startHeuristic = heuristic(start, finalX,finalY)
    queue.push((start, [], 0), startHeuristic)

    while not queue.isEmpty():
        currentPosition = queue.pop()
        currentState = currentPosition[0]
        currentX,currentY=currentPosition[0]
        if (currentX == finalX and currentY == finalY):
            print(currentPosition[1])
            return currentPosition[1]
        if currentState not in visited:
            visited.append(currentState)
            successorsList = getActions(currentState)
            for successor in successorsList:
                if successor[0] not in visited:
                    currentRoute = list(currentPosition[1])
                    currentRoute += [successor[1]]
                    cost = 1
                    getHeuristic = heuristic(successor[0], finalX,finalY)
                    queue.push((successor[0], currentRoute, 1), cost + getHeuristic)

    return []

def getActions(state):
        possible_directions = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
        valid_actions_from_state = []
        for action in possible_directions:
            x, y = state
            nextx, nexty = int(x + action[0]), int(y + action[1])
            if isInside(nextx,nexty):
                valid_actions_from_state.append(((nextx,nexty),action))
        return valid_actions_from_state

#depthFirstSearch(15,15)

def passMovesToGUI():
    listActions = depthFirstSearch(7,4)
    currentX = 0
    currentY = 0
    game_state = ChessEngine.GameState()
    for action in listActions:
        move = ChessEngine.Move((currentX,currentY), (currentX + action[0], currentY + action[1]), game_state.board)
        currentX += action[0]
        currentY += action[1]
        game_state.makeMove(move)

def getMovesDFS(x, y):
    listActions = depthFirstSearch(x,y)
    return listActions

def getMovesBFS(x, y):
    listActions = breadthFirstSearch(x,y)
    return listActions

def getMovesUCS(x, y):
    listActions = uniformCostSearch(x,y)
    return listActions

def getMovesASS(x, y):
    listActions = aStarSearch(x,y)
    return listActions